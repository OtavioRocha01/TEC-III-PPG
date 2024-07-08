import csv
import requests
import os
import time

import Aluno


# LÊ UM ARQUIVO CSV E RETORNA UMA LISTA DE INSTÂNCIAS DE ALUNO
def ler_arquivo_csv(nome_arquivo):
     alunos = []
     # abre o arquivo -- encoding utf-8 é necessário para fazer a leitura corretamente
     with open(nome_arquivo, encoding='utf-8') as arquivo:
          leitor = csv.DictReader(arquivo)
          for linha in leitor:
               aluno = Aluno.Aluno(linha)  
               alunos.append(aluno)
     return alunos


# BAIXA UM ARQUIVO DE UMA URL E SALVA EM UM DIRETÓRIO ESPECIFICO
def baixar_arquivos(alunos):
     # n recebe a quantidade de alunos
     n = len(alunos)

     for i in range(n):
          # salva os links dentro de uma lista
          links = [alunos[i].projeto_doutorado, alunos[i].comprovacao_publicacao1, alunos[i].comprovacao_publicacao2, alunos[i].comprovacao_publicacao3,
               alunos[i].comprovacao_publicacao4, alunos[i].comprovacao_publicacao5, alunos[i].diploma_graduacao, alunos[i].diploma_mestrado, 
               alunos[i].historico_graduacao, alunos[i].historico_mestrado, alunos[i].identidade, alunos[i].cpf_doc, alunos[i].titulo_eleitor,
               alunos[i].certificado_militar, alunos[i].certidao_casamento, alunos[i].comprovante_pagamento]
          nome_dir = alunos[i].nome_completo

          # cria um diretório com o nome do aluno
          os.makedirs(nome_dir, exist_ok=True)

          count = 0
          # itera sobre a lista de links e invoca a função para baixar o arquivo pelo url
          for doc in ['projeto_doutorado', 'comprovacao_publicacao1', 'comprovacao_publicacao2', 'comprovacao_publicacao3', 
                    'comprovacao_publicacao4', 'comprovacao_publicacao5', 'diploma_graduacao', 'diploma_mestrado',
                    'historico_graduacao', 'historico_mestrado', 'identidade', 'cpf_doc', 'titulo_eleitor', 
                    'certificado_militar', 'certidao_casamento', 'comprovante_pagamento']:
               url = links[count]
               if url:
                    baixar_pelo_link(url, f'{nome_dir}/{doc}.pdf')
               count += 1


# RECEBE O URL PARA DOWNLOAD E O CAMINHO PARA SALVAR O ARQUIVO
def baixar_pelo_link(url, destino, max_retries=5):
    for attempt in range(max_retries):
        try:
            resposta = requests.get(url)
            resposta.raise_for_status()
            with open(destino, 'wb') as f:
                f.write(resposta.content)
            break  # Success, exit the loop
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:  # Too Many Requests
                wait = 2 ** attempt  # Exponential backoff
                print(f"Waiting {wait} seconds before retrying...")
                time.sleep(wait)
            else:
                raise  # Reraise the exception if it's not a 429 error


# SEPARA OS ALUNOS DE MESTRADO
def separar_mestres(alunos):
     mestres = []
     for aluno in alunos:
          if aluno.get_tipo_inscricao() == 'Mestrado':
               mestres.append(aluno)
     return mestres


# SEPARA OS ALUNOS DE DOUTORADO
def separar_doutores(alunos):
     doutores = []
     for aluno in alunos:
          if aluno.get_tipo_inscricao() == 'Doutorado':
               doutores.append(aluno)
     return doutores


# ATUALIZA A NOTA E A MÉDIA DO HISTÓRICO DOS ALUNOS
def get_media_historico(arquivo, alunos):
     with open(arquivo, encoding='utf-8') as arquivo:
          leitor = csv.DictReader(arquivo)
          for linha in leitor:
               nome = linha['Nome Completo']
               cpf = linha['CPF']
               media = float(linha['Media Historico da Graduacao'])
               if media > 5.0:
                    nota = 5.0
               else:
                    nota = 0.0
               for aluno in alunos:
                    if aluno.nome_completo == nome and aluno.cpf == cpf:
                         aluno.nota_historico = nota
                         aluno.media_historico = media


