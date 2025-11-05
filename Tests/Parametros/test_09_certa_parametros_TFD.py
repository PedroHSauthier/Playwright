from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes
import logging

log = logging.getLogger(__name__)

cliente = "homologacao"

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_TFD(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção 'Modelo Impressão' da aba 'TFD'.

    Este teste executa as seguintes ações:
    1. Realiza o login no sistema utilizando o perfil de cliente fornecido.
    2. Navega até a tela de 'Parâmetros' do sistema.
    3. Acessa a aba 'TFD' e, em seguida, a seção 'Modelo Impressão'.
    4. Modifica os modelos de impressão para 'Modelo tfd Frente', 'Modelo tfd Verso' e 'Modelo tfd Comprovante'.
    5. Tira um screenshot da tela de parâmetros de TFD.
    6. Salva as alterações e verifica se a mensagem de sucesso é exibida.

    Args:
        logar_usuario_certa (fixture): Fixture para realizar o login do usuário no sistema.
        perfil_cliente (str): O nome do perfil do cliente a ser testado.
    """
    
    
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    log.info(f"Iniciando teste de parâmetros de TFD para o perfil: {perfil_cliente}")
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Usuário {cliente_teste.cpf} logado.")

    # Pesquisa por "Parâmetros" no menu do sistema para acessar a tela de configuração.
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Clica no item de menu "Parâmetros" para abrir a tela de configuração.
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    log.info("Navegou para a página Parâmetros")
    
    # --- Seção: TFD -> Modelo Impressão ---
    # Acessa a aba 'TFD' e rola até a seção 'Modelo Impressão'.
    page.locator("div.dx-list-item:has-text('TFD')").click()
    log.info("Acessou a aba 'Empresa'.")
    page.get_by_text('Modelo Impressão', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Modelo Impressão', exact=True)).to_be_visible()
    
    
    # 1. Modifica o "Modelo tfd frente".
    campo_tfdfrente = page.get_by_label("Modelo tfd Frente", exact=True)
    expect(campo_tfdfrente).to_be_visible()
    campo_tfdfrente.scroll_into_view_if_needed()
    campo_tfdfrente.wait_for(state="visible", timeout=3000)
    campo_tfdfrente.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_tfdfrente = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_tfdfrente).to_be_visible(timeout=5000)
    expect(popup_tfdfrente.get_by_role("textbox")).to_be_visible()
    popup_tfdfrente.get_by_role("textbox").fill("PROCESSO TFD FRENTE - A4")
    expect(popup_tfdfrente.get_by_text("PROCESSO TFD FRENTE - A4", exact=True)).to_be_visible()
    popup_tfdfrente.get_by_text("PROCESSO TFD FRENTE - A4", exact=True).click()
    expect(popup_tfdfrente).to_be_hidden()
    
    # 2. Modifica o "Modelo tfd Verso".
    campo_tfdverso = page.get_by_label("Modelo tfd Verso", exact=True)
    expect(campo_tfdverso).to_be_visible()
    campo_tfdverso.scroll_into_view_if_needed()
    campo_tfdverso.wait_for(state="visible", timeout=3000)
    campo_tfdverso.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_tfdverso = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_tfdverso).to_be_visible(timeout=5000)
    expect(popup_tfdverso.get_by_role("textbox")).to_be_visible()
    popup_tfdverso.get_by_role("textbox").fill("PROCESSO TFD VERSO - A4")
    expect(popup_tfdverso.get_by_text("PROCESSO TFD VERSO - A4", exact=True)).to_be_visible()
    popup_tfdverso.get_by_text("PROCESSO TFD VERSO - A4", exact=True).click()
    expect(popup_tfdverso).to_be_hidden()
    
    # 3. Modifica o "Modelo tfd Comprovante".
    campo_tfdcomprovante = page.get_by_label("Modelo tfd Comprovante", exact=True)
    expect(campo_tfdcomprovante).to_be_visible()
    campo_tfdcomprovante.scroll_into_view_if_needed()
    campo_tfdcomprovante.wait_for(state="visible", timeout=3000)
    campo_tfdcomprovante.click()

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_tfdcomprovante = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_tfdcomprovante).to_be_visible(timeout=5000)
    expect(popup_tfdcomprovante.get_by_role("textbox")).to_be_visible()
    popup_tfdcomprovante.get_by_role("textbox").fill("PROCESSO TFD COMPROVANTE - A4")
    expect(popup_tfdcomprovante.get_by_text("PROCESSO TFD COMPROVANTE - A4", exact=True)).to_be_visible()
    popup_tfdcomprovante.get_by_text("PROCESSO TFD COMPROVANTE - A4", exact=True).click()
    expect(popup_tfdcomprovante).to_be_hidden()
    
    # Tira um screenshot da tela para verificação visual.
    page.screenshot(path="screenshots/certa/parametrosTFD.png")
    
    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()