from dataclasses import dataclass
import json
import logging
from pathlib import Path
from typing import Dict, List

@dataclass
class Individuo:
    """Encapsula os dados de um indivíduo."""
    identificacao: dict
    DocumentosPessoais: dict
    VinculoDomiciliar: dict
    InformacoesESUS: dict
    SaidaDoCidadao: dict
    Profissional: dict

    @staticmethod
    def carregar_todos_individuos() -> Dict[str, 'Individuo']:
        """
        Carrega todos os indivíduos do arquivo individuos.json.

        Returns:
            Dict[str, Individuo]: Um dicionário onde as chaves são os nomes dos perfis
                                  dos indivíduos e os valores são objetos Individuo.
        """
        caminho_json = Path(__file__).parent.parent.parent / "dados_teste" / "individuos.json"
        
        try:
            with open(caminho_json, 'r', encoding='utf-8') as f:
                dados = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo de dados não encontrado em: {caminho_json}")
        except json.JSONDecodeError:
            raise ValueError(f"Erro ao decodificar o JSON em: {caminho_json}")

        individuos = {}
        for nome_perfil, dados_individuo in dados.items():
            individuos[nome_perfil] = Individuo(**dados_individuo)
            
        return individuos

def carregar_dados_individuos(*args) -> Dict[str, 'Individuo']:
    """
    Carrega e filtra os dados dos indivíduos do arquivo JSON com base nos critérios fornecidos.

    A função opera em dois modos, dependendo de como os argumentos são passados:

    1.  **Modo OR (padrão)**:
        - **Uso**: Passe uma ou mais strings como argumentos separados.
        - **Lógica**: Retorna indivíduos cujos nomes de perfil contêm **pelo menos uma** das strings.
        - **Exemplo**: `carregar_dados_individuos('pedro', 'teste')` retornará indivíduos com 'pedro' ou 'teste' no nome do perfil.

    2.  **Modo AND**:
        - **Uso**: Passe uma única lista de strings como argumento.
        - **Lógica**: Retorna indivíduos cujos nomes de perfil contêm **todas** as strings na lista.
        - **Exemplo**: `carregar_dados_individuos(['pedro', 'teste'])` retornará indivíduos com 'pedro' e 'teste' no nome do perfil.

    Se nenhum argumento for fornecido, todos os indivíduos são retornados.
    A verificação não diferencia maiúsculas de minúsculas.

    Args:
        *args: Argumentos dinâmicos para filtragem.

    Returns:
        Dict[str, Individuo]: Um dicionário de indivíduos filtrados.
    """
    log = logging.getLogger(__name__)
    log.debug(f"carregar_dados_individuos received args: {args}")

    caminho_json = Path(__file__).parent.parent.parent / "dados_teste" / "individuos.json"
    with open(caminho_json, 'r', encoding='utf-8') as f:
        todos_dados = json.load(f)
    
    if not args:
        log.debug("No args provided, returning all individuals.")
        return {nome: Individuo(**dados) for nome, dados in todos_dados.items()}

    # Determine the filtering mode (AND vs. OR)
    is_and_mode = len(args) == 1 and isinstance(args[0], list)
    
    if is_and_mode:
        log.debug("AND mode detected.")
        termos_filtro = [str(termo).lower() for termo in args[0]]
        log.debug(f"Filter terms (AND): {termos_filtro}")
        filter_logic = lambda nome_lower: all(termo in nome_lower for termo in termos_filtro)
    else:
        log.debug("OR mode detected.")
        termos_filtro = [str(termo).lower() for termo in args]
        log.debug(f"Filter terms (OR): {termos_filtro}")
        filter_logic = lambda nome_lower: any(termo in nome_lower for termo in termos_filtro)

    # Apply the determined logic to filter the names
    nomes_filtrados = [
        nome for nome in todos_dados.keys() 
        if filter_logic(nome.lower())
    ]
    log.debug(f"Filtered profile names: {nomes_filtrados}")

    # Build the final dictionary from the filtered names
    return {
        nome: Individuo(**todos_dados[nome]) 
        for nome in nomes_filtrados
    }

def carregar_cpf_individuos(*args) -> List[str]:
    """
    Carrega e filtra os CPFs dos indivíduos do arquivo JSON com base nos critérios de nome de perfil.

    A função opera em dois modos, dependendo de como os argumentos são passados:

    1.  **Modo OR (padrão)**:
        - **Uso**: Passe uma ou mais strings como argumentos separados.
        - **Lógica**: Retorna CPFs de indivíduos cujos nomes de perfil contêm **pelo menos uma** das strings.
        - **Exemplo**: `carregar_cpf_individuos('pedro', 'teste')` retornará os CPFs de indivíduos com 'pedro' ou 'teste' no nome do perfil.

    2.  **Modo AND**:
        - **Uso**: Passe uma única lista de strings como argumento.
        - **Lógica**: Retorna CPFs de indivíduos cujos nomes de perfil contêm **todas** as strings na lista.
        - **Exemplo**: `carregar_cpf_individuos(['pedro', 'teste'])` retornará os CPFs de indivíduos com 'pedro' e 'teste' no nome do perfil.

    Se nenhum argumento for fornecido, todos os CPFs de indivíduos são retornados.
    A verificação não diferencia maiúsculas de minúsculas.

    Args:
        *args: Argumentos dinâmicos para filtragem.

    Returns:
        List[str]: Uma lista de CPFs de indivíduos filtrados.
    """
    dados_filtrados = carregar_dados_individuos(*args)
    return [individuo.identificacao['CPF'] for individuo in dados_filtrados.values()]

def carregar_dados_individuo_por_cpf(cpf: str, filtros_nome: List[str] = None) -> Individuo | None:
    """
    Carrega os dados de um indivíduo específico do arquivo JSON com base no CPF e, opcionalmente,
    em filtros de nome de perfil.

    Args:
        cpf (str): O CPF do indivíduo a ser encontrado.
        filtros_nome (List[str], optional): Uma lista de strings que devem estar contidas
                                            no nome do perfil do indivíduo. Defaults to None.

    Returns:
        Individuo | None: O objeto Individuo correspondente ou None se não for encontrado.
    """
    todos_individuos = Individuo.carregar_todos_individuos() # This returns a dict {profile_name: Individuo_object}
    
    for nome_perfil, individuo in todos_individuos.items():
        # Checagem 1: CPF corresponde
        if individuo.identificacao.get('CPF') == cpf:
            
            # Se não houver filtros de nome, retorna o primeiro CPF correspondente (comportamento antigo)
            if not filtros_nome:
                return individuo
            
            # Checagem 2: Todos os filtros de nome correspondem ao nome do perfil
            nome_perfil_lower = nome_perfil.lower()
            if all(filtro.lower() in nome_perfil_lower for filtro in filtros_nome):
                return individuo
                
    return None
