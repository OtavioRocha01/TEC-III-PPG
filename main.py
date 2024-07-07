import csv
import requests
import os

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
     n = len(alunos) - 1

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
def baixar_pelo_link(url, caminho):
     resposta = requests.get(url)
     resposta.raise_for_status()
     with open(caminho, 'wb') as arquivo:
          arquivo.write(resposta.content)


def separar_mestres(alunos):
     mestres = []
     for aluno in alunos:
          if aluno.get_tipo_inscricao() == 'Mestrado':
               mestres.append(aluno)
     return mestres


def calcular_media(mestres):
     media = 0
     pass


def get_media_historico(arquivo, alunos):
     historicos = []
     with open(arquivo, encoding='utf-8') as arquivo:
          leitor = csv.DictReader(arquivo)
          print(leitor)

def main():
     arquivo = 'inscricoes - Página1.csv'
     alunos = ler_arquivo_csv(arquivo)
     #baixar_arquivos(alunos)

     #mestres = separar_mestres(alunos)

     #for mestre in mestres:
          #calcular_media(mestre)

     get_media_historico('Historicos.csv', alunos)
     
if __name__ == '__main__':
     main()