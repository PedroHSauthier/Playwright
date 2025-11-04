from dataclasses import dataclass
import json
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
    caminho_json = Path(__file__).parent.parent.parent / "dados_teste" / "individuos.json"
    with open(caminho_json, 'r', encoding='utf-8') as f:
        todos_dados = json.load(f)
    
    nomes_perfis = list(todos_dados.keys())
    
    if not args:
        return {nome: Individuo(**dados) for nome, dados in todos_dados.items()}

    # Modo AND: um único argumento de lista
    if len(args) == 1 and isinstance(args[0], list):
        termos_filtro = [str(termo).lower() for termo in args[0]]
        nomes_filtrados = []
        for nome in nomes_perfis:
            nome_lower = nome.lower()
            if all(termo in nome_lower for termo in termos_filtro):
                nomes_filtrados.append(nome)
    
    # Modo OR: múltiplos argumentos de string
    else:
        termos_filtro = [str(termo).lower() for termo in args]
        nomes_filtrados = []
        for nome in nomes_perfis:
            nome_lower = nome.lower()
            if any(termo in nome_lower for termo in termos_filtro):
                nomes_filtrados.append(nome)

    dados_filtrados = {}
    for nome in nomes_filtrados:
        dados_filtrados[nome] = Individuo(**todos_dados[nome])
        
    return dados_filtrados

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

def carregar_dados_individuo_por_cpf(cpf: str) -> Individuo | None:
    """
    Carrega os dados de um indivíduo específico do arquivo JSON com base no CPF.

    Args:
        cpf (str): O CPF do indivíduo a ser encontrado.

    Returns:
        Individuo | None: O objeto Individuo correspondente ou None se não for encontrado.
    """
    todos_individuos = Individuo.carregar_todos_individuos()
    for individuo in todos_individuos.values():
        if individuo.identificacao.get('CPF') == cpf:
            return individuo
    return None
