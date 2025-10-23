from playwright.sync_api import Page, expect
from models.cliente import Cliente

cliente_teste = Cliente.carregar_dados_cliente("cliente_admin_homologacao")

def test_baixar_relatorios(logar_usuario_certa):
    """Realiza a atualização de todos os relatórios considerados de importância no sistema, clicando no botão de download na loja e confirmando a ação.

    Args:
        logar_usuario_certa: Fixture para logar o usuário no sistema.
    """
    
    page = logar_usuario_certa(cliente_teste)
    
    # Pesquisar "loja" na tela inicial para encontrar a Loja de Relatórios
    menu = page.locator("#menusistema")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("loja", delay=50)
    
    # Abrir a Loja de Relatórios
    item_loja = page.get_by_text("Loja de Relatorios", exact=True)
    expect(item_loja).to_be_visible()
    item_loja.click()

    expect(page.get_by_text("Grupo: Agendamento")).to_be_visible()
    # Obter todos os botões de download da página.
    download_buttons = page.locator('a[title="Download"]').all()

    # Iterar sobre cada botão de download e clicar nele.
    for i, button in enumerate(download_buttons):
        button.click()
        
        # Localizar o popup visível e, dentro dele, clicar no botão "Sim".
        # O filtro ':visible' é o critério de desempate para garantir que pegamos o popup ativo.
        popup = page.locator(".dx-overlay-content:has-text('Confirma o Download?'):visible")
        popup.get_by_role("button", name="Sim").click()
        
        expect(popup).to_be_hidden()
        
        print(f"Ação de download confirmada para o relatório {i+1}")

    page.screenshot(path="screenshots/certa/relatorios_baixar.png")