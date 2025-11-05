from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes
import logging

log = logging.getLogger(__name__)

cliente = "homologacao"

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_roteiro(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção 'Roteiro Veículo' da aba 'Roteiros de Veículos'.

    Este teste executa as seguintes ações:
    1. Realiza o login no sistema utilizando o perfil de cliente fornecido.
    2. Navega até a tela de 'Parâmetros' do sistema.
    3. Acessa a aba 'Roteiros de Veículos' e, em seguida, a seção 'Roteiro Veículo'.
    4. Modifica os modelos para 'Modelo de roteiro veículo', 'Modelo de Comprovante' e 'Modelo de Assinatura'.
    5. Salva as alterações e verifica se a mensagem de sucesso é exibida.

    Args:
        logar_usuario_certa (fixture): Fixture para realizar o login do usuário no sistema.
        perfil_cliente (str): O nome do perfil do cliente a ser testado.
    """
    
    log.info(f"Iniciando teste de parâmetros de Roteiro para o perfil: {perfil_cliente}")
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Usuário {cliente_teste.cpf} logado.")

    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    log.info("Navegou para a página Parâmetros")
    
    # --- Seção: Roteiro -> Roteiro Veículo ---
    page.locator("div.dx-list-item:has-text('Roteiros de Veículos')").click()
    log.info("Acessou a aba 'Roteiros de Veículos'.")
    page.get_by_text('Roteiro Veículo', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Roteiro Veículo', exact=True)).to_be_visible()
    log.info("Esperou o agrupamento Roteiro Veículo estar visível.")
    
    # 1. Modificar "Modelo de roteiro veículo"
    campo_modelo_roteiro = page.get_by_label("Modelo de roteiro veículo", exact=True)
    expect(campo_modelo_roteiro).to_be_visible()
    campo_modelo_roteiro.scroll_into_view_if_needed()
    campo_modelo_roteiro.wait_for(state="visible", timeout=3000)
    campo_modelo_roteiro.click()
    log.info("Abriu o popup do item Modelo de roteiro veículo")

    popup_roteiro = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_roteiro).to_be_visible(timeout=5000)
    expect(popup_roteiro.get_by_role("textbox")).to_be_visible()
    popup_roteiro.get_by_role("textbox").fill("ROTEIRO DE VEÍCULO - A4 - CURITIBANOS")
    expect(popup_roteiro.get_by_text("ROTEIRO DE VEÍCULO - A4 - CURITIBANOS", exact=True)).to_be_visible()
    popup_roteiro.get_by_text("ROTEIRO DE VEÍCULO - A4 - CURITIBANOS", exact=True).click()
    expect(popup_roteiro).to_be_hidden()
    log.info("Vinculado o modelo ROTEIRO DE VEÍCULO - A4 - CURITIBANOS ao item Modelo de roteiro veículo.")
    
    # 2. Modificar "Modelo de Comprovante"
    campo_modelo_comprovante = page.get_by_label("Modelo de Comprovante", exact=True)
    expect(campo_modelo_comprovante).to_be_visible()
    campo_modelo_comprovante.scroll_into_view_if_needed()
    campo_modelo_comprovante.wait_for(state="visible", timeout=3000)
    campo_modelo_comprovante.click()
    log.info("Abriu o popup do item Modelo de Comprovante")

    popup_comprovante = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_comprovante).to_be_visible(timeout=5000)
    expect(popup_comprovante.get_by_role("textbox")).to_be_visible()
    popup_comprovante.get_by_role("textbox").fill("ROTEIRO DE VEÍCULOS COMPROVANTE - A4")
    expect(popup_comprovante.get_by_text("ROTEIRO DE VEÍCULOS COMPROVANTE - A4", exact=True)).to_be_visible()
    popup_comprovante.get_by_text("ROTEIRO DE VEÍCULOS COMPROVANTE - A4", exact=True).click()
    expect(popup_comprovante).to_be_hidden()
    log.info("Vinculado o modelo ROTEIRO DE VEÍCULOS COMPROVANTE - A4 ao item Modelo de Comprovante.")
    
    # 3. Modificar "Modelo de Assinatura"
    campo_modelo_assinatura = page.get_by_label("Modelo de Assinatura", exact=True)
    expect(campo_modelo_assinatura).to_be_visible()
    campo_modelo_assinatura.scroll_into_view_if_needed()
    campo_modelo_assinatura.wait_for(state="visible", timeout=3000)
    campo_modelo_assinatura.click()
    log.info("Abriu o popup do item Modelo de Assinatura")

    popup_assinatura = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_assinatura).to_be_visible(timeout=5000)
    expect(popup_assinatura.get_by_role("textbox")).to_be_visible()
    popup_assinatura.get_by_role("textbox").fill("ROTEIRO DE VEÍCULOS ASSINATURA- A4")
    expect(popup_assinatura.get_by_text("ROTEIRO DE VEÍCULOS ASSINATURA- A4", exact=True)).to_be_visible()
    popup_assinatura.get_by_text("ROTEIRO DE VEÍCULOS ASSINATURA- A4", exact=True).click()
    expect(popup_assinatura).to_be_hidden()
    log.info("Vinculado o modelo ROTEIRO DE VEÍCULOS ASSINATURA- A4 ao item Modelo de Assinatura.")
    
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    log.info(f"A pagina com as alterações previstas foram salvas. Teste Roteiro Veículo com o perfil {cliente_teste.cpf} na unidade {cliente_teste.unidade} foi concluído.")