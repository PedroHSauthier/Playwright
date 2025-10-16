from playwright.sync_api import Page, expect
import pytest

def pagina_inicial(page: Page):
    page.goto("https://homologacao.certasistemas.com.br/")
    
    expect(page.locator('#app')).to_be_visible()
    
    yield page
    
pagina_inicial("https://homologacao.certasistemas.com.br/")
    
def test_login_1(pagina_inicial: Page):
    """
    Deve conseguir preencher o CPF e a Senha e apertar em login, chegando na próxima tela.
    """
    
    pagina_inicial.get_by_label("span:has_text='CPF - Usuário'").fill("12345678909")
    
    pagina_inicial.screenshot(path="screenshot/certa/login_cpf1.png")