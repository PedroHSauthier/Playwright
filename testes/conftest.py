from playwright.sync_api import Page, expect
import pytest

@pytest.fixture
def pagina_inicial(page: Page):
    page.goto("https://homologacao.certasistemas.com.br/")
    
    expect(page.locator('#app')).to_be_visible()
    
    yield page
    
@pytest.fixture
def logar_usuario(page: Page):
    
    def logar(cpf: str, senha: str):
        page.goto("https://homologacao.certasistemas.com.br/")
        expect(page.locator('#app')).to_be_visible()
        
        page.get_by_label("CPF - Usuário").fill(cpf)
        page.get_by_label("Senha").fill(senha)
        
        cpf_container = page.locator("div.dx-texteditor:has-text('CPF - Usuário')")
        cpf_container.locator(".dx-icon-clear").click()

        senha_container = page.locator("div.dx-texteditor:has-text('Senha')")
        senha_container.locator(".dx-icon-clear").click()
        
        page.get_by_label("CPF - Usuário").fill(cpf)
        page.get_by_label("Senha").fill(senha)
        
        page.get_by_role("button", name="Login").click()
        
        expect(page.get_by_role("option")).to_be_visible()
        page.get_by_role("option").first.click()
        
        expect(page.get_by_text("Novidades da versão")).to_be_visible()
        
        return page
    
    yield logar