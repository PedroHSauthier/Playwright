from playwright.sync_api import Page, expect
import pytest
from models.cliente import Cliente
from datetime import datetime
from pathlib import Path
import os
import logging
import dotenv
import re

dotenv.load_dotenv()
session_file_limit = int(os.getenv("session_file_limit", "3"))
unique_file_limit = int(os.getenv("unique_file_limit", "3"))
screen_file_limit = int(os.getenv("screen_file_limit", "3"))
log_file_limit = int(os.getenv("log_file_limit", "10"))

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
    - Para execuções de sessão (múltiplos testes), os relatórios são salvos em uma subpasta 'Session'.
    - Para execuções de arquivo único, os relatórios são salvos em uma subpasta com nome dinâmico (ex: 'Consultas').
    - Mantém apenas um número configurável de relatórios recentes em cada subpasta.
    """
    now = datetime.now()
    root_report_dir = Path(__file__).parent.parent / "reports"
    
    parent_dir_name = None
    
    if config.args:
        absolute_paths = [Path(arg).resolve() for arg in config.args]
        if len(absolute_paths) == 1:
            path = absolute_paths[0]
            parent_dir_name = path.parent.name if path.is_file() else path.name
        else:
            common_path = Path(os.path.commonpath(absolute_paths))
            parent_dir_name = common_path.parent.name if common_path.is_file() else common_path.name
    
    if not parent_dir_name:
        parent_dir_name = Path(__file__).parent.parent.name

    date_str = now.strftime('%d-%m-%Y')
    is_single_file_run = len(config.args) == 1 and os.path.isfile(config.args[0])

    if is_single_file_run:
        test_filename_stem = Path(config.args[0]).stem
        dynamic_name = test_filename_stem.split('_')[-1]
        report_dir = root_report_dir / parent_dir_name / date_str / dynamic_name
        report_filename = f"report_{dynamic_name}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.html"
        limit = unique_file_limit
    else:
        report_dir = root_report_dir / parent_dir_name / date_str / "Session"
        report_filename = f"report_session_{now.strftime('%Y-%m-%d_%H-%M-%S')}.html"
        limit = session_file_limit

    report_dir.mkdir(parents=True, exist_ok=True)
    
    # --- Lógica de Rotação de Relatórios ---
    existing_reports = sorted(report_dir.glob('*.html'), key=os.path.getmtime)
    # Garante que o número de relatórios não exceda o limite
    while len(existing_reports) >= limit:
        os.remove(existing_reports.pop(0))

    config.option.htmlpath = report_dir / report_filename
    config.option.self_contained_html = True
    
@pytest.fixture(scope="module", autouse=True)
def log_test_module(request):
    """
    Cria um manipulador de log de arquivo exclusivo para cada módulo de teste.
    O arquivo de log é salvo em uma estrutura de diretórios dinâmica e a quantidade de logs é limitada.
    """
    log_root = logging.getLogger()
    log_file_format = request.config.getini("log_file_format")
    log_file_level = logging.getLevelName(request.config.getini("log_file_level"))

    now = datetime.now()
    test_path = Path(request.node.fspath)
    parent_dir_name = test_path.parent.name
    test_filename_stem = test_path.stem
    
    date_str = now.strftime('%d-%m-%Y')
    dynamic_name = test_filename_stem.split('_')[-1]
    log_name_base = '_'.join(test_filename_stem.split('_')[:-1])
    time_str = now.strftime('%H-%M-%S')

    log_dir = Path(__file__).parent.parent / "logs" / parent_dir_name / date_str / dynamic_name
    log_dir.mkdir(parents=True, exist_ok=True);

    # --- Lógica de Rotação de Logs ---
    existing_logs = sorted(log_dir.glob('*.log'), key=os.path.getmtime)
    while len(existing_logs) >= log_file_limit:
        os.remove(existing_logs.pop(0))

    log_filename = f"log_{log_name_base}_{time_str}.log"
    log_path = log_dir / log_filename

    handler = logging.FileHandler(log_path, mode='w', encoding='utf-8')
    handler.setLevel(log_file_level)
    formatter = logging.Formatter(log_file_format)
    handler.setFormatter(formatter)
    
    log_root.addHandler(handler)

    yield

    log_root.removeHandler(handler)
    handler.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Executado após cada teste para tirar um screenshot de tela inteira em caso de falha.
    O screenshot é salvo em uma estrutura de diretórios dinâmica, incluindo uma subpasta para o componente que falhou,
    e a quantidade de screenshots por componente é limitada.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call' and report.failed:
        try:
            page = item.funcargs['page']
            
            now = datetime.now()
            test_path = Path(item.fspath)
            parent_dir_name = test_path.parent.name
            test_filename_stem = test_path.stem
            dynamic_name = test_filename_stem.split('_')[-1]
            date_str = now.strftime('%d-%m-%Y')
            
            # --- Extrai o componente da mensagem de erro ---
            component = "unknown"
            try:
                long_repr = report.longreprtext
                match = re.search(r"waiting for locator\((.*)\)", long_repr)
                if not match:
                    match = re.search(r"expect\(Locator\(.*?selector='(.*?)'\)\)", long_repr)
                
                if match:
                    component_text = match.group(1).strip("'")
                    component = re.sub(r'[^a-zA-Z0-9_]', '_', component_text).strip('_')
                    component = component[:50]
                else:
                    component = item.name
            except Exception:
                component = item.name

            # --- Cria o diretório do screenshot, incluindo a pasta do componente ---
            screenshot_dir = Path(__file__).parent.parent / "screenshots" / parent_dir_name / date_str / dynamic_name / component
            screenshot_dir.mkdir(parents=True, exist_ok=True)

            # --- Lógica de Rotação de Screenshots ---
            existing_screenshots = sorted(screenshot_dir.glob('*.png'), key=os.path.getmtime)
            while len(existing_screenshots) >= screen_file_limit:
                os.remove(existing_screenshots.pop(0))

            # --- Monta o nome do arquivo e lida com conflitos ---
            base_screenshot_filename = f"screenshot_Failed"
            screenshot_filename = f"{base_screenshot_filename}.png"
            screenshot_path = screenshot_dir / screenshot_filename
            
            counter = 1
            while screenshot_path.exists():
                screenshot_filename = f"{base_screenshot_filename}_{counter}.png"
                screenshot_path = screenshot_dir / screenshot_filename
                counter += 1
            
            page.screenshot(path=str(screenshot_path), full_page=True)
            
        except Exception as e:
            print(f"Erro ao tirar screenshot: {e}")