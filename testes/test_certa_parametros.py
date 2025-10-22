from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv

load_dotenv()
cpf = os.getenv("cliente_cpf")
senha = os.getenv("cliente_senha")
unidade = os.getenv("cliente_unidade")
url = os.getenv("cliente_url")

def test_baixar_relatorios(logar_usuario_certa):
    """Realiza a atualização de todos os relatórios considerados de importância no sistema, baixando eles da loja.

    Args:
        logar_usuario (_type_): _description_
    """
    
    pl = logar_usuario_certa(cpf, senha, unidade, url)
    
    # pesquisar loja na tela inicial
    menu = pl.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("loja", delay=2)
    
    # abrir loja
    item_loja = pl.get_by_text("Loja de Relatorios", exact=True)
    expect(item_loja).to_be_visible()
    item_loja.click()
    
    
    
    pl.screenshot(path="screenshots/certa/relatorios_baixar.png")
    