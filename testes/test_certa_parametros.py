from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes())
def test_baixar_relatorios(logar_usuario_certa, perfil_cliente):
    """Realiza a atualização de todos os relatórios da loja para um determinado perfil de cliente.
    Este teste é parametrizado e será executado para todos os perfis em clientes.json.

    Args:
        logar_usuario_certa: Fixture para logar o usuário no sistema.
        perfil_cliente (str): O nome do perfil do cliente a ser testado (injetado pelo pytest).
    """
    
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    
    # A fixture de login recebe o objeto cliente.
    page = logar_usuario_certa(cliente_teste)
    
    print(f"\nExecutando teste para o perfil: {perfil_cliente}")

    # Pesquisar "loja" na tela inicial para encontrar a Loja de Relatórios
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("loja", delay=100)
    
    # Abrir a Loja de Relatórios
    item_loja = page.get_by_text("Loja de Relatorios", exact=True)
    expect(item_loja).to_be_visible()
    item_loja.click()

    # Espera o primeiro grupo de relatórios carregar para garantir que a página está pronta
    expect(page.get_by_text("Grupo: Agendamento")).to_be_visible()
    
    # Obter todos os botões de download da página.
    download_buttons = page.locator('a[title="Download"]').all()

    # Iterar sobre cada botão de download e clicar nele.
    for i, button in enumerate(download_buttons):
        button.click()
        
        # Localizar o popup visível e, dentro dele, clicar no botão "Sim".
        popup = page.locator(".dx-overlay-content:has-text('Confirma o Download?'):visible")
        popup.get_by_role("button", name="Sim").click()
        
        # Esperar explicitamente o popup desaparecer para evitar race conditions.
        expect(popup).to_be_hidden()
        
        print(f"Ação de download confirmada para o relatório {i+1} do perfil {perfil_cliente}")

    page.screenshot(path=f"screenshots/certa/relatorios_baixados_{perfil_cliente}.png")