# CONVERTE A QUALIS EM NOTA
def convert_qualis(qualis, autor):
     nota = 0
     if qualis == 'A1':
          if autor == 1:
               nota = 5.0
          else:
               nota = 1.67
     elif qualis == 'A2':
          if autor == 1:
               nota = 4.38
          else:
               nota = 1.46
     elif qualis == 'A3':
          if autor == 1:
               nota = 3.75
          else:
               nota = 1.25
     elif qualis == 'A4':
          if autor == 1:
               nota = 3.13
          else:
               nota = 1.00
     elif qualis == 'B1':
          if autor == 1:
               nota = 2.5
          else:
               nota = 0.83
     elif qualis == 'B2':
          if autor == 1:
               nota = 1.0
          else:
               nota = 0.33
     elif qualis == 'B3':
          if autor == 1:
               nota = 0.5
          else:
               nota = 0.17
     elif qualis == 'B4':
          if autor == 1:
               nota = 0.25
          else:
               nota = 0.08
     elif qualis == 'Sem Qualis':
          if autor == 1:
               nota = 0.2
          else:
               nota = 0.06
     else:
          nota = 0

     return nota


# ATUALIZA A NOTA E A MÉDIA DAS PUBLICAÇÕES DOS ALUNOS
def get_media_publicacoes(alunos):
     for aluno in alunos:
          soma = 0
          prim_autor = 0 
          count = 0

          if aluno.qualis_publicacao1:
               qualis = aluno.qualis_publicacao1
               count += 1
               if aluno.primeiro_autor1 == 'Sim':
                    prim_autor = 1
               else:
                    prim_autor = 0
               nota = convert_qualis(qualis, prim_autor)
               aluno.nota_publicacao1 = nota
               soma += nota
          else:
               nota += 0 

          if aluno.qualis_publicacao2:
               qualis = aluno.qualis_publicacao2
               count += 1
               if aluno.primeiro_autor2 == 'Sim':
                    prim_autor = 1
               else:
                    prim_autor = 0
               nota = convert_qualis(qualis, prim_autor)
               aluno.nota_publicacao2 = nota
               soma += nota
          else:
               nota += 0 
          
          if aluno.qualis_publicacao3:
               qualis = aluno.qualis_publicacao3
               count += 1
               if aluno.primeiro_autor3 == 'Sim':
                    prim_autor = 1
               else:
                    prim_autor = 0
               nota = convert_qualis(qualis, prim_autor)
               aluno.nota_publicacao3 = nota
               soma += nota
          else:
               nota += 0 
          
          if aluno.qualis_publicacao4:
               qualis = aluno.qualis_publicacao4
               count += 1
               if aluno.primeiro_autor4 == 'Sim':
                    prim_autor = 1
               else:
                    prim_autor = 0
               nota = convert_qualis(qualis, prim_autor)
               aluno.nota_publicacao4 = nota
               soma += nota
          else:
               nota += 0 
     
          if aluno.qualis_publicacao5:
               qualis = aluno.qualis_publicacao5
               count += 1
               if aluno.primeiro_autor5 == 'Sim':
                    prim_autor = 1
               else:
                    prim_autor = 0
               nota = convert_qualis(qualis, prim_autor)
               aluno.nota_publicacao5 = nota
               soma += nota
          else:
               nota += 0 

          media = soma / count
          aluno.media_publicacoes = media


# ATUALIZA A NOTA FINAL DOS ALUNOS
def get_nota_final(alunos):
     for aluno in alunos:
          nota_final = aluno.nota_historico + aluno.media_publicacoes
          aluno.nota_final = nota_final


# ESCREVE UM ARQUIVO CSV COM O RANKING FINAL DOS ALUNOS
def escrever_arquivo_csv(alunos):
     with open('ranking_final.csv', 'w', newline='', encoding='utf-8') as arquivo:
          escritor = csv.writer(arquivo)
          escritor.writerow(['Nome Completo', 'CPF', 'Nota Final'])
          for aluno in alunos:
               escritor.writerow([aluno.nome_completo, aluno.cpf, aluno.nota_final])


def main():
     arquivo = 'inscricoes.csv'
     alunos = ler_arquivo_csv(arquivo)
     baixar_arquivos(alunos)
     
     # MESTRES
     mestres = separar_mestres(alunos)
     get_media_historico('Historicos.csv', mestres)
     get_media_publicacoes(mestres)

     # DOUTORES
     doutores = separar_doutores(alunos)
     get_media_historico('Historicos.csv', doutores)
     get_media_publicacoes(doutores)

     get_nota_final(alunos)

     ranking_final = []
     for aluno in alunos:
          ranking_final.append(aluno)
     
     ranking_final.sort(key=lambda x: x.nota_final, reverse=True)

     print('Ranking Final:')
     for i in range(len(ranking_final)):
          print(f'{i+1}º lugar: {ranking_final[i].nome_completo} - {ranking_final[i].nota_final}')

     escrever_arquivo_csv(ranking_final)
     
if __name__ == '__main__':
     main()