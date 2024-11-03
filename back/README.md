# Projeto: gp-armarios-ifce

Este projeto implementa uma solução para gerenciar o sistema de armários do IFCE Campus Maracanaú. Ele inclui um backend desenvolvido com Flask e está estruturado para facilitar o processo de desenvolvimento, configuração e execução.

## Estrutura do Projeto

- **back**: Diretório que contém o código do backend com Flask.
- **front**: Diretório que contém o código do frontend com Next.JS.

---

## Como Rodar o Projeto

Siga os passos abaixo para executar o backend do projeto:

### Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes softwares instalados:

- **Python**: Versão 3.x
- **pip**: O gerenciador de pacotes Python
- **Virtualenv**: (Opcional, mas recomendado) para gerenciar dependências do projeto em um ambiente isolado.

---

### Passos para Configurar e Executar o Backend

## Clone o Repositório

  Se ainda não fez isso, clone o repositório em sua máquina:

  ```bash
  git clone https://github.com/myller-silva/gp-armarios-ifce.git
  cd gp-armarios-ifce/back
  ```

## Criar e Ativar o Ambiente Virtual

É recomendado usar um ambiente virtual para evitar conflitos de dependências:

  ```bash
  python -m venv venv
  ```

Para ativar o ambiente virtual:

1. **Linux/macOS**:

    ```bash
    source venv/bin/activate
    ```

2. **Windows**

    ```bash
    venv\Scripts\activate
    ```

## Instalar dependencias

  ```bash
  pip install -r requirements.txt
  ```

## Executar o projeto

Inicie o servidor Flask:

   ```bash
    flask run
   ```

## Observações Adicionais

### Configurações CORS

O projeto utiliza Flask-CORS para permitir acessos de diferentes origens. Se precisar modificar as políticas de CORS, ajuste na configuração do Flask.

### Autenticação

A API usa flask_jwt_extended para geração e verificação de tokens JWT. Você pode configurar a segurança no arquivo [config.py](config.py).
