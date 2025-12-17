# 🎤 Conversação por Voz com ChatGPT

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenAI](https://img.shields.io/badge/OpenAI-Whisper-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Projeto desenvolvido como parte do **Bootcamp Bradesco - GenAI & Dados** da [DIO](https://www.dio.me), combinando tecnologias de **Speech-to-Text** e **Text-to-Speech** para criar uma solução de comunicação por voz com IA.

## 💡 Sobre o Projeto

Este projeto integra três tecnologias poderosas para criar uma experiência de conversação natural por voz:

- **OpenAI Whisper**: Conversão de áudio para texto (Speech-to-Text) com suporte multi-idioma
- **ChatGPT API**: Processamento de linguagem natural e geração de respostas inteligentes
- **Google Text-to-Speech (gTTS)**: Conversão de texto para áudio (Text-to-Speech)

### ✨ Funcionalidades

- 🎙️ Gravação de áudio diretamente pelo microfone
- 🔊 Transcrição automática com Whisper
- 🤖 Processamento inteligente com ChatGPT
- 🔊 Resposta em áudio com voz sintetizada
- 🌍 Suporte multi-idioma (português, inglês, espanhol e mais)
- 💾 Salva histórico de conversas

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **OpenAI API** (Whisper e ChatGPT)
- **gTTS** (Google Text-to-Speech)
- **PyAudio** (captura de áudio)
- **pydub** (processamento de áudio)

## 🚀 Começando

### Pré-requisitos

- Python 3.8 ou superior
- Conta na OpenAI com API Key
- FFmpeg instalado (para processamento de áudio)

### Instalação do FFmpeg

**Windows:**
```bash
choco install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install ffmpeg
```

### Configuração do Projeto

1. **Clone o repositório:**
```bash
git clone https://github.com/celloweb-ai/Chatgpt_Voice_Conversation.git
cd chatgpt-voice-conversation
```

2. **Crie um ambiente virtual:**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente:**

Crie um arquivo `.env` na raiz do projeto:
```bash
cp .env.example .env
```

Edite o arquivo `.env` e adicione sua chave da OpenAI:
```
OPENAI_API_KEY=sua_chave_api_aqui
```

### 🎯 Como Usar

**Executar o programa:**
```bash
python main.py
```

**Fluxo de uso:**
1. O programa solicita que você pressione Enter para começar a gravar
2. Fale sua pergunta ou comando
3. Pressione Enter novamente para parar a gravação
4. O Whisper transcreve seu áudio
5. O ChatGPT processa e gera uma resposta
6. O gTTS converte a resposta em áudio
7. A resposta é reproduzida automaticamente

## 📝 Estrutura do Projeto

```
chatgpt-voice-conversation/
│
├── main.py                 # Arquivo principal da aplicação
├── requirements.txt        # Dependências do projeto
├── .env.example            # Exemplo de variáveis de ambiente
├── .gitignore              # Arquivos ignorados pelo Git
├── README.md               # Documentação do projeto
├── audio/                  # Pasta para arquivos de áudio temporários
└── conversations/          # Histórico de conversas
```

## 📊 Exemplo de Uso

```python
# Exemplo de conversa
Você: "Qual é a capital do Brasil?"
ChatGPT: "A capital do Brasil é Brasília."

Você: "Me explique como funciona a fotossíntese"
ChatGPT: "A fotossíntese é o processo pelo qual as plantas..."
```

## ⚙️ Configurações Avançadas

### Personalizar o modelo do ChatGPT

No arquivo `main.py`, você pode ajustar:
- **Modelo**: `gpt-4`, `gpt-3.5-turbo`
- **Temperatura**: Criatividade das respostas (0.0 a 1.0)
- **Max tokens**: Tamanho máximo da resposta

### Idiomas suportados pelo Whisper

O Whisper suporta mais de 90 idiomas, incluindo:
- Português (pt)
- Inglês (en)
- Espanhol (es)
- Francês (fr)
- Alemão (de)
- E muitos outros...

## 📚 Recursos Adicionais

- [Documentação OpenAI Whisper](https://platform.openai.com/docs/guides/speech-to-text)
- [Documentação ChatGPT API](https://platform.openai.com/docs/guides/chat)
- [Documentação gTTS](https://gtts.readthedocs.io/)
- [Artigo DIO sobre o projeto](https://web.dio.me/articles/conversando-por-voz-com-o-chatgpt-utilizando-whisper-openai-e-python)

## 🤝 Contribuindo

Contribuições são sempre bem-vindas! Sinta-se à vontade para:

1. Fazer um Fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📜 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## ⚖️ Limitações e Custos

- A OpenAI API é paga. Consulte os [preços da OpenAI](https://openai.com/pricing)
- Whisper: ~$0.006 por minuto de áudio
- ChatGPT: varia conforme o modelo utilizado

## 👤 Autor

**Desenvolvido como parte do Bootcamp Bradesco - GenAI & Dados**

- GitHub: [@celloweb-ai](https://github.com/celloweb-ai)

## 🚀 Próximos Passos

- [ ] Interface gráfica com Streamlit
- [ ] Suporte a múltiplas conversas simultâneas
- [ ] Exportação de conversas em diferentes formatos
- [ ] Integração com outros modelos de TTS
- [ ] Detecção automática de idioma
- [ ] Sistema de comandos de voz para controle do app

---

<p align="center">
  Feito com ❤️ para o Bootcamp DIO Bradesco - GenAI & Dados
</p>
