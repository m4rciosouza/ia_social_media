from gera_imagens import gerar_imagens
import ollama

print('########################################################')
print('##                  Gerar imagens                     ##')
print('########################################################\n')
print('Quantas imagens você gostaria de gerar?')
num_imagens_gerar = input()
print('Digite o assunto da imagem a ser gerada:')
prompt = input()

print("Realizando requisição para a IA, aguarde...")
response = ollama.chat(model = "llama3", messages=[
  {
    'role': 'user',
    'content': 'liste {} frase(s) sobre \'{}\'. Retorne a(s) frase(s) e em português do Brasil. Não inclua nenhum tipo de formatação, apenas as frases, uma por linha. Não adicione nenhum outro comentário, somente as frases.'.format(num_imagens_gerar, prompt),
  },
])

print('Resposta processada pela IA.\n')
print(response['message']['content'])
print('\n\n')

sentencas = response['message']['content'].splitlines()
for sentenca in sentencas:
    print('Sentença a ser utilizada para gerar a imagem: {}\n'.format(sentenca))
    if sentenca:
      gerar_imagens([sentenca])
    