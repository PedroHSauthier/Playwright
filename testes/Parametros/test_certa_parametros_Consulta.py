from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes

cliente = "homologacao"
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_consulta_procedimentos(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção de Consultas.
    Este teste navega até a página de parâmetros, seleciona opções para os modelos
    de Procedimentos, receituários, exame, encaminhamento, solicitação de retorno, orientações, prontuário e comprovante de agendamento, e verifica se as interações ocorrem como esperado.
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
    
    # --- Seção: Consultas -> Procedimentos Padrões ---
    page.locator("div.dx-list-item:has-text('Consulta')").click() 
    expect(page.get_by_text("Procedimentos Padrões")).to_be_visible()
    
    # 1. Modificar "Procedimentos Padrões"
    page.get_by_label("Avaliação Antropométrica").click()
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("antropometrica")
    expect(popup_avaliacao.get_by_text("AVALIAÇÃO ANTROPOMÉTRICA")).to_be_visible()
    popup_avaliacao.get_by_text("AVALIAÇÃO ANTROPOMÉTRICA", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    # 2. Modificar "Medição de Altura"
    page.get_by_label("Medição de Altura").click()
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("medicao de altura")
    expect(popup_avaliacao.get_by_text("MEDIÇÃO DE ALTURA")).to_be_visible()
    popup_avaliacao.get_by_text("MEDIÇÃO DE ALTURA", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    # 3. Modificar "Medição de Peso"
    page.get_by_label("Medição de Peso").click()
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("Medicao de peso")
    expect(popup_avaliacao.get_by_text("MEDIÇÃO DE PESO")).to_be_visible()
    popup_avaliacao.get_by_text("MEDIÇÃO DE PESO", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    # 4. Modificar "Aferição de Pressão Arterial"
    page.get_by_label("Aferição de Pressão Arterial").click()
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("Aferição de Pressão Arterial")
    expect(popup_avaliacao.get_by_text("AFERIÇÃO DE PRESSÃO ARTERIAL")).to_be_visible()
    popup_avaliacao.get_by_text("AFERIÇÃO DE PRESSÃO ARTERIAL", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    # 5. Modificar "Aferição de Glicemia Capilar"
    page.get_by_label("Aferição de Glicemia Capilar").click()
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("GLICEMIA CAPILAR")
    expect(popup_avaliacao.get_by_text("GLICEMIA CAPILAR", exact=True)).to_be_visible()
    popup_avaliacao.get_by_text("GLICEMIA CAPILAR", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    # 6. Modificar "Aferição de temperatura"
    page.get_by_label("Aferição de Temperatura").click()
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("Aferição de temperatura")
    expect(popup_avaliacao.get_by_text("AFERIÇÃO DE TEMPERATURA")).to_be_visible()
    popup_avaliacao.get_by_text("AFERIÇÃO DE TEMPERATURA", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    # 7. Modificar "Roteiro Veículo"
    page.get_by_label("Roteiro Veículo", exact=True).click()
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("UNIDADE DE REMUNERAÇÃO PARA DESLOCAMENTO DE PACIENTE POR TRANSPORTE TERRESTRE (CADA 50 KM )")
    expect(popup_avaliacao.get_by_text("UNIDADE DE REMUNERAÇÃO PARA DESLOCAMENTO DE PACIENTE POR TRANSPORTE TERRESTRE (CADA 50 KM )")).to_be_visible()
    popup_avaliacao.get_by_text("UNIDADE DE REMUNERAÇÃO PARA DESLOCAMENTO DE PACIENTE POR TRANSPORTE TERRESTRE (CADA 50 KM )", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    # 8. Modificar "Roteiro Veículo Acompanhante"
    page.get_by_label("Roteiro Veículo Acompanhante", exact=True).click()
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("UNIDADE DE REMUNERAÇÃO PARA DESLOCAMENTO DE ACOMPANHANTE POR TRANSPORTE TERRESTRE (CADA 50 KM DE DISTANCIA)")
    expect(popup_avaliacao.get_by_text("UNIDADE DE REMUNERAÇÃO PARA DESLOCAMENTO DE ACOMPANHANTE POR TRANSPORTE TERRESTRE (CADA 50 KM DE DISTANCIA)")).to_be_visible()
    popup_avaliacao.get_by_text("UNIDADE DE REMUNERAÇÃO PARA DESLOCAMENTO DE ACOMPANHANTE POR TRANSPORTE TERRESTRE (CADA 50 KM DE DISTANCIA)", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_consulta_receituarios(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção de Consultas.
    Este teste navega até a página de parâmetros, seleciona opções para os modelos
    de Procedimentos, receituários, exame, encaminhamento, solicitação de retorno, orientações, prontuário e comprovante de agendamento, e verifica se as interações ocorrem como esperado.
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
    
    # --- Seção: Consultas -> Receituários ---
    page.locator("div.dx-list-item:has-text('Consulta')").click()
    expect(page.get_by_text('Receituários')).to_be_visible()
    
    # 1. Modificar "Modelo de receita"
    campo_modelo_receita = page.get_by_label("Modelo de Receita", exact=True)
    expect(campo_modelo_receita).to_be_visible()
    campo_modelo_receita.scroll_into_view_if_needed()
    campo_modelo_receita.wait_for(state="visible", timeout=3000)
    campo_modelo_receita.click()

    # Aguardar o popup aparecer explicitamente
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao).to_be_visible(timeout=5000)
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("RECEITUARIO - A4 - SEPARADA AO MEIO")
    expect(popup_avaliacao.get_by_text("RECEITUARIO - A4 - SEPARADA AO MEIO", exact=True)).to_be_visible()
    popup_avaliacao.get_by_text("RECEITUARIO - A4 - SEPARADA AO MEIO", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    # 2. Modificar "Modelo de Receita Reimpressão"
    campo_modelo_receita = page.get_by_label("Modelo de Receita Reimpressão", exact=True)
    expect(campo_modelo_receita).to_be_visible()
    campo_modelo_receita.scroll_into_view_if_needed()
    campo_modelo_receita.wait_for(state="visible", timeout=3000)
    campo_modelo_receita.click()

    # Aguardar o popup aparecer explicitamente
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao).to_be_visible(timeout=5000)
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("RECEITUARIO REIMPRESSAO - A5")
    expect(popup_avaliacao.get_by_text("RECEITUARIO REIMPRESSAO - A5", exact=True)).to_be_visible()
    popup_avaliacao.get_by_text("RECEITUARIO REIMPRESSAO - A5", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    # 3. Modificar "Modelo de Receita Reimpressão"
    campo_modelo_receita = page.get_by_label("Modelo de Receita Continua", exact=True)
    expect(campo_modelo_receita).to_be_visible()
    campo_modelo_receita.scroll_into_view_if_needed()
    campo_modelo_receita.wait_for(state="visible", timeout=3000)
    campo_modelo_receita.click()

    # Aguardar o popup aparecer explicitamente
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao).to_be_visible(timeout=5000)
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("RECEITUARIO USO CONTINUO - A4 - SEPARADA AO MEIO")
    expect(popup_avaliacao.get_by_text("RECEITUARIO USO CONTINUO - A4 - SEPARADA AO MEIO", exact=True)).to_be_visible()
    popup_avaliacao.get_by_text("RECEITUARIO USO CONTINUO - A4 - SEPARADA AO MEIO", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_consulta_solicitacao(logar_usuario_certa, perfil_cliente):
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
    
    # --- Seção: Consultas -> Solicitacao de exame ---
    page.locator("div.dx-list-item:has-text('Consulta')").click()
    page.get_by_text('Solicitacao de exame').scroll_into_view_if_needed()
    expect(page.get_by_text('Solicitacao de exame')).to_be_visible()
    
    # 1. Modificar "Modelo de Solicitacao de Exames"
    campo_modelo_receita = page.get_by_label("Modelo de Solicitação de Exames", exact=True)
    expect(campo_modelo_receita).to_be_visible()
    campo_modelo_receita.scroll_into_view_if_needed()
    campo_modelo_receita.wait_for(state="visible", timeout=3000)
    campo_modelo_receita.click()

    # Aguardar o popup aparecer explicitamente
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao).to_be_visible(timeout=5000)
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("SOLICITAÇÃO DE EXAMES - A5")
    expect(popup_avaliacao.get_by_text("SOLICITAÇÃO DE EXAMES - A5", exact=True)).to_be_visible()
    popup_avaliacao.get_by_text("SOLICITAÇÃO DE EXAMES - A5", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    # 2. Modificar "Modelo de Reimpressão Solicitação de Exames"
    campo_modelo_receita = page.get_by_label("Modelo de Reimpressão Solicitação de Exames", exact=True)
    expect(campo_modelo_receita).to_be_visible()
    campo_modelo_receita.scroll_into_view_if_needed()
    campo_modelo_receita.wait_for(state="visible", timeout=3000)
    campo_modelo_receita.click()

    # Aguardar o popup aparecer explicitamente
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao).to_be_visible(timeout=5000)
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("SOLICITAÇÃO DE EXAMES  REIMPRESSÃO - A4 - SEPARADA AO MEIO")
    expect(popup_avaliacao.get_by_text("SOLICITAÇÃO DE EXAMES  REIMPRESSÃO - A4 - SEPARADA AO MEIO", exact=True)).to_be_visible()
    popup_avaliacao.get_by_text("SOLICITAÇÃO DE EXAMES  REIMPRESSÃO - A4 - SEPARADA AO MEIO", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_consulta_encaminhamento(logar_usuario_certa, perfil_cliente):
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
    
    # --- Seção: Consultas -> Encaminhamento Médico ---
    page.locator("div.dx-list-item:has-text('Consulta')").click()
    page.get_by_text('Encaminhamento Médico').scroll_into_view_if_needed()
    expect(page.get_by_text('Encaminhamento Médico')).to_be_visible()
    
    # 1. Modificar "Modelo de Encaminhamento"
    campo_modelo_receita = page.get_by_label("Modelo de Encaminhamento", exact=True)
    expect(campo_modelo_receita).to_be_visible()
    campo_modelo_receita.scroll_into_view_if_needed()
    campo_modelo_receita.wait_for(state="visible", timeout=3000)
    campo_modelo_receita.click()

    # Aguardar o popup aparecer explicitamente
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao).to_be_visible(timeout=5000)
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("ENCAMINHAMENTO PARA ESPECIALIDADES - A4")
    expect(popup_avaliacao.get_by_text("ENCAMINHAMENTO PARA ESPECIALIDADES - A4", exact=True)).to_be_visible()
    popup_avaliacao.get_by_text("ENCAMINHAMENTO PARA ESPECIALIDADES - A4", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
 
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_consulta_solicitacao_retorno(logar_usuario_certa, perfil_cliente):
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
    
    # --- Seção: Consultas -> Solicitação de Retorno ---
    page.locator("div.dx-list-item:has-text('Consulta')").click()
    page.get_by_text('Solicitação de Retorno').scroll_into_view_if_needed()
    expect(page.get_by_text('Solicitação de Retorno')).to_be_visible()
    
    # 1. Modificar "Modelo de Encaminhamento"
    campo_modelo_receita = page.get_by_label("Modelo de Retorno", exact=True)
    expect(campo_modelo_receita).to_be_visible()
    campo_modelo_receita.scroll_into_view_if_needed()
    campo_modelo_receita.wait_for(state="visible", timeout=3000)
    campo_modelo_receita.click()

    # Aguardar o popup aparecer explicitamente
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao).to_be_visible(timeout=5000)
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("SOLICITAÇÃO DE RETORNO - A4")
    expect(popup_avaliacao.get_by_text("SOLICITAÇÃO DE RETORNO - A4", exact=True)).to_be_visible()
    popup_avaliacao.get_by_text("SOLICITAÇÃO DE RETORNO - A4", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_consulta_orientacao(logar_usuario_certa, perfil_cliente):
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
    
    # --- Seção: Consultas -> Solicitação de Retorno ---
    page.locator("div.dx-list-item:has-text('Consulta')").click()
    page.get_by_text('Orientações').scroll_into_view_if_needed()
    expect(page.get_by_text('Orientações')).to_be_visible()
    
    # 1. Modificar "Modelo de Orientações"
    campo_modelo_receita = page.get_by_label("Modelo de orientação", exact=True)
    expect(campo_modelo_receita).to_be_visible()
    campo_modelo_receita.scroll_into_view_if_needed()
    campo_modelo_receita.wait_for(state="visible", timeout=3000)
    campo_modelo_receita.click()

    # Aguardar o popup aparecer explicitamente
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao).to_be_visible(timeout=5000)
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("ORIENTAÇÃO DA CONSULTA - A4")
    expect(popup_avaliacao.get_by_text("ORIENTAÇÃO DA CONSULTA - A4", exact=True)).to_be_visible()
    popup_avaliacao.get_by_text("ORIENTAÇÃO DA CONSULTA - A4", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_consulta_prontuario(logar_usuario_certa, perfil_cliente):
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
    
    # --- Seção: Consultas -> Prontuário ---
    page.locator("div.dx-list-item:has-text('Consulta')").click()
    page.get_by_text('Prontuário', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Prontuário', exact=True)).to_be_visible()
    
    # 1. Modificar "Modelo de Orientações"
    campo_modelo_receita = page.get_by_label("Modelo de prontuario", exact=True)
    expect(campo_modelo_receita).to_be_visible()
    campo_modelo_receita.scroll_into_view_if_needed()
    campo_modelo_receita.wait_for(state="visible", timeout=3000)
    campo_modelo_receita.click()

    # Aguardar o popup aparecer explicitamente
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao).to_be_visible(timeout=5000)
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("PRONTUÁRIO - A4")
    expect(popup_avaliacao.get_by_text("PRONTUÁRIO - A4", exact=True)).to_be_visible()
    popup_avaliacao.get_by_text("PRONTUÁRIO - A4", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
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
    
    # --- Seção: Consultas -> Comprovante de agendamento ---
    page.locator("div.dx-list-item:has-text('Consulta')").click()
    page.get_by_text('Comprovante de agendamento').scroll_into_view_if_needed()
    expect(page.get_by_text('Comprovante de agendamento')).to_be_visible()
    
    # 1. Modificar "Modelo Comprovante de agendamento"
    campo_modelo_receita = page.get_by_label("Modelo Comprovante Agendamento", exact=True)
    expect(campo_modelo_receita).to_be_visible()
    campo_modelo_receita.scroll_into_view_if_needed()
    campo_modelo_receita.wait_for(state="visible", timeout=3000)
    campo_modelo_receita.click()

    # Aguardar o popup aparecer explicitamente
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao).to_be_visible(timeout=5000)
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("CONFIRMAÇÃO DE AGENDAMENTO - FOLHA CONTÍNUA")
    expect(popup_avaliacao.get_by_text("CONFIRMAÇÃO DE AGENDAMENTO - FOLHA CONTÍNUA", exact=True)).to_be_visible()
    popup_avaliacao.get_by_text("CONFIRMAÇÃO DE AGENDAMENTO - FOLHA CONTÍNUA", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
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
    
    # --- Seção: Consultas -> Comprovante de agendamento ---
    page.locator("div.dx-list-item:has-text('Consulta')").click()
    page.get_by_text('Comprovante de agendamento').scroll_into_view_if_needed()
    expect(page.get_by_text('Comprovante de agendamento')).to_be_visible()
    
    # 1. Modificar "Modelo Comprovante de agendamento"
    campo_modelo_receita = page.get_by_label("Modelo Comprovante Agendamento", exact=True)
    expect(campo_modelo_receita).to_be_visible()
    campo_modelo_receita.scroll_into_view_if_needed()
    campo_modelo_receita.wait_for(state="visible", timeout=3000)
    campo_modelo_receita.click()

    # Aguardar o popup aparecer explicitamente
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao).to_be_visible(timeout=5000)
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("CONFIRMAÇÃO DE AGENDAMENTO - FOLHA CONTÍNUA")
    expect(popup_avaliacao.get_by_text("CONFIRMAÇÃO DE AGENDAMENTO - FOLHA CONTÍNUA", exact=True)).to_be_visible()
    popup_avaliacao.get_by_text("CONFIRMAÇÃO DE AGENDAMENTO - FOLHA CONTÍNUA", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    
