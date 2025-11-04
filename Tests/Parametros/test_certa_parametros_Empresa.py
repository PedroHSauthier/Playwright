from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes

cliente = "homologacao"

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_empresa(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção 'Alvaras' da aba 'Empresa'.

    Este teste executa as seguintes ações:
    1. Realiza o login no sistema utilizando o perfil de cliente fornecido.
    2. Navega até a tela de 'Parâmetros' do sistema.
    3. Acessa a aba 'Empresa' e, em seguida, a seção 'Alvaras'.
    4. Modifica os modelos de alvará para 'Alvara 1', 'Alvara 2' e 'Alvara 3'.
    5. Tira um screenshot da tela de parâmetros da empresa.
    6. Salva as alterações e verifica se a mensagem de sucesso é exibida.

    Args:
        logar_usuario_certa (fixture): Fixture para realizar o login do usuário no sistema.
        perfil_cliente (str): O nome do perfil do cliente a ser testado.
    """
    
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)

    # Pesquisa por "Parâmetros" no menu do sistema para acessar a tela de configuração.
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Clica no item de menu "Parâmetros" para abrir a tela de configuração.
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    
    # --- Seção: Empresa -> Alvaras ---
    # Acessa a aba 'Empresa' e rola até a seção 'Alvaras'.
    page.locator("div.dx-list-item:has-text('Empresa')").click()
    page.get_by_text('Alvaras', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Alvaras', exact=True)).to_be_visible()
    
    # 1. Modifica o "Alvara 1".
    campo_alvara1 = page.get_by_label("Alvara 1", exact=True)
    expect(campo_alvara1).to_be_visible()
    campo_alvara1.scroll_into_view_if_needed()
    campo_alvara1.wait_for(state="visible", timeout=3000)
    campo_alvara1.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_alvara1 = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_alvara1).to_be_visible(timeout=5000)
    expect(popup_alvara1.get_by_role("textbox")).to_be_visible()
    popup_alvara1.get_by_role("textbox").fill("ALVARÁ SANITÁRIO - MODELO 1 - A4")
    expect(popup_alvara1.get_by_text("ALVARÁ SANITÁRIO - MODELO 1 - A4", exact=True)).to_be_visible()
    popup_alvara1.get_by_text("ALVARÁ SANITÁRIO - MODELO 1 - A4", exact=True).click()
    expect(popup_alvara1).to_be_hidden()
    
    # 2. Modifica o "Alvara 2".
    campo_alvara2 = page.get_by_label("Alvara 2", exact=True)
    expect(campo_alvara2).to_be_visible()
    campo_alvara2.scroll_into_view_if_needed()
    campo_alvara2.wait_for(state="visible", timeout=3000)
    campo_alvara2.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_alvara2 = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_alvara2).to_be_visible(timeout=5000)
    expect(popup_alvara2.get_by_role("textbox")).to_be_visible()
    popup_alvara2.get_by_role("textbox").fill("ALVARÁ SANITÁRIO - MODELO 2 - A4")
    expect(popup_alvara2.get_by_text("ALVARÁ SANITÁRIO - MODELO 2 - A4", exact=True)).to_be_visible()
    popup_alvara2.get_by_text("ALVARÁ SANITÁRIO - MODELO 2 - A4", exact=True).click()
    expect(popup_alvara2).to_be_hidden()
    
    # 3. Modifica o "Alvara 3".
    campo_alvara3 = page.get_by_label("Alvara 3", exact=True)
    expect(campo_alvara3).to_be_visible()
    campo_alvara3.scroll_into_view_if_needed()
    campo_alvara3.wait_for(state="visible", timeout=3000)
    campo_alvara3.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_alvara3 = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_alvara3).to_be_visible(timeout=5000)
    expect(popup_alvara3.get_by_role("textbox")).to_be_visible()
    popup_alvara3.get_by_role("textbox").fill("ALVARÁ SANITÁRIO - MODELO 3 - A4")
    expect(popup_alvara3.get_by_text("ALVARÁ SANITÁRIO - MODELO 3 - A4", exact=True)).to_be_visible()
    popup_alvara3.get_by_text("ALVARÁ SANITÁRIO - MODELO 3 - A4", exact=True).click()
    expect(popup_alvara3).to_be_hidden()
    
    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()