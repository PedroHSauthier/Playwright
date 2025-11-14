from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes
from models.individuo import carregar_cpf_individuos, carregar_dados_individuo_por_cpf
import logging
import re

log = logging.getLogger()

cliente = ["homologacao", "admin"]
parametros_individuais = ["completo", "urussanga"]

@pytest.mark.parametrize('perfil_cliente', carregar_nomes_clientes(cliente))
@pytest.mark.parametrize('cpf_especificado', carregar_cpf_individuos(parametros_individuais))
def inativo_test_cadastro_Profissional_Completo_Admin_Odonto(logar_usuario_certa, perfil_cliente, cpf_especificado):
        
    individuo_especificado = carregar_dados_individuo_por_cpf(cpf_especificado, parametros_individuais)
    
    log.info(f"Perfil: {perfil_cliente}, cliente: {individuo_especificado.identificacao.get('Nome')}, cpf_especificado: {cpf_especificado}")
    
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Logado no sistema com o perfil: {perfil_cliente}")
    
    menu = page.locator("#menusistema")
    log.info("Navegando para a tela de Profissionais do sistema.")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Profissionais", delay=100)
    
    item_parametro = page.get_by_text("Profissionais", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    log.debug("Tela de Profissionais aberta.")
    
    expect(page.get_by_text("Inserir")).to_be_visible()
    page.get_by_text("Inserir").click()
    expect(page.get_by_text("Inserindo")).to_be_visible()
    log.info("Acessado a tela de inserção de novo profissional.")
    
    # =========================================================================================================== #
    # Preenchimento dos dados de identificação.
    # =========================================================================================================== #
    page.get_by_role("textbox", name="Nome completo").fill(individuo_especificado.identificacao.get("Nome"))
    log.debug("Nome completo preenchido.")
    
    page.get_by_role("textbox", name="CPF").fill(individuo_especificado.identificacao.get("CPF"))
    log.debug("CPF Preenchido.")

    campo_cns = page.get_by_role('textbox', name='CNS')
    campo_cns.click()           # Dá foco no campo
    for _ in range(15):         # A CNS tem 15 dígitos
        campo_cns.press("Backspace")
    page.get_by_role('textbox', name='CNS').press_sequentially(individuo_especificado.identificacao.get("CNS"), delay=5)
    log.debug("CNS Preenchido.")
    
    page.get_by_role("combobox", name="Data de Nascimento").press_sequentially(individuo_especificado.identificacao.get("DataNasc"), delay=30)
    log.debug("Data de nascimento preenchido.")
    
    page.get_by_role("combobox", name="Sexo").click()
    page.get_by_text(individuo_especificado.identificacao.get("Sexo")).click()
    log.debug("Sexo preenchido.")
    
    page.get_by_role("textbox", name="Telefone").press_sequentially(individuo_especificado.identificacao.get("TelefoneCelular"))
    log.debug("Telefone preenchido.")
    
    page.get_by_role("textbox", name="E-Mail").fill(individuo_especificado.identificacao.get("Email"))
    log.debug("Email preenchido.")
    
    page.get_by_role("combobox", name="Data de Início").press_sequentially(individuo_especificado.Profissional.get("Inicio"))
    log.debug("Data de inicio preenchido.")
    
    page.get_by_role("combobox", name="Categoria CBO").click()
    page.keyboard.type(individuo_especificado.Profissional.get("Categoria_CBO"))
    page.get_by_text(individuo_especificado.Profissional.get("Categoria_CBO")).click()
    log.debug("Categoria CBO preenchida.")
    
    page.get_by_role("textbox", name="Senha").fill(individuo_especificado.Profissional.get("Senha"))
    log.debug("Senha preenchida.")
    log.info("Informações de identificação todas preenchidas, seguindo para dados de endereço.")
    
    if individuo_especificado.Profissional.get("Ativo") == True:
        page.get_by_role("checkbox", name="Ativo").click()
        log.info("Usuário ativado.")
    else:
        log.info("Usuário se mantém inativo.")
        
    #================================================================================== #
    # Preenchimento dos dados de endereço.
    #================================================================================== #
    
    cep_box = page.get_by_role("textbox", name="CEP")
    for _ in range(10):
        cep_box.press("Backspace")
    cep_box.press_sequentially(individuo_especificado.VinculoDomiciliar.get("CEP"))
    page.get_by_label("map-marker").click()

    # MUNICIPIO VALIDACAO
    expect(page.get_by_role("combobox", name="Município")).not_to_contain_text("Selecione ...")
    municipio_text = page.get_by_role("combobox", name="Município").text_content()
    if municipio_text != "":
        if municipio_text == individuo_especificado.VinculoDomiciliar.get("Municipio"):
            log.info(f"Município preenchido com {municipio_text} corretamente com apenas o CEP.")
        else:
            log.warning(f"Município preenchido com: {municipio_text}, mas diferente do registro: {individuo_especificado.VinculoDomiciliar.get("Municipio")}.")
            page.get_by_role("combobox", name="Município").click()
            page.keyboard.type(individuo_especificado.VinculoDomiciliar.get("Municipio"))
            page.get_by_text(individuo_especificado.VinculoDomiciliar.get("Municipio")).click()
    else:
        log.warning("CEP ou está invalído, ou o botão de pesquisa falhou, iniciando callback e puxando dados do individuo.")
        page.get_by_role("combobox", name="Município").click()
        page.keyboard.type(individuo_especificado.VinculoDomiciliar.get("Municipio"))
        page.get_by_text(individuo_especificado.VinculoDomiciliar.get("Municipio")).click()
    expect(page.get_by_role("combobox", name="Município")).to_contain_text(individuo_especificado.VinculoDomiciliar.get("Municipio"))
    log.info("Municipio verificado ou tratado.")

    #LOGRADOURO NOME VALIDAÇÃO
    logradouro_text = page.get_by_role("textbox", name="Logradouro nome").input_value()
    if logradouro_text != "":
        if logradouro_text == individuo_especificado.VinculoDomiciliar.get("Logradouro"):
            log.info(f"Logradouro nome preenchido com {logradouro_text} corretamente com apenas o CEP.")
        else:
            log.warning(f"Logradouro preenchido com: {logradouro_text}, mas diferente do registro: {individuo_especificado.VinculoDomiciliar.get("Logradouro")}.")
            
            page.get_by_role("textbox", name="Logradouro nome").clear()
            page.keyboard.type(individuo_especificado.VinculoDomiciliar.get("Logradouro"))
    else:
        log.warning("CEP ou está invalído, ou o botão de pesquisa falhou, iniciando callback e puxando dados do individuo.")
        page.get_by_role("textbox", name="Logradouro nome").click()
        page.keyboard.type(individuo_especificado.VinculoDomiciliar.get("Logradouro"))
    expect(page.get_by_role("textbox", name="Logradouro nome")).to_have_value(individuo_especificado.VinculoDomiciliar.get("Logradouro"))
    log.info("Logradouro verificado ou tratado.")
    
    #BAIRRO NOME VALIDAÇÃO
    bairro_text = page.get_by_role("textbox", name="Bairro nome").input_value()
    if bairro_text != "":
        if bairro_text == individuo_especificado.VinculoDomiciliar.get("Bairro"):
            log.info(f"Bairro nome preenchido com {bairro_text} corretamente com apenas o CEP.")
        else:
            log.warning(f"Bairro preenchido com: {bairro_text}, mas diferente do registro: {individuo_especificado.VinculoDomiciliar.get("Bairro")}.")
            
            page.get_by_role("textbox", name="Bairro nome").clear()
            page.keyboard.type(individuo_especificado.VinculoDomiciliar.get("Bairro"))
    else:
        log.warning("CEP ou está invalído, ou o botão de pesquisa falhou, iniciando callback e puxando dados do individuo.")
        page.get_by_role("textbox", name="Bairro nome").click()
        page.keyboard.type(individuo_especificado.VinculoDomiciliar.get("Bairro"))
    expect(page.get_by_role("textbox", name="Bairro nome")).to_have_value(individuo_especificado.VinculoDomiciliar.get("Bairro"))
    log.info("Bairro verificado ou tratado.")
    
    # NUMERO
    if individuo_especificado.VinculoDomiciliar.get("Numero") == "":
        page.get_by_role("checkbox", name="Sem número").click()
        log.info("Sem número acionado. Sem número no cadastro do individuo atual.")
    else:
        page.get_by_role("spinbutton", name="Número").press_sequentially(individuo_especificado.VinculoDomiciliar.get("Numero"))
        log.info("Numero verificado e preenchido.")
    
    page.get_by_role("textbox", name="Complemento").fill(individuo_especificado.VinculoDomiciliar.get("Complemento"))
    
    page.get_by_role("textbox", name="Ponto de referência").fill(individuo_especificado.VinculoDomiciliar.get("Referencia"))
    
    page.get_by_role("textbox", name="Latitude").fill(individuo_especificado.VinculoDomiciliar.get("Latitude"))
    
    page.get_by_role("textbox", name="Longitude").fill(individuo_especificado.VinculoDomiciliar.get("Longitude"))
    log.info("Dados opcionais de endereço, preenchidos com os dados do usuário, caso vazios mantidos assim.")
    log.info("Campos de endereço, finalizados.")
    
    #================================================================================== #
    # Preenchimento dos dados de lotação.
    #================================================================================== #
    
    
    
    for i, lotacao in enumerate(individuo_especificado.Profissional.get("Lotacoes")):
        page.get_by_role("button", name="Inserir").first.click()
        log.info(f"Aberto o modal de inserção de lotação, para a lotação: {i+1}°")
        
        page.get_by_role("combobox", name="Estabelecimento do Atendimento").click()
        page.keyboard.type(lotacao.get("EstabelecimentoAtendimento"))
        page.get_by_role("option", name=lotacao.get("EstabelecimentoAtendimento")).first.click()
        expect(page.get_by_role("combobox", name="Estabelecimento do Atendimento")).not_to_be_empty()
        estabelecimentoAtendimento = page.get_by_role("combobox", name="Estabelecimento do Atendimento").text_content()
        log.debug(f"Estabelecimento atendimento preenchido, com {estabelecimentoAtendimento}")
        
        page.get_by_role("combobox", name="Equipe de Atendimento").click()
        page.keyboard.type(lotacao.get("EquipeAtendimento"))
        page.get_by_role("option", name=lotacao.get("EquipeAtendimento")).first.click()
        expect(page.get_by_role("combobox", name="Equipe de Atendimento")).not_to_be_empty()
        equipeAtendimento = page.get_by_role("combobox", name="Equipe de Atendimento").text_content()
        log.debug(f"Equipe atendimento preenchido, com {equipeAtendimento}")
        
        page.get_by_role("combobox", name="Estabelecimento de Faturamento").click()
        page.keyboard.type(lotacao.get("EstabelecimentoFaturamento"))
        page.get_by_role("option", name=lotacao.get("EstabelecimentoFaturamento")).first.click()
        expect(page.get_by_role("combobox", name="Estabelecimento de Faturamento")).not_to_be_empty()
        estabelecimentoFaturamento = page.get_by_role("combobox", name="Estabelecimento de Faturamento").text_content()
        log.debug(f"Estabelecimento faturamento preenchido, com {estabelecimentoFaturamento}")
        
        page.get_by_role("combobox", name="Equipe de Faturamento").click()
        page.keyboard.type(lotacao.get("EquipeFaturamento"))
        page.get_by_role("option", name=lotacao.get("EquipeFaturamento")).first.click()
        expect(page.get_by_role("combobox", name="Equipe de Faturamento")).not_to_be_empty()
        equipeFaturamento = page.get_by_role("combobox", name="Equipe de Faturamento").text_content()
        log.debug(f"Equipe faturamento preenchido, com {equipeFaturamento}")
        
        page.get_by_role("combobox", name="Horário").click()
        page.keyboard.type(lotacao.get("Horario"))
        page.get_by_role("option", name=lotacao.get("Horario")).first.click()
        expect(page.get_by_role("combobox", name="Horário")).not_to_be_empty()
        Horario = page.get_by_role("combobox", name="Horário").text_content()
        log.debug(f"Horário preenchido, com {Horario}")
        
        page.get_by_role("combobox", name="CBO", exact=True).click()
        page.keyboard.type(lotacao.get("CBO"))
        page.get_by_role("option", name=lotacao.get("CBO")).first.click()
        expect(page.get_by_role("combobox", name="CBO", exact=True)).not_to_be_empty()
        CBO = page.get_by_role("combobox", name="CBO", exact=True).text_content()
        log.debug(f"CBO preenchido, com {CBO}")
        
        page.get_by_role("textbox", name="Microárea").fill(lotacao.get("Microarea"))
        if page.get_by_role("textbox", name="Microárea").input_value() == "":
            log.warning("Sem microárea no registro.")
        if page.get_by_role("textbox", name="Microárea").input_value() != "":
            log.debug(f"Microárea definida como {page.get_by_role("textbox", name="Microárea").input_value()}")
            
        page.get_by_role("combobox", name="Tipo conselho").click()
        page.keyboard.type(lotacao.get("Conselho"))
        page.get_by_role("option", name=lotacao.get("Conselho")).first.click()
        expect(page.get_by_role("combobox", name="Tipo conselho")).not_to_be_empty()
        tipoConselho = page.get_by_role("combobox", name="Tipo conselho").text_content()
        log.debug(f"Tipo conselho preenchido, com {tipoConselho}")
        
        page.get_by_role("combobox", name="Estado conselho").click()
        page.keyboard.type(individuo_especificado.DocumentosPessoais.get("EstadoCarteiraTrabalho"))
        page.get_by_role("option", name=individuo_especificado.DocumentosPessoais.get("EstadoCarteiraTrabalho")).first.click()
        expect(page.get_by_role("combobox", name="Estado conselho")).not_to_be_empty()
        EstadoConselho = page.get_by_role("combobox", name="Estado conselho").text_content()
        log.debug(f"Estado conselho preenchido, com {EstadoConselho}")
    
        page.get_by_role("textbox", name="Número Conselho").fill(lotacao.get("NumeroConselho"))
        if page.get_by_role("textbox", name="Número Conselho").input_value() == "":
            log.warning("Sem Número Conselho no registro.")
        if page.get_by_role("textbox", name="Número Conselho").input_value() != "":
            log.debug(f"Número Conselho definida como {page.get_by_role("textbox", name="Número Conselho").input_value()}")
            
        page.get_by_role("textbox", name="Número RQE").fill(lotacao.get("RQE"))
        if page.get_by_role("textbox", name="Número RQE").input_value() == "":
            log.warning("Sem Número RQE no registro.")
        if page.get_by_role("textbox", name="Número RQE").input_value() != "":
            log.debug(f"Número RQE definida como {page.get_by_role("textbox", name="Número RQE").input_value()}")
            
        page.get_by_role("combobox", name="Procedimento").click()
        page.keyboard.type(lotacao.get("Procedimento"))
        page.get_by_role("option", name=lotacao.get("Procedimento")).first.click()
        expect(page.get_by_role("combobox", name="Procedimento")).not_to_be_empty()
        Procedimento = page.get_by_role("combobox", name="Procedimento").text_content()
        log.debug(f"Procedimento preenchido, com {Procedimento}")
        
        for perfil in lotacao.get("PerfisDeAcesso"):
            perfilMenu = page.locator("dx-dropdowneditor-overlay-flipped").filter(has_text="Perfil de Acesso")
            page.get_by_role("combobox", name="Perfil de Acesso").click()
            expect(page.get_by_text("Selecionar todos")).to_be_visible()
            option_locator = page.get_by_role("option").filter(has_text=re.compile(f"^{perfil}$", re.IGNORECASE))
            option_locator.click()
            expect(perfilMenu).to_be_hidden()
            
            perfis = page.locator('[id-test="searchPerfil"]')
            tagsperfis = perfis.locator(".dx-tag-content span")
            expect(tagsperfis.filter(has_text=perfil)).to_be_visible()
            texttags = tagsperfis.all_text_contents()
            log.info(f"Associado ao profissional no momento: {texttags}")
        
        if lotacao.get("GeraEsus") == True:
            page.get_by_role("checkbox", name="Gera Esus").click()
            log.info("Gera Esus ativado.")
        else:
            log.debug("Gera Esus ignorado.")
            
        if lotacao.get("VisualizaProntuario") == True:
            page.get_by_role("checkbox", name="Visualiza prontuário").click()
            log.info("Visualiza Prontuário ativado.")
        else:
            log.debug("Visualiza Prontuário ignorado.")
            
        if lotacao.get("Telesaude") == True:
            page.get_by_role("checkbox", name="TeleSaude").click()
            log.info("TeleSaude ativado.")
        else:
            log.debug("TeleSaude ignorado.")
            
        if lotacao.get("Ativo") == True:
            page.get_by_role("checkbox", name="Ativo").nth(1).click()
            log.info("Lotação ativada.")
        else:
            log.debug("Lotação ignorada.")
    
        page.get_by_role("button", name="Salvar e Fechar").click()
        expect(page.get_by_text("Inserindo Lotações")).to_be_hidden()
        
    for exame in individuo_especificado.Profissional.get("GrupoDeExame"):
        page.get_by_role("button", name="Inserir").nth(1).click()
        expect(page.get_by_text("Inserindo Grupo de exame", exact=True)).to_be_visible()
        page.get_by_role("combobox", name="Grupo Exame").click()
        page.keyboard.type(exame)
        page.get_by_role("option", name=exame).click()
        log.info(f"Exame associado: {page.get_by_role("combobox", name="Grupo Exame").text_content()}")
        page.get_by_role("button", name="Salvar e Fechar").click()
        
    page.get_by_role("button", name="Salvar", exact=True).click()

@pytest.mark.parametrize('perfil_cliente', carregar_nomes_clientes(cliente))
@pytest.mark.parametrize('cpf_especificado', carregar_cpf_individuos(parametros_individuais))
def test_excluir_Profissional_Completo_Admin_Odonto(logar_usuario_certa, perfil_cliente, cpf_especificado):
    
    individuo_especificado = carregar_dados_individuo_por_cpf(cpf_especificado, parametros_individuais)
    
    log.info(f"Perfil: {perfil_cliente}, cliente: {individuo_especificado.identificacao.get('Nome')}, cpf_especificado: {cpf_especificado}")
    
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Logado no sistema com o perfil: {perfil_cliente}")
    
    menu = page.locator("#menusistema")
    log.info("Navegando para a tela de Profissionais do sistema.")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Profissionais", delay=100)
    
    item_parametro = page.get_by_text("Profissionais", exact=True)
    expect(item_parametro).to_be_visible()
    item_parametro.click()
    log.debug("Tela de Profissionais aberta.")
    
    cpf_to_delete = individuo_especificado.identificacao.get("CPF")
    page.get_by_label("Pesquisar na grade de dados").fill(cpf_to_delete)
    log.info(f"Pesquisando pelo CPF: {cpf_to_delete}")
    