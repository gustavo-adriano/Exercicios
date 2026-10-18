# 🎙️ Reconhecimento de Voz em Python

Projeto simples em Python para capturar áudio do microfone e converter em texto em tempo real utilizando a biblioteca `SpeechRecognition` integrada à API do Google.

Ideal para testar comandos de voz e entender na prática como funciona a captura de áudio com tratamento de ruído ambiente.

---

### ⚙️ Como Funciona

1. **Ajuste de Ruído:** O script analisa o som ambiente antes de escutar para melhorar a precisão.
2. **Captação:** O microfone é ativado aguardando a fala.
3. **Transcrição:** O áudio capturado é enviado para a API (em português do Brasil) e o texto é exibido direto no terminal.

---

### 🛠️ Pré-requisitos e Instalação

Você vai precisar das bibliotecas `SpeechRecognition` e `PyAudio`. Instale rodando:

```bash
pip install SpeechRecognition PyAudio