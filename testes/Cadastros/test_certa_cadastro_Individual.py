from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes
from models.individuo import Individuo, carregar_cpf_individuos, carregar_dados_individuo_por_cpf

cliente = ["homologacao", "admin"]
parametros_individuais = ["completo", ]

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes(cliente))
@pytest.mark.parametrize("individuo_cpf", carregar_cpf_individuos())
def test_modificar_individual_cadastro_Teste(logar_usuario_certa, perfil_cliente):
    """
    """
    
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    # A fixture de login recebe o objeto cliente e retorna a página.
    page = logar_usuario_certa(cliente_teste)

    # Pesquisa por "Individual" no menu do sistema para acessar a tela de configuração.
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("Individual", delay=100)
    
    # Clica no item de menu "Individual" para abrir a tela de configuração.
    item_individual = page.get_by_text("Individual", exact=True)
    expect(item_individual).to_be_visible()
    item_individual.click()
    
    