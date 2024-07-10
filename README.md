# IA Social Media

## O projeto IA Social Media combina desenvolvimento e inteligência artificial para a criação de conteúdos automatizados para mídias sociais.

Atualmente o projeto contém código para geração de imagens utilizadas pelas principais mídias sociais, definido pelo tamanho recomendado de 1080x1080 pixels.

## Pré-requisitos
Para executar o código, será necessário antes instalar algumas dependências, conforma a lista a seguir:
- [Python3](https://www.python.org/downloads)
- [Ollama](https://ollama.com/download)
- [Llhama3](https://ollama.com/library/llama3)

## Instalação
Depois de ter todos os pré-requisitos instalados, será necessário executar os comandos abaixo para instalar algumas dependências do Python no projeto, portanto execute os comandos no terminal:
```
pip install ollama
pip install opencv-python
pip install Pillow
```

## Gerando imagens
Primeiramente certifique-se de que o Ollama esteja rodando, para isso você pode acessar a url [http://localhost:11434](http://localhost:11434) e vificar se a mensagem **Ollama is running** é exibida no navegador.

Feito isso, uma vez que a instalação esteja concluída (veja passos anteriores), basta executar no terminal o seguinte comando, dentro do diretório principal do projeto:
```
python .\ia_social_media_app.py
```
Pronto, feito isso a aplicação será inicializada, e a partir dai basta seguir as instruções da tela, e ao final da execução as imagens serão geradas na raiz do projeto, dento do diretório **imagens_geradas**.