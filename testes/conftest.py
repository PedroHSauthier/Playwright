from playwright.sync_api import Page, expect
import pytest

@pytest.fixture
def pagina_inicial(page: Page):
    page.goto("https://homologacao.certasistemas.com.br/")
    
    expect(page.locator('#app')).to_be_visible()
    
    yield page
    
@pytest.fixture
def logar_usuario_certa(page: Page):
    
    def logar(cpf: str, senha: str, unidade: str, url: str):
        page.goto(url)
        expect(page.locator('#app')).to_be_visible()
        
        page.reload()
        #Preenche o CPF e a Senha
        page.get_by_label("CPF - Usuário").fill(cpf)
        page.get_by_label("Senha").fill(senha)
        
        #Limpa o campo do usuário, pora que o dicionário possa identificar os dados.
        cpf_container = page.locator("div.dx-texteditor:has-text('CPF - Usuário')")
        cpf_container.locator(".dx-icon-clear").click()
        
        #Preenche de forma final o CPF 
        expect(page.get_by_label("CPF - Usuário")).to_be_empty()
        page.get_by_label("CPF - Usuário").fill(cpf)

        #Limpa o campo do usuário, pora que o dicionário possa identificar os dados.
        senha_container = page.locator("div.dx-texteditor:has-text('Senha')")
        senha_container.locator(".dx-icon-clear").click()
        
        #Preenche de forma final a senha
        expect(page.get_by_label("Senha")).to_be_empty()
        page.get_by_label("Senha").fill(senha)
        
        #Aciona o login
        page.get_by_role("button", name="Login").click()
        
        #Seleciona a primeira unidade cadastrada no perfil do usuário.
        expect(page.get_by_role("listbox")).to_be_visible()
        if(unidade == ""):
            page.get_by_role("option").first.click()    
        else:
            page.get_by_text(unidade).click()
        
        #Verifica se ocorreu realmente o login e o acesso a unidade.
        expect(page.get_by_text("Novidades da versão")).to_be_visible()
        
        return page
    
    yield logar