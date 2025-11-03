from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes("homologacao"))
def test_modificar_parametros_consulta_comprovanteagendamento(logar_usuario_certa, perfil_cliente):
    """"""
    
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
    
    # --- Seção: Roteiro -> Roteiro Veículo ---
    page.locator("div.dx-list-item:has-text('Roteiros de Veículos')").click()
    page.get_by_text('Roteiro Veículo', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Roteiro Veículo', exact=True)).to_be_visible()
    
    # 1. Modificar "Modelo de roteiro veículo"
    campo_modelo_receita = page.get_by_label("Modelo de roteiro veículo", exact=True)
    expect(campo_modelo_receita).to_be_visible()
    campo_modelo_receita.scroll_into_view_if_needed()
    campo_modelo_receita.wait_for(state="visible", timeout=3000)
    campo_modelo_receita.click()

    # Aguardar o popup aparecer explicitamente
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao).to_be_visible(timeout=5000)
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("ROTEIRO DE VEÍCULO - A4 - CURITIBANOS")
    expect(popup_avaliacao.get_by_text("ROTEIRO DE VEÍCULO - A4 - CURITIBANOS", exact=True)).to_be_visible()
    popup_avaliacao.get_by_text("ROTEIRO DE VEÍCULO - A4 - CURITIBANOS", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    # 2. Modificar "Modelo de Comprovante"
    campo_modelo_receita = page.get_by_label("Modelo de Comprovante", exact=True)
    expect(campo_modelo_receita).to_be_visible()
    campo_modelo_receita.scroll_into_view_if_needed()
    campo_modelo_receita.wait_for(state="visible", timeout=3000)
    campo_modelo_receita.click()

    # Aguardar o popup aparecer explicitamente
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao).to_be_visible(timeout=5000)
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("ROTEIRO DE VEÍCULOS COMPROVANTE - A4")
    expect(popup_avaliacao.get_by_text("ROTEIRO DE VEÍCULOS COMPROVANTE - A4", exact=True)).to_be_visible()
    popup_avaliacao.get_by_text("ROTEIRO DE VEÍCULOS COMPROVANTE - A4", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    # 3. Modificar "Modelo de Assinatura"
    campo_modelo_receita = page.get_by_label("Modelo de Assinatura", exact=True)
    expect(campo_modelo_receita).to_be_visible()
    campo_modelo_receita.scroll_into_view_if_needed()
    campo_modelo_receita.wait_for(state="visible", timeout=3000)
    campo_modelo_receita.click()

    # Aguardar o popup aparecer explicitamente
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao).to_be_visible(timeout=5000)
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("ROTEIRO DE VEÍCULOS ASSINATURA- A4")
    expect(popup_avaliacao.get_by_text("ROTEIRO DE VEÍCULOS ASSINATURA- A4", exact=True)).to_be_visible()
    popup_avaliacao.get_by_text("ROTEIRO DE VEÍCULOS ASSINATURA- A4", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()