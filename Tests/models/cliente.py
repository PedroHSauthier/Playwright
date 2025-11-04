from dataclasses import dataclass
import json
from pathlib import Path

@dataclass
class Cliente:
    """Encapsula todos os dados e credenciais de um cliente."""
    cpf: str
    senha: str
    unidade: str
    url: str

    @staticmethod
    def carregar_dados_cliente(perfil: str) -> 'Cliente':
        """
        Carrega os dados de um perfil de cliente específico do arquivo JSON.
        """
        # O caminho é construído a partir do local deste arquivo, subindo dois níveis de diretório 
        # (de 'models' para 'testes', e de 'testes' para a raiz do projeto)
        # e então entrando em 'dados_teste/clientes.json'.
        caminho_json = Path(__file__).parent.parent.parent / "dados_teste" / "clientes.json"
        
        try:
            with open(caminho_json, 'r', encoding='utf-8') as f:
                dados = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo de dados não encontrado em: {caminho_json}")
        except json.JSONDecodeError:
            raise ValueError(f"Erro ao decodificar o JSON em: {caminho_json}")

        dados_perfil = dados.get(perfil)
        if not dados_perfil:
            raise ValueError(f"Perfil de cliente '{perfil}' não encontrado em {caminho_json}")
            
        return Cliente(**dados_perfil)
    
def carregar_nomes_clientes(*args) -> list[str]:
    """
    Carrega e filtra os nomes dos clientes do arquivo JSON com base nos critérios fornecidos.

    A função opera em dois modos, dependendo de como os argumentos são passados:

    1.  **Modo OR (padrão)**:
        - **Uso**: Passe uma ou mais strings como argumentos separados.
        - **Lógica**: Retorna nomes de clientes que contêm **pelo menos uma** das strings.
        - **Exemplo**: `carregar_nomes_clientes('admin', 'dev')` retornará nomes com 'admin' ou 'dev'.

    2.  **Modo AND**:
        - **Uso**: Passe uma única lista de strings como argumento.
        - **Lógica**: Retorna nomes de clientes que contêm **todas** as strings na lista.
        - **Exemplo**: `carregar_nomes_clientes(['admin', 'dev'])` retornará nomes com 'admin' e 'dev'.

    Se nenhum argumento for fornecido, todos os nomes de clientes são retornados.
    A verificação não diferencia maiúsculas de minúsculas.

    Args:
        *args: Argumentos dinâmicos para filtragem.
        
    Returns:
        list[str]: Uma lista de nomes de clientes filtrada.
    """
    caminho_json = Path(__file__).parent.parent.parent / "dados_teste" / "clientes.json"
    with open(caminho_json, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    
    nomes_clientes = list(dados.keys())
    
    if not args:
        return nomes_clientes

    # Modo AND: um único argumento de lista
    if len(args) == 1 and isinstance(args[0], list):
        termos_filtro = [str(termo).lower() for termo in args[0]]
        clientes_filtrados = []
        for nome in nomes_clientes:
            nome_lower = nome.lower()
            if all(termo in nome_lower for termo in termos_filtro):
                clientes_filtrados.append(nome)
        return clientes_filtrados
    
    # Modo OR: múltiplos argumentos de string
    else:
        termos_filtro = [str(termo).lower() for termo in args]
        clientes_filtrados = []
        for nome in nomes_clientes:
            nome_lower = nome.lower()
            if any(termo in nome_lower for termo in termos_filtro):
                clientes_filtrados.append(nome)
        return clientes_filtrados
