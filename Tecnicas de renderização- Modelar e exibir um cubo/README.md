# Técnicas de Renderização: Cubo 3D com OpenGL

Este é um exercício acadêmico do curso de Ciência da Computação. O objetivo do projeto é modelar e renderizar um cubo 3D no estilo *wireframe* (linhas) utilizando Python. 

A renderização da janela e captura de eventos é feita através do Pygame, enquanto os cálculos e o desenho do cubo ficam a cargo do PyOpenGL.

## 💻 Tecnologias Utilizadas
* Python 3.12
* Pygame
* PyOpenGL

## 🚀 Como executar o projeto

1. Certifique-se de ter o Python instalado (recomendado: versão 3.12).
2. Clone o repositório e abra o terminal na pasta do projeto.
3. Crie e ative um ambiente virtual:
   > python -m venv .venv
   > .venv\Scripts\activate

4. Instale as dependências necessárias:
   > pip install pygame PyOpenGL

5. Execute o arquivo principal:
   > python main.py

## ⚙️ Configurações
Por padrão, o cubo é renderizado de forma estática. Para habilitar a rotação automática contínua, basta abrir o arquivo main.py e alterar a variável habilitar_rotacao para True na linha final do código:

    if __name__ == "__main__":
        habilitar_rotacao = True
        principal(habilitar_rotacao)