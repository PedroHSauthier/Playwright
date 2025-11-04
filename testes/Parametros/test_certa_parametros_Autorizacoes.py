from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes

cliente = "homologacao"

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_autorizacoes_vacina(logar_usuario_certa, perfil_cliente):
    """
    """
    
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)

    # Pesquisa por "Parâmetros" no menu do sistema.
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Clica no item de menu "Parâmetros" para abrir a tela de configuração.
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    
    # --- Seção: Autorizações -> Vacina ---
    # Acessa a aba 'Autorizações' e rola até a seção 'Vacina'.
    page.locator("div.dx-list-item:has-text('Autorizações')").click()
    page.get_by_text('Vacina', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Vacina', exact=True)).to_be_visible()
    
    # 1. Modifica o "Modelo Vacina".
    campo_vacina = page.get_by_label("Modelo Vacina", exact=True)
    expect(campo_vacina).to_be_visible()
    campo_vacina.scroll_into_view_if_needed()
    campo_vacina.wait_for(state="visible", timeout=3000)
    campo_vacina.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_vacina = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_vacina).to_be_visible(timeout=5000)
    expect(popup_vacina.get_by_role("textbox")).to_be_visible()
    popup_vacina.get_by_role("textbox").fill("CARTEIRA DE VACINA - A4")
    expect(popup_vacina.get_by_text("CARTEIRA DE VACINA - A4", exact=True)).to_be_visible()
    popup_vacina.get_by_text("CARTEIRA DE VACINA - A4", exact=True).click()
    expect(popup_vacina).to_be_hidden()

    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_autorizacoes_outrosprocedimentos(logar_usuario_certa, perfil_cliente):
    """
    """
    
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)

    # Pesquisa por "Parâmetros" no menu do sistema.
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Clica no item de menu "Parâmetros" para abrir a tela de configuração.
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    
    # --- Seção: Autorizações -> Outros Procedimentos ---
    # Acessa a aba 'Autorizações' e rola até a seção 'Outros Procedimentos'.
    page.locator("div.dx-list-item:has-text('Autorizações')").click()
    page.get_by_text('Outros Procedimentos', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Outros Procedimentos', exact=True)).to_be_visible()
    
    # 1. Modifica o "Modelo outros procedimentos".
    campo_vacina = page.get_by_label("Modelo outros procedimentos", exact=True)
    expect(campo_vacina).to_be_visible()
    campo_vacina.scroll_into_view_if_needed()
    campo_vacina.wait_for(state="visible", timeout=3000)
    campo_vacina.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_vacina = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_vacina).to_be_visible(timeout=5000)
    expect(popup_vacina.get_by_role("textbox")).to_be_visible()
    popup_vacina.get_by_role("textbox").fill("OUTROS PROCEDIMENTOS - A4")
    expect(popup_vacina.get_by_text("OUTROS PROCEDIMENTOS - A4", exact=True)).to_be_visible()
    popup_vacina.get_by_text("OUTROS PROCEDIMENTOS - A4", exact=True).click()
    expect(popup_vacina).to_be_hidden()

    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_autorizacoes_filaencaminhamento(logar_usuario_certa, perfil_cliente):
    """
    """
    
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)

    # Pesquisa por "Parâmetros" no menu do sistema.
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Clica no item de menu "Parâmetros" para abrir a tela de configuração.
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    
    # --- Seção: Autorizações -> Fila Encaminhamento ---
    # Acessa a aba 'Autorizações' e rola até a seção 'Fila Encaminhamento'.
    page.locator("div.dx-list-item:has-text('Autorizações')").click()
    page.get_by_text('Fila Encaminhamento', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Fila Encaminhamento', exact=True)).to_be_visible()
    
    # 1. Modifica o "Modelo fila autorização".
    campo_vacina = page.get_by_label("Modelo fila autorização", exact=True)
    expect(campo_vacina).to_be_visible()
    campo_vacina.scroll_into_view_if_needed()
    campo_vacina.wait_for(state="visible", timeout=3000)
    campo_vacina.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_vacina = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_vacina).to_be_visible(timeout=5000)
    expect(popup_vacina.get_by_role("textbox")).to_be_visible()
    popup_vacina.get_by_role("textbox").fill("FILA AUTORIZAÇÃO")
    expect(popup_vacina.get_by_text("FILA AUTORIZAÇÃO", exact=True)).to_be_visible()
    popup_vacina.get_by_text("FILA AUTORIZAÇÃO", exact=True).click()
    expect(popup_vacina).to_be_hidden()
    
    # 2. Modifica o "Modelo fila encaminhamento".
    campo_vacina = page.get_by_label("Modelo fila encaminhamento", exact=True)
    expect(campo_vacina).to_be_visible()
    campo_vacina.scroll_into_view_if_needed()
    campo_vacina.wait_for(state="visible", timeout=3000)
    campo_vacina.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_vacina = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_vacina).to_be_visible(timeout=5000)
    expect(popup_vacina.get_by_role("textbox")).to_be_visible()
    popup_vacina.get_by_role("textbox").fill("FILA ENCAMINHAMENTO")
    expect(popup_vacina.get_by_text("FILA ENCAMINHAMENTO", exact=True)).to_be_visible()
    popup_vacina.get_by_text("FILA ENCAMINHAMENTO", exact=True).click()
    expect(popup_vacina).to_be_hidden()

    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()