from playwright.sync_api import Page, expect
import pytest
from models.cliente import Cliente
from datetime import datetime
from pathlib import Path
import os
import logging


@pytest.fixture
def pagina_inicial(page: Page):
    page.goto("https://homologacao.certasistemas.com.br/")
    
    expect(page.locator('#app')).to_be_visible()
    
    yield page
    
@pytest.fixture
def logar_usuario_certa(page: Page):
    
    def logar(cliente: Cliente):
        page.goto(cliente.url)
        expect(page.locator('#app')).to_be_visible()
        
        page.reload()
        #Preenche o CPF e a Senha
        page.get_by_label("CPF - Usuário").fill(cliente.cpf)
        page.get_by_label("Senha").fill(cliente.senha)
        
        #Limpa o campo do usuário, pora que o dicionário possa identificar os dados.
        cpf_container = page.locator("div.dx-texteditor:has-text('CPF - Usuário')")
        cpf_container.locator(".dx-icon-clear").click()
        
        #Preenche de forma final o CPF 
        expect(page.get_by_label("CPF - Usuário")).to_be_empty()
        page.get_by_label("CPF - Usuário").fill(cliente.cpf)

        #Limpa o campo do usuário, pora que o dicionário possa identificar os dados.
        senha_container = page.locator("div.dx-texteditor:has-text('Senha')")
        senha_container.locator(".dx-icon-clear").click()
        
        #Preenche de forma final a senha
        expect(page.get_by_label("Senha")).to_be_empty()
        page.get_by_label("Senha").fill(cliente.senha)
        
        #Aciona o login
        page.get_by_role("button", name="Login").click()
        
        #Seleciona a primeira unidade cadastrada no perfil do usuário.
        expect(page.get_by_role("listbox")).to_be_enabled()
        if(cliente.unidade == ""):
            page.get_by_role("option").first.click()    
        else:
            page.get_by_label("Pesquisar").fill(cliente.unidade)
            page.get_by_text(cliente.unidade).click()
        
        #Verifica se ocorreu realmente o login e o acesso a unidade.
        expect(page.get_by_text("Novidades da versão")).to_be_visible()
        
        return page
    
    yield logar

def pytest_configure(config):
    """
    Cria um nome de arquivo de relatório HTML dinâmico com base no contexto de execução.
    - Se múltiplos arquivos ou diretórios são testados, o relatório é salvo em um
      subdiretório com o nome do diretório pai comum.
    - Se um único arquivo é testado, o subdiretório é o do diretório pai do arquivo.
    - Como fallback (nenhum argumento), usa o nome do diretório raiz do projeto.
    - Os relatórios são organizados em pastas por data (dd-mm-yyyy).
    - Mantém apenas os 3 relatórios mais recentes em cada pasta de data.
    """
    now = datetime.now()
    root_report_dir = Path(__file__).parent.parent / "reports"
    
    parent_dir_name = None
    
    # Determina o nome do diretório pai com base nos argumentos do pytest
    if config.args:
        # Converte todos os argumentos para caminhos absolutos
        absolute_paths = [Path(arg).resolve() for arg in config.args]
        
        if len(absolute_paths) == 1:
            # Se for um único argumento, usa o nome do diretório pai se for arquivo, ou o próprio nome se for diretório
            path = absolute_paths[0]
            if path.is_file():
                parent_dir_name = path.parent.name
            else:
                parent_dir_name = path.name
        else:
            # Se forem múltiplos argumentos, encontra o caminho comum
            common_path = Path(os.path.commonpath(absolute_paths))
            # Verifica se o caminho comum é um diretório de fato. Se for um arquivo, pega o pai.
            if common_path.is_file():
                parent_dir_name = common_path.parent.name
            else:
                parent_dir_name = common_path.name
    
    # Fallback: se nenhum argumento for passado, usa o nome do diretório raiz do projeto
    if not parent_dir_name:
        parent_dir_name = Path(__file__).parent.parent.name

    # Cria o diretório do relatório com a data
    date_str = now.strftime('%d-%m-%Y')
    report_dir = root_report_dir / parent_dir_name / date_str
    report_dir.mkdir(parents=True, exist_ok=True)

    # --- Lógica de Rotação de Relatórios ---
    # Lista os relatórios existentes e os ordena por data de modificação (do mais antigo para o mais novo)
    existing_reports = sorted(report_dir.glob('*.html'), key=os.path.getmtime)
    
    # Se já existirem 3 ou mais relatórios, remove o mais antigo
    if len(existing_reports) >= 3:
        os.remove(existing_reports[0])

    # Define o nome do arquivo de relatório
    if len(config.args) == 1 and os.path.isfile(config.args[0]):
        test_filename = Path(config.args[0]).stem
        last_part = test_filename.split('_')[-1]
        report_filename = f"report_{last_part}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.html"
    else:
        report_filename = f"report_session_{now.strftime('%Y-%m-%d_%H-%M-%S')}.html"

    # Define o caminho completo do relatório nas opções do pytest
    config.option.htmlpath = report_dir / report_filename
    config.option.self_contained_html = True
    
@pytest.fixture(scope="module", autouse=True)
def log_test_module(request):
    """
    Cria um manipulador de log de arquivo exclusivo para cada módulo de teste.
    O arquivo de log é nomeado dinamicamente com base no nome do arquivo de teste e em um timestamp,
    e é colocado em um subdiretório correspondente dentro da pasta 'logs'.
    Ex: logs/Parametros/log_09_TFD_2025-11-04_10-30-00.log
    """
    # Pega o logger raiz do pytest
    log_root = logging.getLogger()
    
    # Pega as configurações do pytest.ini
    log_file_format = request.config.getini("log_file_format")
    log_file_level_str = request.config.getini("log_file_level")
    log_file_level = logging.getLevelName(log_file_level_str)
    
    # --- Cria o caminho dinâmico para o log ---
    test_path = Path(request.node.fspath)
    
    # Extrai o nome do diretório pai e o nome do arquivo de teste
    parent_dir_name = test_path.parent.name
    test_filename_stem = test_path.stem # ex: test_09_certa_parametros_TFD
    
    # Monta o nome do arquivo de log (sem timestamp)
    log_filename = f"log_{test_filename_stem}.log"
    
    # Define o diretório de log
    log_dir = Path(__file__).parent.parent / "logs" / parent_dir_name
    log_dir.mkdir(parents=True, exist_ok=True)
    
    log_path = log_dir / log_filename

    # --- Configura e adiciona o handler ---
    handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    handler.setLevel(log_file_level)
    formatter = logging.Formatter(log_file_format)
    handler.setFormatter(formatter)
    
    log_root.addHandler(handler)
    
    # --- Executa os testes do módulo ---
    yield
    
    # --- Teardown: Remove e fecha o handler ---
    log_root.removeHandler(handler)
    handler.close()
