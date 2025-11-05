from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes
import logging

log = logging.getLogger(__name__)

cliente = ["homologacao", "admin"]

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_autorizacoes_vacina(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção 'Vacina' da aba 'Autorizações'.

    Este teste executa as seguintes ações:
    1. Realiza o login no sistema utilizando o perfil de cliente fornecido.
    2. Navega até a tela de 'Parâmetros' do sistema.
    3. Acessa a aba 'Autorizações' e, em seguida, a seção 'Vacina'.
    4. Modifica o modelo de vacina.
    5. Salva as alterações e verifica se a mensagem de sucesso é exibida.

    Args:
        logar_usuario_certa (fixture): Fixture para realizar o login do usuário no sistema.
        perfil_cliente (str): O nome do perfil do cliente a ser testado.
    """
    log.info(f"Iniciando teste 'modificar_parametros_autorizacoes_vacina' para o perfil: {perfil_cliente}")
    
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    log.debug(f"Dados do cliente carregados: {cliente_teste.cpf}")
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Usuário {cliente_teste.cpf} logado com sucesso.")

    # Pesquisa por "Parâmetros" no menu do sistema para acessar a tela de configuração.
    menu = page.locator("#menusistema")
    log.info("Navegando para a tela de Parâmetros do sistema.")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Clica no item de menu "Parâmetros" para abrir a tela de configuração.
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    log.debug("Tela de Parâmetros aberta.")
    
    # --- Seção: Autorizações -> Vacina ---
    # Acessa a aba 'Autorizações' e rola até a seção 'Vacina'.
    log.info("Acessando a seção Autorizações -> Vacina.")
    page.locator("div.dx-list-item:has-text('Autorizações')").click()
    page.get_by_text('Vacina', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Vacina', exact=True)).to_be_visible()
    log.debug("Seção 'Vacina' visível.")
    
    # 1. Modifica o "Modelo Vacina".
    campo_vacina = page.get_by_label("Modelo Vacina", exact=True)
    expect(campo_vacina).to_be_visible()
    campo_vacina.scroll_into_view_if_needed()
    campo_vacina.wait_for(state="visible", timeout=3000)
    campo_vacina.click()
    log.info("Modificando o campo 'Modelo Vacina'.")

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_vacina = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_vacina).to_be_visible(timeout=5000)
    expect(popup_vacina.get_by_role("textbox")).to_be_visible()
    popup_vacina.get_by_role("textbox").fill("CARTEIRA DE VACINA - A4")
    log.debug("Selecionando 'CARTEIRA DE VACINA - A4' no popup.")
    expect(popup_vacina.get_by_text("CARTEIRA DE VACINA - A4", exact=True)).to_be_visible()
    popup_vacina.get_by_text("CARTEIRA DE VACINA - A4", exact=True).click()
    expect(popup_vacina).to_be_hidden()

    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    log.info("Salvando as alterações.")
    expect(page.get_by_text("sucesso")).to_be_visible()
    log.info(f"Teste 'modificar_parametros_autorizacoes_vacina' concluído com sucesso para o perfil: {perfil_cliente}")
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_autorizacoes_outrosprocedimentos(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção 'Outros Procedimentos' da aba 'Autorizações'.

    Este teste executa as seguintes ações:
    1. Realiza o login no sistema utilizando o perfil de cliente fornecido.
    2. Navega até a tela de 'Parâmetros' do sistema.
    3. Acessa a aba 'Autorizações' e, em seguida, a seção 'Outros Procedimentos'.
    4. Modifica o modelo de outros procedimentos.
    5. Salva as alterações e verifica se a mensagem de sucesso é exibida.

    Args:
        logar_usuario_certa (fixture): Fixture para realizar o login do usuário no sistema.
        perfil_cliente (str): O nome do perfil do cliente a ser testado.
    """
    log.info(f"Iniciando teste 'modificar_parametros_autorizacoes_outrosprocedimentos' para o perfil: {perfil_cliente}")
    
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    log.debug(f"Dados do cliente carregados: {cliente_teste.cpf}")
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Usuário {cliente_teste.cpf} logado com sucesso.")

    # Pesquisa por "Parâmetros" no menu do sistema para acessar a tela de configuração.
    menu = page.locator("#menusistema")
    log.info("Navegando para a tela de Parâmetros do sistema.")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Clica no item de menu "Parâmetros" para abrir a tela de configuração.
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    log.debug("Tela de Parâmetros aberta.")
    
    # --- Seção: Autorizações -> Outros Procedimentos ---
    # Acessa a aba 'Autorizações' e rola até a seção 'Outros Procedimentos'.
    log.info("Acessando a seção Autorizações -> Outros Procedimentos.")
    page.locator("div.dx-list-item:has-text('Autorizações')").click()
    page.get_by_text('Outros Procedimentos', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Outros Procedimentos', exact=True)).to_be_visible()
    log.debug("Seção 'Outros Procedimentos' visível.")
    
    # 1. Modifica o "Modelo outros procedimentos".
    campo_outros_procedimentos = page.get_by_label("Modelo outros procedimentos", exact=True)
    expect(campo_outros_procedimentos).to_be_visible()
    campo_outros_procedimentos.scroll_into_view_if_needed()
    campo_outros_procedimentos.wait_for(state="visible", timeout=3000)
    campo_outros_procedimentos.click()
    log.info("Modificando o campo 'Modelo outros procedimentos'.")

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_outros_procedimentos = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_outros_procedimentos).to_be_visible(timeout=5000)
    expect(popup_outros_procedimentos.get_by_role("textbox")).to_be_visible()
    popup_outros_procedimentos.get_by_role("textbox").fill("OUTROS PROCEDIMENTOS - A4")
    log.debug("Selecionando 'OUTROS PROCEDIMENTOS - A4' no popup.")
    expect(popup_outros_procedimentos.get_by_text("OUTROS PROCEDIMENTOS - A4", exact=True)).to_be_visible()
    popup_outros_procedimentos.get_by_text("OUTROS PROCEDIMENTOS - A4", exact=True).click()
    expect(popup_outros_procedimentos).to_be_hidden()

    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    log.info("Salvando as alterações.")
    expect(page.get_by_text("sucesso")).to_be_visible()
    log.info(f"Teste 'modificar_parametros_autorizacoes_outrosprocedimentos' concluído com sucesso para o perfil: {perfil_cliente}")
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_autorizacoes_filaencaminhamento(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção 'Fila Encaminhamento' da aba 'Autorizações'.

    Este teste executa as seguintes ações:
    1. Realiza o login no sistema utilizando o perfil de cliente fornecido.
    2. Navega até a tela de 'Parâmetros' do sistema.
    3. Acessa a aba 'Autorizações' e, em seguida, a seção 'Fila Encaminhamento'.
    4. Modifica os modelos de 'Fila Autorização' e 'Fila Encaminhamento'.
    5. Salva as alterações e verifica se a mensagem de sucesso é exibida.

    Args:
        logar_usuario_certa (fixture): Fixture para realizar o login do usuário no sistema.
        perfil_cliente (str): O nome do perfil do cliente a ser testado.
    """
    log.info(f"Iniciando teste 'modificar_parametros_autorizacoes_filaencaminhamento' para o perfil: {perfil_cliente}")
    
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    log.debug(f"Dados do cliente carregados: {cliente_teste.cpf}")
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Usuário {cliente_teste.cpf} logado com sucesso.")

    # Pesquisa por "Parâmetros" no menu do sistema para acessar a tela de configuração.
    menu = page.locator("#menusistema")
    log.info("Navegando para a tela de Parâmetros do sistema.")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Clica no item de menu "Parâmetros" para abrir a tela de configuração.
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    log.debug("Tela de Parâmetros aberta.")
    
    # --- Seção: Autorizações -> Fila Encaminhamento ---
    # Acessa a aba 'Autorizações' e rola até a seção 'Fila Encaminhamento'.
    log.info("Acessando a seção Autorizações -> Fila Encaminhamento.")
    page.locator("div.dx-list-item:has-text('Autorizações')").click()
    page.get_by_text('Fila Encaminhamento', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Fila Encaminhamento', exact=True)).to_be_visible()
    log.debug("Seção 'Fila Encaminhamento' visível.")
    
    # 1. Modifica o "Modelo fila autorização".
    campo_fila_autorizacao = page.get_by_label("Modelo fila autorização", exact=True)
    expect(campo_fila_autorizacao).to_be_visible()
    campo_fila_autorizacao.scroll_into_view_if_needed()
    campo_fila_autorizacao.wait_for(state="visible", timeout=3000)
    campo_fila_autorizacao.click()
    log.info("Modificando o campo 'Modelo fila autorização'.")

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_fila_autorizacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_fila_autorizacao).to_be_visible(timeout=5000)
    expect(popup_fila_autorizacao.get_by_role("textbox")).to_be_visible()
    popup_fila_autorizacao.get_by_role("textbox").fill("FILA AUTORIZAÇÃO")
    log.debug("Selecionando 'FILA AUTORIZAÇÃO' no popup.")
    expect(popup_fila_autorizacao.get_by_text("FILA AUTORIZAÇÃO", exact=True)).to_be_visible()
    popup_fila_autorizacao.get_by_text("FILA AUTORIZAÇÃO", exact=True).click()
    expect(popup_fila_autorizacao).to_be_hidden()
    
    # 2. Modifica o "Modelo fila encaminhamento".
    campo_fila_encaminhamento = page.get_by_label("Modelo fila encaminhamento", exact=True)
    expect(campo_fila_encaminhamento).to_be_visible()
    campo_fila_encaminhamento.scroll_into_view_if_needed()
    campo_fila_encaminhamento.wait_for(state="visible", timeout=3000)
    campo_fila_encaminhamento.click()
    log.info("Modificando o campo 'Modelo fila encaminhamento'.")

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_fila_encaminhamento = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_fila_encaminhamento).to_be_visible(timeout=5000)
    expect(popup_fila_encaminhamento.get_by_role("textbox")).to_be_visible()
    popup_fila_encaminhamento.get_by_role("textbox").fill("FILA ENCAMINHAMENTO")
    log.debug("Selecionando 'FILA ENCAMINHAMENTO' no popup.")
    expect(popup_fila_encaminhamento.get_by_text("FILA ENCAMINHAMENTO", exact=True)).to_be_visible()
    popup_fila_encaminhamento.get_by_text("FILA ENCAMINHAMENTO", exact=True).click()
    expect(popup_fila_encaminhamento).to_be_hidden()

    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    log.info("Salvando as alterações.")
    expect(page.get_by_text("sucesso")).to_be_visible()
    log.info(f"Teste 'modificar_parametros_autorizacoes_filaencaminhamento' concluído com sucesso para o perfil: {perfil_cliente}")