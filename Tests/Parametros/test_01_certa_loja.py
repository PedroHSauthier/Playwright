from playwright.sync_api import expect
import pytest
from models.cliente import Cliente, carregar_nomes_clientes
import logging

log = logging.getLogger(__name__)

@pytest.mark.parametrize("perfil_cliente", carregar_nomes_clientes("homologacao"))
def test_baixar_relatorios(logar_usuario_certa, perfil_cliente):
    """Realiza a atualização de todos os relatórios da loja para um determinado perfil de cliente.
    Este teste é parametrizado e será executado para todos os perfis em clientes.json.

    Args:
        logar_usuario_certa: Fixture para logar o usuário no sistema.
        perfil_cliente (str): O nome do perfil do cliente a ser testado (injetado pelo pytest).
    """
    log.info(f"Iniciando teste de download de relatórios para o perfil: {perfil_cliente}")
    
    # Carrega os dados do cliente a partir do perfil fornecido pelo pytest.
    cliente_teste = Cliente.carregar_dados_cliente(perfil_cliente)
    log.debug(f"Dados do cliente carregados: {cliente_teste.cpf} ({cliente_teste.cpf})")
    
    # A fixture de login recebe o objeto cliente.
    page = logar_usuario_certa(cliente_teste)
    log.info(f"Usuário {cliente_teste.cpf} logado com sucesso.")

    # Pesquisar "loja" na tela inicial para encontrar a Loja de Relatórios
    menu = page.locator("#menusistema")
    log.info("Pesquisando 'loja' no menu do sistema.")
    menu.get_by_role("textbox").click()
    menu.get_by_role("textbox").press_sequentially("loja", delay=100)
    
    # Abrir a Loja de Relatórios
    item_loja = page.get_by_text("Loja de Relatorios", exact=True)
    expect(item_loja).to_be_visible()
    log.info("Item 'Loja de Relatorios' encontrado e visível.")
    item_loja.click()
    log.info("Clicou em 'Loja de Relatorios'.")

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
        log.debug(f"Verificando visibilidade do grupo: {grupo}")
        # Espera o grupo estar visível, rolando se necessário
        group_locator = page.get_by_text(f"Grupo: {grupo}", exact=True)
        group_locator.scroll_into_view_if_needed()
        expect(group_locator).to_be_visible()
        log.debug(f"Grupo '{grupo}' visível.")

    log.info("Todos os grupos de relatórios verificados. Procurando botões de download.")
    # Depois de percorrer todos os grupos, todos os botões de download devem estar presentes no DOM
    download_buttons = page.locator('a[title="Download"]').all()
    log.info(f"Encontrados {len(download_buttons)} botões de download.")

    # Itera sobre todos os botões de download e clica em cada um
    for i, button in enumerate(download_buttons):
        log.debug(f"Clicando no botão de download {i+1}/{len(download_buttons)}.")
        button.scroll_into_view_if_needed()
        button.click()
        
        popup = page.locator(".dx-overlay-content:has-text('Confirma o Download?'):visible")
        expect(popup).to_be_visible()
        log.debug("Popup de confirmação de download visível.")
        popup.get_by_role("button", name="Sim").click()
        log.info("Confirmado o download no popup.")
        expect(popup).to_be_hidden()
        log.debug("Popup de confirmação de download oculto.")
    
    log.info(f"Teste de download de relatórios concluído com sucesso para o perfil: {perfil_cliente}.")