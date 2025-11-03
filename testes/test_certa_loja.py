from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes("homologacao"))
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
    
    # Contador para os botões de download já processados
    i = 0
    while True:
        # Reavalia a lista de botões de download a cada iteração
        download_buttons = page.locator('a[title="Download"]').all()
        
        # Se não houver mais botões para processar na lista atual, saia do loop
        if i >= len(download_buttons):
            break
            
        # Pega o próximo botão da lista
        button = download_buttons[i]
        
        # Rola a página até que o botão esteja visível
        button.scroll_into_view_if_needed()
        
        # Clica no botão de download
        button.click()
        
        # Localiza o popup de confirmação e clica em "Sim"
        popup = page.locator(".dx-overlay-content:has-text('Confirma o Download?'):visible")
        popup.get_by_role("button", name="Sim").click()
        
        # Espera o popup desaparecer
        expect(popup).to_be_hidden()
        
        # Incrementa o contador para processar o próximo botão na próxima iteração
        i += 1