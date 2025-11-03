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

    # Lista de todos os grupos de relatórios
    grupos = [
        "Agendamento", "Atendimentos", "Atestado", "Auxilios", "Cadastrais",
        "Comprovante Medicamentos", "Encaminhamento para especialidades",
        "Etiqueta medicamento", "HORUS", "Medicamentos / Materiais",
        "Orientações", "Outros Procedimentos", "Parecer", "Posologia",
        "Prontuário", "Receituário", "Roteiro Veículos",
        "Roteiro Veículos Comprovante", "Solicitação de exame",
        "Solicitação de retorno", "TFD"
    ]

    # Itera sobre cada grupo para garantir que todos os relatórios sejam carregados
    for grupo in grupos:
        # Espera o grupo estar visível, rolando se necessário
        group_locator = page.get_by_text(f"Grupo: {grupo}", exact=True)
        group_locator.scroll_into_view_if_needed()
        expect(group_locator).to_be_visible()

    # Depois de percorrer todos os grupos, todos os botões de download devem estar presentes no DOM
    download_buttons = page.locator('a[title="Download"]').all()

    # Itera sobre todos os botões de download e clica em cada um
    for button in download_buttons:
        button.scroll_into_view_if_needed()
        button.click()
        
        popup = page.locator(".dx-overlay-content:has-text('Confirma o Download?'):visible")
        expect(popup).to_be_visible()
        popup.get_by_role("button", name="Sim").click()
        expect(popup).to_be_hidden()