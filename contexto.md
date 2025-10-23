# Contexto do Projeto de Testes com Playwright

## Visão Geral

Este projeto é um ambiente de aprendizado para testes automatizados de uma aplicação web de gestão de saúde. O objetivo é aplicar as melhores práticas de mercado para garantir a qualidade e a robustez do sistema.

## Estrutura do Projeto

- **`html/`**: Contém os arquivos HTML completos das páginas da aplicação web que estão sendo testadas. Isso nos permite simular o front-end da aplicação de forma local e controlada.
- **`testes/`**: É o coração do projeto de testes. Aqui ficam todos os nossos scripts de teste, escritos em Python com o framework `pytest`.
  - **`conftest.py`**: Arquivo de configuração do `pytest`, onde definimos fixtures, hooks e outros elementos de suporte para os testes.
  - **`test_*.py`**: Os arquivos de teste propriamente ditos, onde cada um é responsável por testar uma funcionalidade ou um conjunto de funcionalidades específicas.
- **`screenshots/`**: Diretório utilizado para salvar capturas de tela durante a execução dos testes. É uma ferramenta visual poderosa para depurar falhas e analisar o comportamento da aplicação em diferentes cenários.
- **`playVenv/`**: Ambiente virtual do Python que isola as dependências do projeto, garantindo que o ambiente de desenvolvimento e de execução dos testes seja consistente.
- **`.env.example`**: Arquivo de exemplo para as variáveis de ambiente. Informações sensíveis, como senhas e tokens de acesso, devem ser armazenadas em um arquivo `.env` (não versionado) e carregadas nos testes.
- **`requirements.txt`**: Arquivo que lista todas as dependências do projeto, permitindo a fácil recriação do ambiente de desenvolvimento.
- **`contexto.md`**: Este arquivo. Serve como um guia de referência rápida para qualquer pessoa que venha a trabalhar no projeto, incluindo eu, para que eu possa me lembrar do contexto em sessões futuras.

## Ferramentas e Tecnologias

- **Linguagem**: Python
- **Framework de Teste**: `pytest`
- **Automação de Browser**: `Playwright`
- **Gerenciamento de Dependências**: `pip` e `virtualenv`

## Como Começar

1.  **Instalar as dependências**: `pip install -r requirements.txt`.
2.  **Executar os testes**: `pytest`