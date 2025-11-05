from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes
import logging

log = logging.getLogger(__name__)

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes("homologacao"))
def test_modificar_parametros_cadastro(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção de Cadastro Individual.
    Este teste navega até a página de parâmetros, seleciona opções para os modelos
    de domicílio e grupo, e verifica se as interações ocorrem como esperado.
    """
    log.info(f"Iniciando teste 'modificar_parametros_cadastro' para o perfil: {perfil_cliente}")
    
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    log.debug(f"Dados do cliente carregados: {cliente_teste.cpf}")
    
    # A fixture de login recebe o objeto cliente.
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Usuário {cliente_teste.cpf} logado com sucesso.")

    # Pesquisar "Parâmetros" na tela inicial para encontrar a page Parâmetros
    menu = page.locator("#menusistema")
    log.info("Navegando para a tela de Parâmetros do sistema.")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Abrir a Tela de Parâmetros
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    log.debug("Tela de Parâmetros aberta.")
    
    # --- Seção: Cadastros -> Individual ---
    log.info("Acessando a seção Cadastros -> Individual.")
    expect(page.get_by_text("Individual")).to_be_visible()
    log.debug("Seção 'Individual' visível.")

    # 1. Modificar "Modelo de Domicilio Individual"
    log.info("Modificando o campo 'Modelo de Domicilio Individual'.")
    page.get_by_label("Modelo de Domicilio Individual").click()
    popup_domicilio = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_domicilio).to_be_visible()
    log.debug("Selecionando 'FICHA CADASTRO INDIVIDUAL - A4' no popup.")
    popup_domicilio.get_by_text("FICHA CADASTRO INDIVIDUAL - A4").click()
    expect(popup_domicilio).to_be_hidden()

    # 2. Modificar "Modelo cadastro Grupo"
    log.info("Modificando o campo 'Modelo cadastro Grupo'.")
    page.get_by_label("Modelo cadastro Grupo").click()
    popup_grupo = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_grupo).to_be_visible()
    log.debug("Selecionando 'RELATÓRIO - CADASTRO INDIVIDUAL RESUMIDO' no popup.")
    popup_grupo.get_by_text("RELATÓRIO - CADASTRO INDIVIDUAL RESUMIDO", exact=True).click()
    expect(popup_grupo).to_be_hidden()
    
    page.get_by_role("button", name="Salvar").click()
    log.info("Salvando as alterações.")
    expect(page.get_by_text("sucesso")).to_be_visible()
    log.info(f"A pagina com as alterações previstas foram salvas. Teste Cadastro com o perfil {cliente_teste.cpf} na unidade {cliente_teste.unidade} foi concluído.")