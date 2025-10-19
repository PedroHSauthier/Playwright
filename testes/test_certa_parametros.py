from playwright.sync_api import Page, expect
import os
from dotenv import load_dotenv

load_dotenv()
cpf = os.getenv("cliente_cpf")
senha = os.getenv("cliente_senha")

def baixar_relatorios(logar_usuario):
    
    pagina_logada = logar_usuario(cpf, senha)
    
    