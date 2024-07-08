class Aluno:
     def __init__(self, linha):
          self.nome_completo = linha.get('Nome Completo')
          self.data_nascimento = linha.get('Data de nascimento')
          self.email = linha.get('Seu e-mail')
          self.nome_mae = linha.get('Nome da mãe')
          self.cpf = linha.get('CPF')
          self.carteira_identidade = linha.get('Carteira de Identidade, no caso de candidatas/os de nacionalidade brasileira, ou passaporte, no caso de candidatas/os de nacionalidade estrangeira')
          self.data_emissao_ci = linha.get('Data de emissão da carteira de identidade')
          self.orgao_emissor_ci = linha.get('Órgão emissor da carteira de identidade e estado emissor')
          self.numero_titulo_eleitoral = linha.get('Número do título eleitoral')
          self.serie_documento_militar = linha.get('Número de série do documento militar')
          self.endereco_residencial = linha.get('Endereço residencial')
          self.cidade_residencia = linha.get('Cidade de residência')
          self.estado_residencia = linha.get('Estado de residência')
          self.telefone_contato = linha.get('Telefone para contato')
          self.link_curriculo_lattes = linha.get('Link para o currículo Lattes')
          self.reservas_vagas = linha.get('Reservas de vagas')
          self.siape = linha.get('Informe o número do seu SIAPE ligado a UFPel para confirmar a candidatura às quotas de vagas para servidores da Universidade')
          self.nome_curso1 = linha.get('Nome do Curso')
          self.tipo_curso1 = linha.get('Tipo de curso')
          self.instituicao1 = linha.get('Instituição')
          self.ano_conclusao1 = linha.get('Ano de conclusão')
          self.nome_curso2 = linha.get('Nome do curso')
          self.tipo_curso2 = linha.get('Tipo de curso')
          self.instituicao2 = linha.get('Instituição')
          self.ano_conclusao2 = linha.get('Ano de conclusão')
          self.local_trabalho = linha.get('Local de trabalho')
          self.atuacao = linha.get('Atuação')
          self.ingles_leitura = linha.get('Língua Inglesa (Leitura)')
          self.ingles_escrita = linha.get('Língua Inglesa (Escrita)')
          self.ingles_fala = linha.get('Língua Inglesa (Fala)')
          self.tipo_inscricao = linha.get('Tipo de inscrição')
          self.semestre_ingresso = linha.get('Em que semestre faria o ingresso?')
          self.orientador_preferencial = linha.get('Orientador preferencial')
          self.segunda_opcao = linha.get('Segunda opção')
          self.terceira_opcao = linha.get('Terceira opção')
          self.dedicacao_integral = linha.get('Você teria dedicação integral para o curso?')
          self.vinculo_empregaticio = linha.get('Você manteria vínculo empregatício durante a execução do curso?')
          self.interesse_bolsa = linha.get('Você tem interesse em concorrer a uma bolsa do programa?')
          self.projeto_doutorado = linha.get('Enviar arquivo PDF contendo o Projeto de Doutorado e Memorial Acadêmico, conforme especificado no edital.')
          self.titulo_publicacao1 = linha.get('Título da publicação')
          self.local_publicacao1 = linha.get('Local de publicação')
          self.tipo_publicacao1 = linha.get('Tipo da publicação')
          self.qualis_publicacao1 = linha.get('Qualis do local de publicação')
          self.nota_publicacao1 = 0.0
          self.comprovacao_publicacao1 = linha.get('Comprovação de publicação ou aceite de publicação (PDF)')
          self.primeiro_autor1 = linha.get('Primeiro autor')
          self.titulo_publicacao2 = linha.get('Título da publicação')
          self.local_publicacao2 = linha.get('Local de publicação')
          self.tipo_publicacao2 = linha.get('Tipo da publicação')
          self.qualis_publicacao2 = linha.get('Qualis do local de publicação')
          self.nota_publicacao2 = 0.0
          self.comprovacao_publicacao2 = linha.get('Comprovação de publicação ou aceite de publicação (PDF)')
          self.primeiro_autor2 = linha.get('Primeiro autor')
          self.titulo_publicacao3 = linha.get('Título da publicação')
          self.local_publicacao3 = linha.get('Local de publicação')
          self.tipo_publicacao3 = linha.get('Tipo da publicação')
          self.qualis_publicacao3 = linha.get('Qualis do local de publicação')
          self.nota_publicacao3 = 0.0
          self.comprovacao_publicacao3 = linha.get('Comprovação de publicação ou aceite de publicação (PDF)')
          self.primeiro_autor3 = linha.get('Primeiro autor')
          self.titulo_publicacao4 = linha.get('Título da publicação')
          self.local_publicacao4 = linha.get('Local de publicação')
          self.tipo_publicacao4 = linha.get('Tipo da publicação')
          self.qualis_publicacao4 = linha.get('Qualis do local de publicação')
          self.nota_publicacao4 = 0.0
          self.comprovacao_publicacao4 = linha.get('Comprovação de publicação ou aceite de publicação (PDF)')
          self.primeiro_autor4 = linha.get('Primeiro autor')
          self.titulo_publicacao5 = linha.get('Título da publicação')
          self.local_publicacao5 = linha.get('Local de publicação')
          self.tipo_publicacao5 = linha.get('Tipo da publicação')
          self.qualis_publicacao5 = linha.get('Qualis do local de publicação')
          self.nota_publicacao5 = 0.0
          self.comprovacao_publicacao5 = linha.get('Comprovação de publicação ou aceite de publicação (PDF)')
          self.primeiro_autor5 = linha.get('Primeiro autor')
          self.media_publicacoes = 0.0
          self.curriculo_lattes = linha.get('Currículo Lattes')
          self.diploma_graduacao = linha.get('Diploma de graduação OU atestado de conclusão de curso OU atestado de provável formando OU atestado de provável formando indicando que irá concluir o curso até 30 de julho de 2023 no caso de ingresso em 2023/2')
          self.diploma_mestrado = linha.get('Se aplicável, cópia do diploma de mestrado OU comprovação de cumprimento de todos requisitos para obtenção do diploma OU atestado indicando que irá concluir o seu curso de mestrado até 30 de julho de 2023 no caso de ingresso em 2023/2')
          self.historico_graduacao = linha.get('Histórico escolar de Graduação')
          self.historico_mestrado = linha.get('Histórico escolar de Mestrado')
          self.identidade = linha.get('Carteira de Identidade')
          self.cpf_doc = linha.get('CPF, se não disponível na carteira de identidade;')
          self.titulo_eleitor = linha.get('Título de eleitor')
          self.certificado_militar = linha.get('Certificado de quitação com serviço militar, ou equivalente, se aplicável')
          self.certidao_casamento = linha.get('Certidão de Casamento, no caso de mudança do nome')
          self.comprovante_pagamento = linha.get('Comprovante de pagamento ou comprovante de isenção da taxa de inscrição')
          self.documentacao_secoes = linha.get('Documentação relativa a seção 6(l), 6(m), 6(n), 6(o), 6(p) ou 6(q), se aplicável')
          self.outro_documento = linha.get('Outro documento se necessário de acordo com o Edital')
          self.id_usuario = linha.get('ID do Usuário')
          self.timestamp = linha.get('Timestamp')
          self.last_updated = linha.get('Last Updated')
          self.created_by = linha.get('Created By')
          self.updated_by = linha.get('Updated By')
          self.draft = linha.get('Draft')
          self.ip = linha.get('IP')
          self.id_key = linha.get('ID')
          self.nota_historico = 0.0
          self.media_historico = 0.0
          self.nota_final = 0.0

     # DEFINE COMO SERÁ FEITA A IMPRESSÃO DO OBJETO
     def __str__(self):
          return f"""
          Nome Completo: {self.nome_completo}
          Data de Nascimento: {self.data_nascimento}
          Email: {self.email}
          Nome da Mãe: {self.nome_mae}
          CPF: {self.cpf}
          Carteira de Identidade: {self.carteira_identidade}
          Data de Emissão da Carteira de Identidade: {self.data_emissao_ci}
          Órgão Emissor da Carteira de Identidade: {self.orgao_emissor_ci}
          Número do Título Eleitoral: {self.numero_titulo_eleitoral}
          Número de Série do Documento Militar: {self.serie_documento_militar}
          Endereço Residencial: {self.endereco_residencial}
          Cidade de Residência: {self.cidade_residencia}
          Estado de Residência: {self.estado_residencia}
          Telefone para Contato: {self.telefone_contato}
          Link para o Currículo Lattes: {self.link_curriculo_lattes}
          Reservas de Vagas: {self.reservas_vagas}
          SIAPE: {self.siape}
          Nome do Curso 1: {self.nome_curso1}
          Tipo de Curso 1: {self.tipo_curso1}
          Instituição 1: {self.instituicao1}
          Ano de Conclusão 1: {self.ano_conclusao1}
          Nome do Curso 2: {self.nome_curso2}
          Tipo de Curso 2: {self.tipo_curso2}
          Instituição 2: {self.instituicao2}
          Ano de Conclusão 2: {self.ano_conclusao2}
          Local de Trabalho: {self.local_trabalho}
          Atuação: {self.atuacao}
          Língua Inglesa (Leitura): {self.ingles_leitura}
          Língua Inglesa (Escrita): {self.ingles_escrita}
          Língua Inglesa (Fala): {self.ingles_fala}
          Tipo de Inscrição: {self.tipo_inscricao}
          Semestre de Ingresso: {self.semestre_ingresso}
          Orientador Preferencial: {self.orientador_preferencial}
          Segunda Opção: {self.segunda_opcao}
          Terceira Opção: {self.terceira_opcao}
          Dedicação Integral: {self.dedicacao_integral}
          Vínculo Empregatício: {self.vinculo_empregaticio}
          Interesse em Bolsa: {self.interesse_bolsa}
          Projeto de Doutorado: {self.projeto_doutorado}
          Título da Publicação 1: {self.titulo_publicacao1}
          Local de Publicação 1: {self.local_publicacao1}
          Tipo da Publicação 1: {self.tipo_publicacao1}
          Qualis da Publicação 1: {self.qualis_publicacao1}
          Nota da Publicação 1: {self.nota_publicacao1}
          Comprovação de Publicação 1: {self.comprovacao_publicacao1}
          Primeiro Autor 1: {self.primeiro_autor1}
          Título da Publicação 2: {self.titulo_publicacao2}
          Local de Publicação 2: {self.local_publicacao2}
          Tipo da Publicação 2: {self.tipo_publicacao2}
          Qualis da Publicação 2: {self.qualis_publicacao2}
          Nota da Publicação 2: {self.nota_publicacao2}
          Comprovação de Publicação 2: {self.comprovacao_publicacao2}
          Primeiro Autor 2: {self.primeiro_autor2}
          Título da Publicação 3: {self.titulo_publicacao3}
          Local de Publicação 3: {self.local_publicacao3}
          Tipo da Publicação 3: {self.tipo_publicacao3}
          Qualis da Publicação 3: {self.qualis_publicacao3}
          Nota da Publicação 3: {self.nota_publicacao3}
          Comprovação de Publicação 3: {self.comprovacao_publicacao3}
          Primeiro Autor 3: {self.primeiro_autor3}
          Título da Publicação 4: {self.titulo_publicacao4}
          Local de Publicação 4: {self.local_publicacao4}
          Tipo da Publicação 4: {self.tipo_publicacao4}
          Qualis da Publicação 4: {self.qualis_publicacao4}
          Nota da Publicação 4: {self.nota_publicacao4}
          Comprovação de Publicação 4: {self.comprovacao_publicacao4}
          Primeiro Autor 4: {self.primeiro_autor4}
          Título da Publicação 5: {self.titulo_publicacao5}
          Local de Publicação 5: {self.local_publicacao5}
          Tipo da Publicação 5: {self.tipo_publicacao5}
          Qualis da Publicação 5: {self.qualis_publicacao5}
          Nota da Publicação 5: {self.nota_publicacao5}
          Comprovação de Publicação 5: {self.comprovacao_publicacao5}
          Primeiro Autor 5: {self.primeiro_autor5}
          Média das Publicações: {self.media_publicacoes}
          Currículo Lattes: {self.curriculo_lattes}
          Diploma de Graduação: {self.diploma_graduacao}
          Diploma de Mestrado: {self.diploma_mestrado}
          Histórico de Graduação: {self.historico_graduacao}
          Histórico de Mestrado: {self.historico_mestrado}
          Identidade: {self.identidade}
          CPF (Documento): {self.cpf_doc}
          Título de Eleitor: {self.titulo_eleitor}
          Certificado Militar: {self.certificado_militar}
          Certidão de Casamento: {self.certidao_casamento}
          Comprovante de Pagamento: {self.comprovante_pagamento}
          Documentação Seções: {self.documentacao_secoes}
          Outro Documento: {self.outro_documento}
          ID do Usuário: {self.id_usuario}
          Timestamp: {self.timestamp}
          Last Updated: {self.last_updated}
          Created By: {self.created_by}
          Updated By: {self.updated_by}
          Draft: {self.draft}
          IP: {self.ip}
          ID Key: {self.id_key}
          Nota do Histórico: {self.nota_historico}
          Média do Histórico: {self.media_historico}
          Nota Final: {self.nota_final}
          """

     def get_tipo_inscricao(self):
          return self.tipo_inscricao
     
     def print_reduzido(self):
          print(f"""
               Nome Completo: {self.nome_completo}
               Email: {self.email}
               Tipo de Inscrição: {self.tipo_inscricao}
               Nota Histórico: {self.nota_historico}
               Média Histórico: {self.media_historico}""")
          
     def print_notas(self):
          print(f"""
               Nota Histórico: {self.nota_historico}
               Média Histórico: {self.media_historico}
               Nota Publicação 1: {self.nota_publicacao1}
               Nota Publicação 2: {self.nota_publicacao2}
               Nota Publicação 3: {self.nota_publicacao3}
               Nota Publicação 4: {self.nota_publicacao4}
               Nota Publicação 5: {self.nota_publicacao5}
               Média Publicações: {self.media_publicacoes}""")

# END CLASS ALUNO