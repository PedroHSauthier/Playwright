from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes

cliente = "homologacao"

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_medicamentos(logar_usuario_certa, perfil_cliente):
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
    
    # --- Seção: Medicamentos -> Medicamentos ---
    # Acessa a aba 'Medicamentos' e rola até a seção 'Medicamentos'.
    page.locator("div.dx-list-item:has-text('Medicamentos')").click()
    page.get_by_text('Modelo de etiqueta', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Modelo de etiqueta', exact=True)).to_be_visible()
    
    # 1. Modifica o "Modelo de etiqueta".
    campo_etiqueta = page.get_by_label("Modelo de etiqueta", exact=True)
    expect(campo_etiqueta).to_be_visible()
    campo_etiqueta.scroll_into_view_if_needed()
    campo_etiqueta.wait_for(state="visible", timeout=3000)
    campo_etiqueta.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_etiqueta = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_etiqueta).to_be_visible(timeout=5000)
    expect(popup_etiqueta.get_by_role("textbox")).to_be_visible()
    popup_etiqueta.get_by_role("textbox").fill("ETIQUETA EAN13")
    expect(popup_etiqueta.get_by_text("ETIQUETA EAN13", exact=True)).to_be_visible()
    popup_etiqueta.get_by_text("ETIQUETA EAN13", exact=True).click()
    expect(popup_etiqueta).to_be_hidden()
    
    # 2. Modifica o "Modelo Reimpressão de etiqueta".
    campo_etiqueta_reim = page.get_by_label("Modelo Reimpressão de etiqueta", exact=True)
    expect(campo_etiqueta_reim).to_be_visible()
    campo_etiqueta_reim.scroll_into_view_if_needed()
    campo_etiqueta_reim.wait_for(state="visible", timeout=3000)
    campo_etiqueta_reim.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_etiqueta_reim = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_etiqueta_reim).to_be_visible(timeout=5000)
    expect(popup_etiqueta_reim.get_by_role("textbox")).to_be_visible()
    popup_etiqueta_reim.get_by_role("textbox").fill("ETIQUETA EAN13 - REIMPRESSÃO")
    expect(popup_etiqueta_reim.get_by_text("ETIQUETA EAN13 - REIMPRESSÃO", exact=True)).to_be_visible()
    popup_etiqueta_reim.get_by_text("ETIQUETA EAN13 - REIMPRESSÃO", exact=True).click()
    expect(popup_etiqueta_reim).to_be_hidden()
    
    # 3. Modifica o "Modelo de posologia".
    campo_posologia = page.get_by_label("Modelo de posologia", exact=True)
    expect(campo_posologia).to_be_visible()
    campo_posologia.scroll_into_view_if_needed()
    campo_posologia.wait_for(state="visible", timeout=3000)
    campo_posologia.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_posologia = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_posologia).to_be_visible(timeout=5000)
    expect(popup_posologia.get_by_role("textbox")).to_be_visible()
    popup_posologia.get_by_role("textbox").fill("POSOLOGIA")
    expect(popup_posologia.get_by_text("POSOLOGIA", exact=True)).to_be_visible()
    popup_posologia.get_by_text("POSOLOGIA", exact=True).click()
    expect(popup_posologia).to_be_hidden()
    
    # 4. Modifica o "Modelo comprovante de transferência".
    campo_comp_transferencia = page.get_by_label("Modelo comprovante de transferência", exact=True)
    expect(campo_comp_transferencia).to_be_visible()
    campo_comp_transferencia.scroll_into_view_if_needed()
    campo_comp_transferencia.wait_for(state="visible", timeout=3000)
    campo_comp_transferencia.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_comp_transferencia = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_comp_transferencia).to_be_visible(timeout=5000)
    expect(popup_comp_transferencia.get_by_role("textbox")).to_be_visible()
    popup_comp_transferencia.get_by_role("textbox").fill("COMPROVANTE TRANSFERENCIA - A4")
    expect(popup_comp_transferencia.get_by_text("COMPROVANTE TRANSFERENCIA - A4", exact=True)).to_be_visible()
    popup_comp_transferencia.get_by_text("COMPROVANTE TRANSFERENCIA - A4", exact=True).click()
    expect(popup_comp_transferencia).to_be_hidden()
    
    # 5. Modifica o "Modelo comprovante de dispensação".
    campo_comp_dispensacao = page.get_by_label("Modelo comprovante de dispensação", exact=True)
    expect(campo_comp_dispensacao).to_be_visible()
    campo_comp_dispensacao.scroll_into_view_if_needed()
    campo_comp_dispensacao.wait_for(state="visible", timeout=3000)
    campo_comp_dispensacao.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_comp_dispensacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_comp_dispensacao).to_be_visible(timeout=5000)
    expect(popup_comp_dispensacao.get_by_role("textbox")).to_be_visible()
    popup_comp_dispensacao.get_by_role("textbox").fill("COMPROVANTE DISPENSAÇÃO - A4")
    expect(popup_comp_dispensacao.get_by_text("COMPROVANTE DISPENSAÇÃO - A4", exact=True)).to_be_visible()
    popup_comp_dispensacao.get_by_text("COMPROVANTE DISPENSAÇÃO - A4", exact=True).click()
    expect(popup_comp_dispensacao).to_be_hidden()
    
    # 6. Modifica o "Modelo comprovante de saída".
    campo_comp_saida = page.get_by_label("Modelo comprovante de saída", exact=True)
    expect(campo_comp_saida).to_be_visible()
    campo_comp_saida.scroll_into_view_if_needed()
    campo_comp_saida.wait_for(state="visible", timeout=3000)
    campo_comp_saida.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_comp_saida = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_comp_saida).to_be_visible(timeout=5000)
    expect(popup_comp_saida.get_by_role("textbox")).to_be_visible()
    popup_comp_saida.get_by_role("textbox").fill("COMPROVANTE OUTRAS SAÍDAS - A4")
    expect(popup_comp_saida.get_by_text("COMPROVANTE OUTRAS SAÍDAS - A4", exact=True)).to_be_visible()
    popup_comp_saida.get_by_text("COMPROVANTE OUTRAS SAÍDAS - A4", exact=True).click()
    expect(popup_comp_saida).to_be_hidden()
    
    # 7. Modifica o "Modelo comprovante de saída".
    campo_comp_saida = page.get_by_label("Modelo comprovante de saída", exact=True)
    expect(campo_comp_saida).to_be_visible()
    campo_comp_saida.scroll_into_view_if_needed()
    campo_comp_saida.wait_for(state="visible", timeout=3000)
    campo_comp_saida.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_comp_saida = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_comp_saida).to_be_visible(timeout=5000)
    expect(popup_comp_saida.get_by_role("textbox")).to_be_visible()
    popup_comp_saida.get_by_role("textbox").fill("COMPROVANTE OUTRAS SAÍDAS - A4")
    expect(popup_comp_saida.get_by_text("COMPROVANTE OUTRAS SAÍDAS - A4", exact=True)).to_be_visible()
    popup_comp_saida.get_by_text("COMPROVANTE OUTRAS SAÍDAS - A4", exact=True).click()
    expect(popup_comp_saida).to_be_hidden()
    
    # 8. Modifica o "Modelo comprovante de entrada".
    campo_comp_entrada = page.get_by_label("Modelo comprovante de entrada", exact=True)
    expect(campo_comp_entrada).to_be_visible()
    campo_comp_entrada.scroll_into_view_if_needed()
    campo_comp_entrada.wait_for(state="visible", timeout=3000)
    campo_comp_entrada.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_comp_entrada = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_comp_entrada).to_be_visible(timeout=5000)
    expect(popup_comp_entrada.get_by_role("textbox")).to_be_visible()
    popup_comp_entrada.get_by_role("textbox").fill("COMPROVANTE DISPENSAÇÃO - A4")
    expect(popup_comp_entrada.get_by_text("COMPROVANTE DISPENSAÇÃO - A4", exact=True)).to_be_visible()
    popup_comp_entrada.get_by_text("COMPROVANTE DISPENSAÇÃO - A4", exact=True).click()
    expect(popup_comp_entrada).to_be_hidden()
    
    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()