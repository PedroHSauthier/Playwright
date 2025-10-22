from playwright.sync_api import Page, expect
from dotenv import load_dotenv
import os

load_dotenv()
cliente = os.getenv("cliente_cpf")
senha = os.getenv("cliente_senha")
unidade = os.getenv("cliente_unidade")
url = os.getenv("cliente_url")

def inativo_test_login_with_fixture(pagina_inicial: Page):
    """A função testa a fixture pagina_inicial para realizar um login bem-sucedido.

    Args:
        pagina_inicial (Page): definido a fixture pagina_inicial ao parâmetro Page.
    """
    
    pagina_inicial.get_by_label("CPF - Usuário").fill(cliente)
    pagina_inicial.get_by_label("Senha").fill(senha)
    
    cpf_container = pagina_inicial.locator("div.dx-texteditor:has-text('CPF - Usuário')")
    cpf_container.locator(".dx-icon-clear").click()

    senha_container = pagina_inicial.locator("div.dx-texteditor:has-text('Senha')")
    senha_container.locator(".dx-icon-clear").click()
    
    pagina_inicial.get_by_label("CPF - Usuário").fill(cliente)
    pagina_inicial.get_by_label("Senha").fill(senha)
    
    pagina_inicial.get_by_role("button", name="Login").click()
    
    expect(pagina_inicial.locator(".dx-scrollable")).to_be_visible()
    pagina_inicial.locator(".dx-scrollable").first.click()
    
    pagina_inicial.screenshot(path="screenshots/certa/login_cpf2.png")
    
def test_logado_with_fixture(logar_usuario_certa):
    """Teste da fixture logar_usuario.

    Args:
        pagina_logada (Page): definido a fixture logar_usuario ao parâmetro Page.
    """
    page = logar_usuario_certa(cliente, senha, unidade, url)
    
    page.screenshot(path="screenshots/certa/login_cpf3.png")