from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes("homologacao"))
def test_modificar_parametros_cadastro(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção de Cadastro Individual.
    Este teste navega até a página de parâmetros, seleciona opções para os modelos
    de domicílio e grupo, e verifica se as interações ocorrem como esperado.
    """
    
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    # A fixture de login recebe o objeto cliente.
    page = logar_usuario_certa(cliente_teste)

    # Pesquisar "Parâmetros" na tela inicial para encontrar a page Parâmetros
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Abrir a Tela de Parâmetros
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    
    # --- Seção: Cadastros -> Individual ---
    expect(page.get_by_text("Individual")).to_be_visible()

    # 1. Modificar "Modelo de Domicilio Individual"
    page.get_by_label("Modelo de Domicilio Individual").click()
    popup_domicilio = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_domicilio).to_be_visible()
    popup_domicilio.get_by_text("FICHA CADASTRO INDIVIDUAL - A4").click()
    expect(popup_domicilio).to_be_hidden()

    # 2. Modificar "Modelo cadastro Grupo"
    page.get_by_label("Modelo cadastro Grupo").click()
    popup_grupo = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_grupo).to_be_visible()
    popup_grupo.get_by_text("RELATÓRIO - CADASTRO INDIVIDUAL RESUMIDO", exact=True).click()
    expect(popup_grupo).to_be_hidden()
    
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()