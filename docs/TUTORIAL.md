# 🎯 Tutorial Completo - Conversação por Voz com ChatGPT

## 🎯 Objetivo

Este tutorial irá guiá-lo passo a passo na construção e uso de um assistente de voz integrado com ChatGPT, Whisper e gTTS.

## 📑 Conteúdo

1. [Entendendo a Arquitetura](#arquitetura)
2. [Configuração do Ambiente](#configuracao)
3. [Componentes do Sistema](#componentes)
4. [Passo a Passo de Uso](#uso)
5. [Personalizações](#personalizacoes)
6. [Solução de Problemas](#problemas)

## 🏗️ Arquitetura

### Fluxo de Dados

```
🎙️ Usuário fala
    ↓
💾 Gravação de áudio (PyAudio)
    ↓
🔊 Transcrição (Whisper)
    ↓
🤖 Processamento (ChatGPT)
    ↓
📢 Síntese de voz (gTTS)
    ↓
🔊 Reprodução da resposta
```

### Tecnologias Principais

1. **OpenAI Whisper**: Modelo de reconhecimento de fala (ASR)
2. **ChatGPT API**: Modelo de linguagem para gerar respostas
3. **gTTS**: Google Text-to-Speech para sintetizar voz
4. **PyAudio**: Captura de áudio do microfone

## ⚙️ Configuração

### 1. Obter API Key da OpenAI

1. Acesse [platform.openai.com](https://platform.openai.com)
2. Faça login ou crie uma conta
3. Vá em "API Keys"
4. Clique em "Create new secret key"
5. Copie e guarde sua chave com segurança

### 2. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```bash
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxx
```

### 3. Instalar Dependências do Sistema

#### Windows
```bash
# Instalar FFmpeg
choco install ffmpeg

# Instalar PortAudio (para PyAudio)
# Baixe o instalador em: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
```

#### macOS
```bash
brew install ffmpeg
brew install portaudio
```

#### Linux
```bash
sudo apt update
sudo apt install ffmpeg portaudio19-dev python3-pyaudio
```

## 📦 Componentes

### 1. Gravação de Áudio

```python
def record_audio(self, filename="input.wav", duration=5):
    """Grava áudio do microfone usando PyAudio"""
    audio = pyaudio.PyAudio()
    stream = audio.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True
    )
    # ... gravação ...
```

**Parâmetros importantes:**
- `RATE`: Taxa de amostragem (44100 Hz é padrão CD)
- `CHANNELS`: Mono (1) ou Stereo (2)
- `FORMAT`: Formato dos dados (paInt16 = 16 bits)

### 2. Transcrição com Whisper

```python
def transcribe_audio(self, audio_file):
    """Transcreve áudio usando OpenAI Whisper"""
    with open(audio_file, "rb") as file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=file,
            language="pt"  # Especifica o idioma
        )
    return transcription.text
```

**Idiomas suportados:**
- `pt`: Português
- `en`: Inglês
- `es`: Espanhol
- `fr`: Francês
- E mais de 90 outros idiomas

### 3. Processamento com ChatGPT

```python
def chat_with_gpt(self, user_message):
    """Envia mensagem para ChatGPT"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Prompt do sistema"},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7,  # Criatividade
        max_tokens=500    # Tamanho máximo
    )
    return response.choices[0].message.content
```

**Parâmetros:**
- `temperature`: 0.0 (determinístico) a 1.0 (criativo)
- `max_tokens`: Limita o tamanho da resposta
- `model`: `gpt-3.5-turbo` ou `gpt-4`

### 4. Síntese de Voz com gTTS

```python
def text_to_speech(self, text, filename="response.mp3"):
    """Converte texto em áudio"""
    tts = gTTS(text=text, lang='pt', slow=False)
    tts.save(filename)
    return filename
```

**Configurações:**
- `lang`: Idioma da voz
- `slow`: Velocidade da fala (False = normal)

## 🎮 Uso

### Execução Básica

```bash
python main.py
```

### Fluxo de Interação

1. **Início**: O programa exibe o cabeçalho
2. **Prompt**: "Pressione Enter para começar a gravar..."
3. **Gravação**: Fale sua pergunta
4. **Transcrição**: Seu áudio é convertido em texto
5. **Processamento**: ChatGPT gera uma resposta
6. **Reprodução**: A resposta é falada em voz
7. **Loop**: Retorna ao passo 2

### Comandos de Voz

Para encerrar o programa, diga:
- "sair"
- "encerrar"
- "tchau"

Ou pressione `Ctrl+C`

## 🎨 Personalizações

### 1. Alterar o Modelo do ChatGPT

```python
# No método chat_with_gpt
model="gpt-4"  # Mais preciso, porém mais caro
```

### 2. Ajustar Criatividade

```python
temperature=0.3  # Mais conservador
temperature=0.9  # Mais criativo
```

### 3. Mudar Idioma

```python
# Whisper
language="en"  # Inglês

# gTTS
lang='en'  # Inglês
```

### 4. Personalizar Prompt do Sistema

```python
system_prompt = """
Você é um especialista em automação industrial.
Responda de forma técnica mas acessível.
"""
```

### 5. Ajustar Duração da Gravação

```python
audio_file = self.record_audio(duration=15)  # 15 segundos
```

## 🔧 Solução de Problemas

### Erro: "OPENAI_API_KEY não configurada"

**Solução:**
```bash
# Crie o arquivo .env
echo "OPENAI_API_KEY=sua_chave_aqui" > .env
```

### Erro: "PyAudio não encontrado"

**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**Linux:**
```bash
sudo apt install portaudio19-dev
pip install pyaudio
```

### Erro: "FFmpeg não encontrado"

**Solução:**
Instale o FFmpeg conforme seu sistema operacional (ver seção de configuração)

### Áudio não é reproduzido

**Solução:**
```bash
# Teste alternativas ao playsound
pip install pygame

# Substitua no código:
import pygame
pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play()
```

### Transcrição incorreta

**Dicas:**
- Fale claramente e devagar
- Reduza ruído de fundo
- Use um microfone de qualidade
- Especifique o idioma correto no Whisper

## 📊 Custos Estimados

### OpenAI API

- **Whisper**: $0.006 por minuto de áudio
- **GPT-3.5-turbo**: $0.0015 por 1K tokens (input)
- **GPT-4**: $0.03 por 1K tokens (input)

### Exemplo de Uso

10 conversas de 1 minuto cada:
- Whisper: 10 min × $0.006 = $0.06
- GPT-3.5: ~20K tokens × $0.0015 = $0.03
- **Total**: ~$0.09

## 🚀 Próximos Passos

1. Adicionar interface gráfica (Streamlit/Gradio)
2. Implementar detecção automática de idioma
3. Suporte a múltiplas vozes com gTTS
4. Integrar com bases de conhecimento (RAG)
5. Adicionar memória de longo prazo

## 📚 Recursos Adicionais

- [Documentação OpenAI](https://platform.openai.com/docs)
- [Whisper GitHub](https://github.com/openai/whisper)
- [gTTS Documentação](https://gtts.readthedocs.io/)
- [PyAudio Documentação](http://people.csail.mit.edu/hubert/pyaudio/)

---

**Feito com ❤️ para o Bootcamp DIO CAIXA**
