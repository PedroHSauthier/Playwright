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
