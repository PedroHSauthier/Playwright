from playwright.sync_api import Page, expect

def test_login_with_fixture(pagina_inicial: Page):
    """A função testa a fixture pagina_inicial para realizar um login bem-sucedido.

    Args:
        pagina_inicial (Page): definido a fixture pagina_inicial ao parâmetro Page.
    """
    
    pagina_inicial.get_by_label("CPF - Usuário").fill("12345678909")
    pagina_inicial.get_by_label("Senha").fill("cert@0601")
    
    cpf_container = pagina_inicial.locator("div.dx-texteditor:has-text('CPF - Usuário')")
    cpf_container.locator(".dx-icon-clear").click()

    senha_container = pagina_inicial.locator("div.dx-texteditor:has-text('Senha')")
    senha_container.locator(".dx-icon-clear").click()
    
    pagina_inicial.get_by_label("CPF - Usuário").fill("12345678909")
    pagina_inicial.get_by_label("Senha").fill("cert@0601")
    
    pagina_inicial.get_by_role("button", name="Login").click()
    
    expect(pagina_inicial.locator(".dx-scrollable")).to_be_visible()
    pagina_inicial.locator(".dx-scrollable").first.click()
    
    pagina_inicial.screenshot(path="screenshots/certa/login_cpf2.png")
    
def test_logado_with_fixture(logar_usuario):
    """Teste da fixture logar_usuario.

    Args:
        pagina_logada (Page): definido a fixture logar_usuario ao parâmetro Page.
    """
    page = logar_usuario("17961631984", "123")
    
    page.screenshot(path="screenshots/certa/login_cpf3.png")