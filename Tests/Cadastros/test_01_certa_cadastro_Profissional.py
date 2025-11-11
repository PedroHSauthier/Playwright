from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes
from models.individuo import carregar_cpf_individuos, carregar_dados_individuo_por_cpf
import logging

log = logging.getLogger()

cliente = ["homologacao", "admin"]
parametros_individuais = ["completo"]

@pytest.mark.parametrize('perfil_cliente', carregar_nomes_clientes(cliente))
@pytest.mark.parametrize('cpf_especificado', carregar_cpf_individuos(parametros_individuais))
def test_cadastro_Profissional_Completo_Admin_Odonto(logar_usuario_certa, perfil_cliente, cpf_especificado):
    
    individuo_especificado = carregar_dados_individuo_por_cpf(cpf_especificado)
    
    log.info(f"Perfil: {perfil_cliente}, cliente: {individuo_especificado.identificacao.get('Nome')}, cpf_especificado: {cpf_especificado}")
    
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Logado no sistema com o perfil: {perfil_cliente}")
    
    menu = page.locator("#menusistema")
    log.info("Navegando para a tela de Profissionais do sistema.")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Profissionais", delay=100)