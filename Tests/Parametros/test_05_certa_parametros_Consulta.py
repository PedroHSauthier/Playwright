from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes
import logging

log = logging.getLogger(__name__)

cliente = "homologacao"
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_consulta_procedimentos(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção de 'Procedimentos Padrões' em Consultas.

    O teste realiza as seguintes ações:
    1. Realiza o login no sistema com o perfil de cliente especificado.
    2. Navega até a tela de 'Parâmetros'.
    3. Acessa a seção 'Consulta' e, em seguida, 'Procedimentos Padrões'.
    4. Modifica os valores para diversos procedimentos padrões, como 'Avaliação Antropométrica', 'Medição de Altura', 'Medição de Peso', entre outros.
    5. Salva as alterações e verifica se a mensagem de sucesso é exibida.

    Args:
        logar_usuario_certa: Fixture para fazer o login do usuário.
        perfil_cliente: O perfil do cliente a ser usado no teste.
    """
    
    log.info(f"Iniciando teste de parâmetros de Consulta - Procedimentos Padrões para o perfil: {perfil_cliente}")
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
    
    # --- Seção: Consultas -> Procedimentos Padrões ---
    page.locator("div.dx-list-item:has-text('Consulta')").click() 
    log.info("Acessou a aba 'Consulta'.")
    expect(page.get_by_text("Procedimentos Padrões", exact=True)).to_be_visible()
    log.info("Esperou o agrupamento Procedimentos Padrões estar visível.")
    
    # 1. Modifica o procedimento "Avaliação Antropométrica".
    page.get_by_label("Avaliação Antropométrica").click()
    log.info("Abriu o popup do item Avaliação Antropométrica")
    popup_avaliacao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_avaliacao.get_by_role("textbox")).to_be_visible()
    popup_avaliacao.get_by_role("textbox").fill("antropometrica")
    expect(popup_avaliacao.get_by_text("AVALIAÇÃO ANTROPOMÉTRICA")).to_be_visible()
    popup_avaliacao.get_by_text("AVALIAÇÃO ANTROPOMÉTRICA", exact=True).click()
    expect(popup_avaliacao).to_be_hidden()
    log.info("Vinculado o procedimento AVALIAÇÃO ANTROPOMÉTRICA ao item Avaliação Antropométrica.")
    
    # 2. Modifica o procedimento "Medição de Altura".
    page.get_by_label("Medição de Altura").click()
    log.info("Abriu o popup do item Medição de Altura")
    popup_altura = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_altura.get_by_role("textbox")).to_be_visible()
    popup_altura.get_by_role("textbox").fill("medicao de altura")
    expect(popup_altura.get_by_text("MEDIÇÃO DE ALTURA")).to_be_visible()
    popup_altura.get_by_text("MEDIÇÃO DE ALTURA", exact=True).click()
    expect(popup_altura).to_be_hidden()
    log.info("Vinculado o procedimento MEDIÇÃO DE ALTURA ao item Medição de Altura.")
    
    # 3. Modifica o procedimento "Medição de Peso".
    page.get_by_label("Medição de Peso").click()
    log.info("Abriu o popup do item Medição de Peso")
    popup_peso = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_peso.get_by_role("textbox")).to_be_visible()
    popup_peso.get_by_role("textbox").fill("Medicao de peso")
    expect(popup_peso.get_by_text("MEDIÇÃO DE PESO")).to_be_visible()
    popup_peso.get_by_text("MEDIÇÃO DE PESO", exact=True).click()
    expect(popup_peso).to_be_hidden()
    log.info("Vinculado o procedimento MEDIÇÃO DE PESO ao item Medição de Peso.")
    
    # 4. Modifica o procedimento "Aferição de Pressão Arterial".
    page.get_by_label("Aferição de Pressão Arterial").click()
    log.info("Abriu o popup do item Aferição de Pressão Arterial")
    popup_pressao = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_pressao.get_by_role("textbox")).to_be_visible()
    popup_pressao.get_by_role("textbox").fill("Aferição de Pressão Arterial")
    expect(popup_pressao.get_by_text("AFERIÇÃO DE PRESSÃO ARTERIAL")).to_be_visible()
    popup_pressao.get_by_text("AFERIÇÃO DE PRESSÃO ARTERIAL", exact=True).click()
    expect(popup_pressao).to_be_hidden()
    log.info("Vinculado o procedimento AFERIÇÃO DE PRESSÃO ARTERIAL ao item Aferição de Pressão Arterial.")
    
    # 5. Modifica o procedimento "Aferição de Glicemia Capilar".
    page.get_by_label("Aferição de Glicemia Capilar").click()
    log.info("Abriu o popup do item Aferição de Glicemia Capilar")
    popup_glicemia = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_glicemia.get_by_role("textbox")).to_be_visible()
    popup_glicemia.get_by_role("textbox").fill("GLICEMIA CAPILAR")
    expect(popup_glicemia.get_by_text("GLICEMIA CAPILAR", exact=True)).to_be_visible()
    popup_glicemia.get_by_text("GLICEMIA CAPILAR", exact=True).click()
    expect(popup_glicemia).to_be_hidden()
    log.info("Vinculado o procedimento GLICEMIA CAPILAR ao item Aferição de Glicemia Capilar.")
    
    # 6. Modifica o procedimento "Aferição de temperatura".
    page.get_by_label("Aferição de Temperatura").click()
    log.info("Abriu o popup do item Aferição de Temperatura")
    popup_temperatura = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_temperatura.get_by_role("textbox")).to_be_visible()
    popup_temperatura.get_by_role("textbox").fill("Aferição de temperatura")
    expect(popup_temperatura.get_by_text("AFERIÇÃO DE TEMPERATURA")).to_be_visible()
    popup_temperatura.get_by_text("AFERIÇÃO DE TEMPERATURA", exact=True).click()
    expect(popup_temperatura).to_be_hidden()
    log.info("Vinculado o procedimento AFERIÇÃO DE TEMPERATURA ao item Aferição de Temperatura.")
    
    # 7. Modifica o procedimento "Roteiro Veículo".
    page.get_by_label("Roteiro Veículo", exact=True).click()
    log.info("Abriu o popup do item Roteiro Veículo")
    popup_veiculo = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_veiculo.get_by_role("textbox")).to_be_visible()
    popup_veiculo.get_by_role("textbox").fill("UNIDADE DE REMUNERAÇÃO PARA DESLOCAMENTO DE PACIENTE POR TRANSPORTE TERRESTRE (CADA 50 KM )")
    expect(popup_veiculo.get_by_text("UNIDADE DE REMUNERAÇÃO PARA DESLOCAMENTO DE PACIENTE POR TRANSPORTE TERRESTRE (CADA 50 KM )")).to_be_visible()
    popup_veiculo.get_by_text("UNIDADE DE REMUNERAÇÃO PARA DESLOCAMENTO DE PACIENTE POR TRANSPORTE TERRESTRE (CADA 50 KM )", exact=True).click()
    expect(popup_veiculo).to_be_hidden()
    log.info("Vinculado o procedimento UNIDADE DE REMUNERAÇÃO PARA DESLOCAMENTO DE PACIENTE POR TRANSPORTE TERRESTRE (CADA 50 KM ) ao item Roteiro Veículo.")
    
    # 8. Modifica o procedimento "Roteiro Veículo Acompanhante".
    page.get_by_label("Roteiro Veículo Acompanhante", exact=True).click()
    log.info("Abriu o popup do item Roteiro Veículo Acompanhante")
    popup_veiculo_comp = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_veiculo_comp.get_by_role("textbox")).to_be_visible()
    popup_veiculo_comp.get_by_role("textbox").fill("UNIDADE DE REMUNERAÇÃO PARA DESLOCAMENTO DE ACOMPANHANTE POR TRANSPORTE TERRESTRE (CADA 50 KM DE DISTANCIA)")
    expect(popup_veiculo_comp.get_by_text("UNIDADE DE REMUNERAÇÃO PARA DESLOCAMENTO DE ACOMPANHANTE POR TRANSPORTE TERRESTRE (CADA 50 KM DE DISTANCIA)")).to_be_visible()
    popup_veiculo_comp.get_by_text("UNIDADE DE REMUNERAÇÃO PARA DESLOCAMENTO DE ACOMPANHANTE POR TRANSPORTE TERRESTRE (CADA 50 KM DE DISTANCIA)", exact=True).click()
    expect(popup_veiculo_comp).to_be_hidden()
    log.info("Vinculado o procedimento UNIDADE DE REMUNERAÇÃO PARA DESLOCAMENTO DE ACOMPANHANTE POR TRANSPORTE TERRESTRE (CADA 50 KM DE DISTANCIA) ao item Roteiro Veículo Acompanhante.")
    
    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    log.info("Alterações salvas com sucesso.")
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_consulta_receituarios(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção de 'Receituários' em Consultas.

    O teste realiza as seguintes ações:
    1. Realiza o login no sistema com o perfil de cliente especificado.
    2. Navega até a tela de 'Parâmetros'.
    3. Acessa a seção 'Consulta' e, em seguida, 'Receituários'.
    4. Modifica os modelos de receita, incluindo 'Modelo de Receita', 'Modelo de Receita Reimpressão' e 'Modelo de Receita Continua'.
    5. Salva as alterações e verifica se a mensagem de sucesso é exibida.

    Args:
        logar_usuario_certa: Fixture para fazer o login do usuário.
        perfil_cliente: O perfil do cliente a ser usado no teste.
    """
    
    log.info(f"Iniciando teste de parâmetros de Consulta - Receituários para o perfil: {perfil_cliente}")
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Usuário {cliente_teste.cpf} logado.")

    # Pesquisa por "Parâmetros" no menu do sistema.
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Clica no item de menu "Parâmetros" para abrir a tela de configuração.
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    log.info("Navegou para a página Parâmetros")
    
    # --- Seção: Consultas -> Receituários ---
    # Acessa a aba 'Consulta' e verifica se a seção 'Receituários' está visível.
    page.locator("div.dx-list-item:has-text('Consulta')").click()
    log.info("Acessou a aba 'Consulta'.")
    expect(page.get_by_text('Receituários', exact=True)).to_be_visible()
    log.info("Esperou o agrupamento Receituários estar visível.")
    
    # 1. Modifica o "Modelo de Receita".
    campo_modelo_receita = page.get_by_label("Modelo de Receita", exact=True)
    expect(campo_modelo_receita).to_be_visible()
    campo_modelo_receita.scroll_into_view_if_needed()
    campo_modelo_receita.wait_for(state="visible", timeout=3000)
    campo_modelo_receita.click()
    log.info("Abriu o popup do item Modelo de Receita")

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_modelo_receita = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_modelo_receita).to_be_visible(timeout=5000)
    expect(popup_modelo_receita.get_by_role("textbox")).to_be_visible()
    popup_modelo_receita.get_by_role("textbox").fill("RECEITUARIO - A4 - SEPARADA AO MEIO")
    expect(popup_modelo_receita.get_by_text("RECEITUARIO - A4 - SEPARADA AO MEIO", exact=True)).to_be_visible()
    popup_modelo_receita.get_by_text("RECEITUARIO - A4 - SEPARADA AO MEIO", exact=True).click()
    expect(popup_modelo_receita).to_be_hidden()
    log.info("Vinculado o modelo RECEITUARIO - A4 - SEPARADA AO MEIO ao item Modelo de Receita.")
    
    # 2. Modifica o "Modelo de Receita Reimpressão".
    campo_modelo_receita_reim = page.get_by_label("Modelo de Receita Reimpressão", exact=True)
    expect(campo_modelo_receita_reim).to_be_visible()
    campo_modelo_receita_reim.scroll_into_view_if_needed()
    campo_modelo_receita_reim.wait_for(state="visible", timeout=3000)
    campo_modelo_receita_reim.click()
    log.info("Abriu o popup do item Modelo de Receita Reimpressão")

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_modelo_receita_reim = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_modelo_receita_reim).to_be_visible(timeout=5000)
    expect(popup_modelo_receita_reim.get_by_role("textbox")).to_be_visible()
    popup_modelo_receita_reim.get_by_role("textbox").fill("RECEITUARIO REIMPRESSAO - A5")
    expect(popup_modelo_receita_reim.get_by_text("RECEITUARIO REIMPRESSAO - A5", exact=True)).to_be_visible()
    popup_modelo_receita_reim.get_by_text("RECEITUARIO REIMPRESSAO - A5", exact=True).click()
    expect(popup_modelo_receita_reim).to_be_hidden()
    log.info("Vinculado o modelo RECEITUARIO REIMPRESSAO - A5 ao item Modelo de Receita Reimpressão.")
    
    # 3. Modifica o "Modelo de Receita Continua".
    campo_modelo_receita_cont = page.get_by_label("Modelo de Receita Continua", exact=True)
    expect(campo_modelo_receita_cont).to_be_visible()
    campo_modelo_receita_cont.scroll_into_view_if_needed()
    campo_modelo_receita_cont.wait_for(state="visible", timeout=3000)
    campo_modelo_receita_cont.click()
    log.info("Abriu o popup do item Modelo de Receita Continua")

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_modelo_receita_cont = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_modelo_receita_cont).to_be_visible(timeout=5000)
    expect(popup_modelo_receita_cont.get_by_role("textbox")).to_be_visible()
    popup_modelo_receita_cont.get_by_role("textbox").fill("RECEITUARIO USO CONTINUO - A4 - SEPARADA AO MEIO")
    expect(popup_modelo_receita_cont.get_by_text("RECEITUARIO USO CONTINUO - A4 - SEPARADA AO MEIO", exact=True)).to_be_visible()
    popup_modelo_receita_cont.get_by_text("RECEITUARIO USO CONTINUO - A4 - SEPARADA AO MEIO", exact=True).click()
    expect(popup_modelo_receita_cont).to_be_hidden()
    log.info("Vinculado o modelo RECEITUARIO USO CONTINUO - A4 - SEPARADA AO MEIO ao item Modelo de Receita Continua.")
    
    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    log.info("Alterações salvas com sucesso.")

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_consulta_solicitacao(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção de 'Solicitação de exame' em Consultas.

    O teste realiza as seguintes ações:
    1. Realiza o login no sistema com o perfil de cliente especificado.
    2. Navega até a tela de 'Parâmetros'.
    3. Acessa a seção 'Consulta' e, em seguida, 'Solicitação de exame'.
    4. Modifica os modelos de solicitação de exames, incluindo 'Modelo de Solicitação de Exames' e 'Modelo de Reimpressão'.
    5. Salva as alterações e verifica se a mensagem de sucesso é exibida.

    Args:
        logar_usuario_certa: Fixture para fazer o login do usuário.
        perfil_cliente: O perfil do cliente a ser usado no teste.
    """
    
    log.info(f"Iniciando teste de parâmetros de Consulta - Solicitação de exame para o perfil: {perfil_cliente}")
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Usuário {cliente_teste.cpf} logado.")

    # Pesquisa por "Parâmetros" no menu do sistema.
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Clica no item de menu "Parâmetros" para abrir a tela de configuração.
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    log.info("Navegou para a página Parâmetros")
    
    # --- Seção: Consultas -> Solicitacao de exame ---
    # Acessa a aba 'Consulta' e rola até a seção 'Solicitacao de exame'.
    page.locator("div.dx-list-item:has-text('Consulta')").click()
    log.info("Acessou a aba 'Consulta'.")
    page.get_by_text('Solicitacao de Exame', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Solicitacao de Exame', exact=True)).to_be_visible()
    log.info("Esperou o agrupamento Solicitacao de Exame estar visível.")
    
    # 1. Modifica o "Modelo de Solicitacao de Exames".
    campo_solicitacao_exame = page.get_by_label("Modelo de Solicitação de Exames", exact=True)
    expect(campo_solicitacao_exame).to_be_visible()
    campo_solicitacao_exame.scroll_into_view_if_needed()
    campo_solicitacao_exame.wait_for(state="visible", timeout=3000)
    campo_solicitacao_exame.click()
    log.info("Abriu o popup do item Modelo de Solicitação de Exames")

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_solicitacao_exame = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_solicitacao_exame).to_be_visible(timeout=5000)
    expect(popup_solicitacao_exame.get_by_role("textbox")).to_be_visible()
    popup_solicitacao_exame.get_by_role("textbox").fill("SOLICITAÇÃO DE EXAMES - A5")
    expect(popup_solicitacao_exame.get_by_text("SOLICITAÇÃO DE EXAMES - A5", exact=True)).to_be_visible()
    popup_solicitacao_exame.get_by_text("SOLICITAÇÃO DE EXAMES - A5", exact=True).click()
    expect(popup_solicitacao_exame).to_be_hidden()
    log.info("Vinculado o modelo SOLICITAÇÃO DE EXAMES - A5 ao item Modelo de Solicitação de Exames.")
    
    # 2. Modifica o "Modelo de Reimpressão Solicitação de Exames".
    campo_solicitacao_exame_reim = page.get_by_label("Modelo de Reimpressão Solicitação de Exames", exact=True)
    expect(campo_solicitacao_exame_reim).to_be_visible()
    campo_solicitacao_exame_reim.scroll_into_view_if_needed()
    campo_solicitacao_exame_reim.wait_for(state="visible", timeout=3000)
    campo_solicitacao_exame_reim.click()
    log.info("Abriu o popup do item Modelo de Reimpressão Solicitação de Exames")

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_solicitacao_exame_reim = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_solicitacao_exame_reim).to_be_visible(timeout=5000)
    expect(popup_solicitacao_exame_reim.get_by_role("textbox")).to_be_visible()
    popup_solicitacao_exame_reim.get_by_role("textbox").fill("SOLICITAÇÃO DE EXAMES REIMPRESSÃO - A4")
    expect(popup_solicitacao_exame_reim.get_by_text("SOLICITAÇÃO DE EXAMES REIMPRESSÃO - A4", exact=True)).to_be_visible()
    popup_solicitacao_exame_reim.get_by_text("SOLICITAÇÃO DE EXAMES REIMPRESSÃO - A4", exact=True).click()
    expect(popup_solicitacao_exame_reim).to_be_hidden()
    log.info("Vinculado o modelo SOLICITAÇÃO DE EXAMES REIMPRESSÃO - A4 ao item Modelo de Reimpressão Solicitação de Exames.")
    
    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    log.info("Alterações salvas com sucesso.")

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_consulta_encaminhamento(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção de 'Encaminhamento Médico' em Consultas.

    O teste realiza as seguintes ações:
    1. Realiza o login no sistema com o perfil de cliente especificado.
    2. Navega até a tela de 'Parâmetros'.
    3. Acessa a seção 'Consulta' e, em seguida, 'Encaminhamento Médico'.
    4. Modifica o 'Modelo de Encaminhamento'.
    5. Salva as alterações e verifica se a mensagem de sucesso é exibida.

    Args:
        logar_usuario_certa: Fixture para fazer o login do usuário.
        perfil_cliente: O perfil do cliente a ser usado no teste.
    """
    
    log.info(f"Iniciando teste de parâmetros de Consulta - Encaminhamento Médico para o perfil: {perfil_cliente}")
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Usuário {cliente_teste.cpf} logado.")

    # Pesquisa por "Parâmetros" no menu do sistema.
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Clica no item de menu "Parâmetros" para abrir a tela de configuração.
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    log.info("Navegou para a página Parâmetros")
    
    # --- Seção: Consultas -> Encaminhamento Médico ---
    # Acessa a aba 'Consulta' e rola até a seção 'Encaminhamento Médico'.
    page.locator("div.dx-list-item:has-text('Consulta')").click()
    log.info("Acessou a aba 'Consulta'.")
    page.get_by_text('Encaminhamento Médico', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Encaminhamento Médico', exact=True)).to_be_visible()
    log.info("Esperou o agrupamento Encaminhamento Médico estar visível.")
    
    # 1. Modifica o "Modelo de Encaminhamento".
    campo_modelo_encaminhamento = page.get_by_label("Modelo de Encaminhamento", exact=True)
    expect(campo_modelo_encaminhamento).to_be_visible()
    campo_modelo_encaminhamento.scroll_into_view_if_needed()
    campo_modelo_encaminhamento.wait_for(state="visible", timeout=3000)
    campo_modelo_encaminhamento.click()
    log.info("Abriu o popup do item Modelo de Encaminhamento")

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_modelo_encaminhamento = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_modelo_encaminhamento).to_be_visible(timeout=5000)
    expect(popup_modelo_encaminhamento.get_by_role("textbox")).to_be_visible()
    popup_modelo_encaminhamento.get_by_role("textbox").fill("ENCAMINHAMENTO PARA ESPECIALIDADES - A4")
    expect(popup_modelo_encaminhamento.get_by_text("ENCAMINHAMENTO PARA ESPECIALIDADES - A4", exact=True)).to_be_visible()
    popup_modelo_encaminhamento.get_by_text("ENCAMINHAMENTO PARA ESPECIALIDADES - A4", exact=True).click()
    expect(popup_modelo_encaminhamento).to_be_hidden()
    log.info("Vinculado o modelo ENCAMINHAMENTO PARA ESPECIALIDADES - A4 ao item Modelo de Encaminhamento.")
    
    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    log.info("Alterações salvas com sucesso.")
 
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_consulta_solicitacao_retorno(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção de 'Solicitação de Retorno' em Consultas.

    O teste realiza as seguintes ações:
    1. Realiza o login no sistema com o perfil de cliente especificado.
    2. Navega até a tela de 'Parâmetros'.
    3. Acessa a seção 'Consulta' e, em seguida, 'Solicitação de Retorno'.
    4. Modifica o 'Modelo de Retorno'.
    5. Salva as alterações e verifica se a mensagem de sucesso é exibida.

    Args:
        logar_usuario_certa: Fixture para fazer o login do usuário.
        perfil_cliente: O perfil do cliente a ser usado no teste.
    """
    
    log.info(f"Iniciando teste de parâmetros de Consulta - Solicitação de Retorno para o perfil: {perfil_cliente}")
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Usuário {cliente_teste.cpf} logado.")

    # Pesquisa por "Parâmetros" no menu do sistema.
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Clica no item de menu "Parâmetros" para abrir a tela de configuração.
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    log.info("Navegou para a página Parâmetros")
    
    # --- Seção: Consultas -> Solicitação de Retorno ---
    # Acessa a aba 'Consulta' e rola até a seção 'Solicitação de Retorno'.
    page.locator("div.dx-list-item:has-text('Consulta')").click()
    log.info("Acessou a aba 'Consulta'.")
    page.get_by_text('Solicitação de Retorno', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Solicitação de Retorno', exact=True)).to_be_visible()
    log.info("Esperou o agrupamento Solicitação de Retorno estar visível.")
    
    # 1. Modifica o "Modelo de Retorno".
    campo_solicitacao_retorno = page.get_by_label("Modelo de Retorno", exact=True)
    expect(campo_solicitacao_retorno).to_be_visible()
    campo_solicitacao_retorno.scroll_into_view_if_needed()
    campo_solicitacao_retorno.wait_for(state="visible", timeout=3000)
    campo_solicitacao_retorno.click()
    log.info("Abriu o popup do item Modelo de Retorno")

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_solitacao_retorno = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_solitacao_retorno).to_be_visible(timeout=5000)
    expect(popup_solitacao_retorno.get_by_role("textbox")).to_be_visible()
    popup_solitacao_retorno.get_by_role("textbox").fill("SOLICITAÇÃO DE RETORNO - A4")
    expect(popup_solitacao_retorno.get_by_text("SOLICITAÇÃO DE RETORNO - A4", exact=True)).to_be_visible()
    popup_solitacao_retorno.get_by_text("SOLICITAÇÃO DE RETORNO - A4", exact=True).click()
    expect(popup_solitacao_retorno).to_be_hidden()
    log.info("Vinculado o modelo SOLICITAÇÃO DE RETORNO - A4 ao item Modelo de Retorno.")
    
    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    log.info("Alterações salvas com sucesso.")
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_consulta_orientacao(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção de 'Orientações' em Consultas.

    O teste realiza as seguintes ações:
    1. Realiza o login no sistema com o perfil de cliente especificado.
    2. Navega até a tela de 'Parâmetros'.
    3. Acessa a seção 'Consulta' e, em seguida, 'Orientações'.
    4. Modifica o 'Modelo de orientação'.
    5. Salva as alterações e verifica se a mensagem de sucesso é exibida.

    Args:
        logar_usuario_certa: Fixture para fazer o login do usuário.
        perfil_cliente: O perfil do cliente a ser usado no teste.
    """
    
    log.info(f"Iniciando teste de parâmetros de Consulta - Orientações para o perfil: {perfil_cliente}")
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Usuário {cliente_teste.cpf} logado.")

    # Pesquisa por "Parâmetros" no menu do sistema.
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Clica no item de menu "Parâmetros" para abrir a tela de configuração.
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    log.info("Navegou para a página Parâmetros")
    
    # --- Seção: Consultas -> Orientações ---
    # Acessa a aba 'Consulta' e rola até a seção 'Orientações'.
    page.locator("div.dx-list-item:has-text('Consulta')").click()
    log.info("Acessou a aba 'Consulta'.")
    page.get_by_text('Orientações', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Orientações', exact=True)).to_be_visible()
    log.info("Esperou o agrupamento Orientações estar visível.")
    
    # 1. Modifica o "Modelo de Orientações".
    campo_orientacoes = page.get_by_label("Modelo de orientação", exact=True)
    expect(campo_orientacoes).to_be_visible()
    campo_orientacoes.scroll_into_view_if_needed()
    campo_orientacoes.wait_for(state="visible", timeout=3000)
    campo_orientacoes.click()
    log.info("Abriu o popup do item Modelo de Orientações")

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_orientacoes = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_orientacoes).to_be_visible(timeout=5000)
    expect(popup_orientacoes.get_by_role("textbox")).to_be_visible()
    popup_orientacoes.get_by_role("textbox").fill("ORIENTAÇÃO DA CONSULTA - A4")
    expect(popup_orientacoes.get_by_text("ORIENTAÇÃO DA CONSULTA - A4", exact=True)).to_be_visible()
    popup_orientacoes.get_by_text("ORIENTAÇÃO DA CONSULTA - A4", exact=True).click()
    expect(popup_orientacoes).to_be_hidden()
    log.info("Vinculado o modelo ORIENTAÇÃO DA CONSULTA - A4 ao item Modelo de Orientações.")
    
    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    log.info("Alterações salvas com sucesso.")
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_consulta_prontuario(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção de 'Prontuário' em Consultas.

    O teste realiza as seguintes ações:
    1. Realiza o login no sistema com o perfil de cliente especificado.
    2. Navega até a tela de 'Parâmetros'.
    3. Acessa a seção 'Consulta' e, em seguida, 'Prontuário'.
    4. Modifica o 'Modelo de prontuario'.
    5. Salva as alterações e verifica se a mensagem de sucesso é exibida.

    Args:
        logar_usuario_certa: Fixture para fazer o login do usuário.
        perfil_cliente: O perfil do cliente a ser usado no teste.
    """
    
    log.info(f"Iniciando teste de parâmetros de Consulta - Prontuário para o perfil: {perfil_cliente}")
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Usuário {cliente_teste.cpf} logado.")

    # Pesquisa por "Parâmetros" no menu do sistema.
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Clica no item de menu "Parâmetros" para abrir a tela de configuração.
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    log.info("Navegou para a página Parâmetros")
    
    # --- Seção: Consultas -> Prontuário ---
    # Acessa a aba 'Consulta' e rola até a seção 'Prontuário'.
    page.locator("div.dx-list-item:has-text('Consulta')").click()
    log.info("Acessou a aba 'Consulta'.")
    page.get_by_text('Prontuário', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Prontuário', exact=True)).to_be_visible()
    log.info("Esperou o agrupamento Prontuário estar visível.")
    
    # 1. Modifica o "Modelo de prontuario".
    campo_prontuario = page.get_by_label("Modelo de prontuario", exact=True)
    expect(campo_prontuario).to_be_visible()
    campo_prontuario.scroll_into_view_if_needed()
    campo_prontuario.wait_for(state="visible", timeout=3000)
    campo_prontuario.click()
    log.info("Abriu o popup do item Modelo de prontuario")

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_prontuario = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_prontuario).to_be_visible(timeout=5000)
    expect(popup_prontuario.get_by_role("textbox")).to_be_visible()
    popup_prontuario.get_by_role("textbox").fill("PRONTUÁRIO - A4")
    expect(popup_prontuario.get_by_text("PRONTUÁRIO - A4", exact=True)).to_be_visible()
    popup_prontuario.get_by_text("PRONTUÁRIO - A4", exact=True).click()
    expect(popup_prontuario).to_be_hidden()
    log.info("Vinculado o modelo PRONTUÁRIO - A4 ao item Modelo de prontuario.")
    
    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    log.info("Alterações salvas com sucesso.")
    
@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
def test_modificar_parametros_consulta_comprovanteagendamento(logar_usuario_certa, perfil_cliente):
    """
    Testa a modificação de parâmetros na seção de 'Comprovante de agendamento' em Consultas.

    O teste realiza as seguintes ações:
    1. Realiza o login no sistema com o perfil de cliente especificado.
    2. Navega até a tela de 'Parâmetros'.
    3. Acessa a seção 'Consulta' e, em seguida, 'Comprovante de agendamento'.
    4. Modifica o 'Modelo Comprovante Agendamento'.
    5. Salva as alterações e verifica se a mensagem de sucesso é exibida.

    Args:
        logar_usuario_certa: Fixture para fazer o login do usuário.
        perfil_cliente: O perfil do cliente a ser usado no teste.
    """
    
    log.info(f"Iniciando teste de parâmetros de Consulta - Comprovante de agendamento para o perfil: {perfil_cliente}")
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Usuário {cliente_teste.cpf} logado.")

    # Pesquisa por "Parâmetros" no menu do sistema.
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Parâmetros", delay=100)
    
    # Clica no item de menu "Parâmetros" para abrir a tela de configuração.
    item_parametro = page.get_by_text("Parâmetros", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    log.info("Navegou para a página Parâmetros")
    
    # --- Seção: Consultas -> Comprovante de agendamento ---
    # Acessa a aba 'Consulta' e rola até a seção 'Comprovante de agendamento'.
    page.locator("div.dx-list-item:has-text('Consulta')").click()
    log.info("Acessou a aba 'Consulta'.")
    page.get_by_text('Comprovante de agendamento', exact=True).scroll_into_view_if_needed()
    expect(page.get_by_text('Comprovante de agendamento', exact=True)).to_be_visible()
    log.info("Esperou o agrupamento Comprovante de agendamento estar visível.")
    
    # 1. Modifica o "Modelo Comprovante de agendamento".
    campo_comp_agendamento = page.get_by_label("Modelo Comprovante Agendamento", exact=True)
    expect(campo_comp_agendamento).to_be_visible()
    campo_comp_agendamento.scroll_into_view_if_needed()
    campo_comp_agendamento.wait_for(state="visible", timeout=3000)
    campo_comp_agendamento.click()
    log.info("Abriu o popup do item Modelo Comprovante de agendamento")

    # Aguarda o popup de seleção aparecer, preenche e seleciona o modelo.
    popup_comp_agendamento = page.locator(".dx-overlay-content.dx-popup-normal.dx-resizable:visible")
    expect(popup_comp_agendamento).to_be_visible(timeout=5000)
    expect(popup_comp_agendamento.get_by_role("textbox")).to_be_visible()
    popup_comp_agendamento.get_by_role("textbox").fill("CONFIRMAÇÃO DE AGENDAMENTO - FOLHA CONTÍNUA")
    expect(popup_comp_agendamento.get_by_text("CONFIRMAÇÃO DE AGENDAMENTO - FOLHA CONTÍNUA", exact=True)).to_be_visible()
    popup_comp_agendamento.get_by_text("CONFIRMAÇÃO DE AGENDAMENTO - FOLHA CONTÍNUA", exact=True).click()
    expect(popup_comp_agendamento).to_be_hidden()
    log.info("Vinculado o modelo CONFIRMAÇÃO DE AGENDAMENTO - FOLHA CONTÍNUA ao item Modelo Comprovante de agendamento.")
    
    # Salva as alterações e verifica a mensagem de sucesso.
    page.get_by_role("button", name="Salvar").click()
    expect(page.get_by_text("sucesso")).to_be_visible()
    log.info(f"A pagina com as alterações previstas foram salvas. Teste Consulta com o perfil {cliente_teste.cpf} na unidade {cliente_teste.unidade} foi concluído.")