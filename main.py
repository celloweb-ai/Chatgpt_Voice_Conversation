#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Conversação por Voz com ChatGPT
Utilizando Whisper (OpenAI) e gTTS

Desafio: Bootcamp CAIXA - IA Generativa (DIO)
Autor: celloweb-ai
Data: Dezembro 2025
"""

import os
import sys
import time
from datetime import datetime
from pathlib import Path

try:
    import pyaudio
    import wave
    from openai import OpenAI
    from gtts import gTTS
    from playsound import playsound
    from dotenv import load_dotenv
    from colorama import Fore, Style, init
except ImportError as e:
    print(f"Erro ao importar dependências: {e}")
    print("Execute: pip install -r requirements.txt")
    sys.exit(1)

# Inicializar colorama para cores no terminal
init(autoreset=True)

# Carregar variáveis de ambiente
load_dotenv()

# Configurações
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    print(f"{Fore.RED}Erro: OPENAI_API_KEY não configurada!")
    print(f"{Fore.YELLOW}Configure sua chave no arquivo .env")
    sys.exit(1)

# Cliente OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

# Configurações de áudio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10

# Diretórios
AUDIO_DIR = Path("audio")
CONVERSATIONS_DIR = Path("conversations")
AUDIO_DIR.mkdir(exist_ok=True)
CONVERSATIONS_DIR.mkdir(exist_ok=True)


class VoiceAssistant:
    """Assistente de voz integrado com ChatGPT, Whisper e gTTS"""
    
    def __init__(self):
        self.conversation_history = []
        self.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        
    def print_header(self):
        """Exibe o cabeçalho do programa"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}🎤 ASSISTENTE DE VOZ COM CHATGPT")
        print(f"{Fore.CYAN}Bootcamp DIO CAIXA - IA Generativa")
        print(f"{Fore.CYAN}{'='*60}\n")
        
    def record_audio(self, filename="input.wav", duration=5):
        """Grava áudio do microfone"""
        print(f"{Fore.YELLOW}🎙️  Gravando... Fale agora! (pressione Ctrl+C para parar)\n")
        
        audio = pyaudio.PyAudio()
        stream = audio.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=CHUNK
        )
        
        frames = []
        try:
            for i in range(0, int(RATE / CHUNK * duration)):
                data = stream.read(CHUNK)
                frames.append(data)
        except KeyboardInterrupt:
            pass
        
        print(f"{Fore.GREEN}✓ Gravação finalizada!\n")
        
        stream.stop_stream()
        stream.close()
        audio.terminate()
        
        # Salvar arquivo
        filepath = AUDIO_DIR / filename
        with wave.open(str(filepath), 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(audio.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))
        
        return filepath
    
    def transcribe_audio(self, audio_file):
        """Transcreve áudio usando Whisper"""
        print(f"{Fore.CYAN}🔊 Transcrevendo áudio com Whisper...")
        
        try:
            with open(audio_file, "rb") as file:
                transcription = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=file,
                    language="pt"  # Português
                )
            
            text = transcription.text
            print(f"{Fore.GREEN}✓ Transcrição: {Fore.WHITE}{text}\n")
            return text
            
        except Exception as e:
            print(f"{Fore.RED}Erro na transcrição: {e}")
            return None
    
    def chat_with_gpt(self, user_message):
        """Envia mensagem para ChatGPT e recebe resposta"""
        print(f"{Fore.CYAN}🤖 Processando com ChatGPT...")
        
        try:
            # Adicionar mensagem ao histórico
            self.conversation_history.append({
                "role": "user",
                "content": user_message
            })
            
            # Chamar API do ChatGPT
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente prestativo e amigável. Responda de forma clara e concisa."},
                    *self.conversation_history
                ],
                temperature=0.7,
                max_tokens=500
            )
            
            assistant_message = response.choices[0].message.content
            
            # Adicionar resposta ao histórico
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            print(f"{Fore.GREEN}✓ Resposta: {Fore.WHITE}{assistant_message}\n")
            return assistant_message
            
        except Exception as e:
            print(f"{Fore.RED}Erro ao comunicar com ChatGPT: {e}")
            return None
    
    def text_to_speech(self, text, filename="response.mp3"):
        """Converte texto em áudio usando gTTS"""
        print(f"{Fore.CYAN}🔊 Gerando áudio com gTTS...")
        
        try:
            filepath = AUDIO_DIR / filename
            tts = gTTS(text=text, lang='pt', slow=False)
            tts.save(str(filepath))
            
            print(f"{Fore.GREEN}✓ Áudio gerado com sucesso!\n")
            return filepath
            
        except Exception as e:
            print(f"{Fore.RED}Erro ao gerar áudio: {e}")
            return None
    
    def play_audio(self, audio_file):
        """Reproduz arquivo de áudio"""
        print(f"{Fore.YELLOW}🔊 Reproduzindo resposta...\n")
        
        try:
            playsound(str(audio_file))
            print(f"{Fore.GREEN}✓ Reprodução concluída!\n")
        except Exception as e:
            print(f"{Fore.RED}Erro ao reproduzir áudio: {e}")
    
    def save_conversation(self):
        """Salva histórico da conversa"""
        filepath = CONVERSATIONS_DIR / f"conversation_{self.session_id}.txt"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"Conversação - {self.session_id}\n")
            f.write("="*60 + "\n\n")
            
            for msg in self.conversation_history:
                role = "Usuário" if msg["role"] == "user" else "Assistente"
                f.write(f"{role}: {msg['content']}\n\n")
        
        print(f"{Fore.GREEN}✓ Conversa salva em: {filepath}\n")
    
    def run(self):
        """Executa o loop principal do assistente"""
        self.print_header()
        
        print(f"{Fore.YELLOW}Digite 'sair' ou pressione Ctrl+C para encerrar\n")
        
        try:
            while True:
                input(f"{Fore.CYAN}Pressione Enter para começar a gravar... ")
                
                # 1. Gravar áudio
                audio_file = self.record_audio(duration=10)
                
                # 2. Transcrever com Whisper
                user_text = self.transcribe_audio(audio_file)
                
                if not user_text:
                    continue
                
                # Verificar comando de saída
                if user_text.lower() in ['sair', 'encerrar', 'tchau']:
                    print(f"{Fore.YELLOW}Encerrando...")
                    break
                
                # 3. Processar com ChatGPT
                response_text = self.chat_with_gpt(user_text)
                
                if not response_text:
                    continue
                
                # 4. Converter resposta em áudio
                response_audio = self.text_to_speech(response_text)
                
                if response_audio:
                    # 5. Reproduzir resposta
                    self.play_audio(response_audio)
                
                print(f"{Fore.CYAN}{'-'*60}\n")
                
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Programa interrompido pelo usuário")
        
        finally:
            # Salvar conversa ao encerrar
            if self.conversation_history:
                self.save_conversation()
            
            print(f"\n{Fore.CYAN}Até logo! 👋\n")


def main():
    """Função principal"""
    assistant = VoiceAssistant()
    assistant.run()


if __name__ == "__main__":
    main()
