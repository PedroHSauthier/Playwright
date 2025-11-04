from playwright.sync_api import Page, expect
import pytest
from models.cliente import Cliente
from datetime import datetime
from pathlib import Path
import os

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
    Cria um nome de arquivo de relatório HTML dinâmico.
    Se um único arquivo de teste for executado, o relatório é salvo em um
    subdiretório correspondente com um nome baseado no arquivo de teste.
    Caso contrário, um relatório genérico com timestamp é criado no diretório 'reports'.
    """
    now = datetime.now()
    root_report_dir = Path(__file__).parent.parent / "reports"
    
    # Verifica se um único arquivo de teste está sendo executado
    if len(config.args) == 1 and os.path.isfile(config.args[0]):
        test_path = Path(config.args[0])
        
        # Diretório pai do teste
        parent_dir_name = test_path.parent.name
        
        # Subdiretório de relatórios
        report_dir = root_report_dir / parent_dir_name
        
        # Última parte do nome do arquivo de teste
        test_filename = test_path.stem
        last_part = test_filename.split('_')[-1]
        
        report_filename = f"report_{last_part}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.html"
        
    else:
        # Fallback para múltiplos testes ou execução de diretório
        report_dir = root_report_dir
        report_filename = f"report_session_{now.strftime('%Y-%m-%d_%H-%M-%S')}.html"

    report_dir.mkdir(parents=True, exist_ok=True)
    config.option.htmlpath = report_dir / report_filename
    config.option.self_contained_html = True
