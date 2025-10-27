from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes())
def inativo_test_modificar_parametros_cadastro(logar_usuario_certa, perfil_cliente):
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
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes())
def test_modificar_parametros_consulta(logar_usuario_certa, perfil_cliente):
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
    
    # --- Seção: Consultas -> Receituários ---
    
    # 1. Modificar "Modelo de receita"
    page.get_by_label("Modelo de receita", exact=True).click()
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("")
    expect(popup_avaliacao.get_by_text("")).to_be_visible()
    popup_avaliacao.get_by_text("", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    
    page.screenshot(path="screenshots/certa/parametros.png")
