import os
import logging

# Configure o logger (nível básico: INFO)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Caminho para o arquivo TXT com dados dos municípios
municip_txt_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../dictionaries/municipios/municipio_codigos.txt")

def criar_dicionario_municipios(dbf_path):
    """
    Cria um dicionário de códigos de município para nomes de município a partir do arquivo TXT.

    Args:
        dbf_path (str): Caminho para o arquivo DBF (usado para fins de log, não para processamento direto).

    Returns:
        dict: Dicionário onde as chaves são os códigos de município e os valores são os nomes.
    """
    dicionario_mun_natu = {}
    try:
        with open(municip_txt_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                partes = line.strip().split()
                if len(partes) > 2 and partes[1].isdigit() and len(partes[1]) == 6:
                    codigo_municipio = partes[1]
                    nome_municipio_lista = partes[2:]
                    nome_municipio = " ".join(nome_municipio_lista).split('(')[0].strip()
                    nome_municipio = nome_municipio.replace(codigo_municipio, "").strip()
                    dicionario_mun_natu[codigo_municipio] = nome_municipio
        logging.info(f"Dicionário de municípios criado com sucesso a partir de: {municip_txt_path}")
    except FileNotFoundError:
        logging.error(f"Erro: Arquivo de municípios não encontrado em: {municip_txt_path}")
    except Exception as e:
        logging.error(f"Ocorreu um erro ao ler o arquivo de municípios: {e}")
        logging.exception(e)  # Loga a stack trace completa
    return dicionario_mun_natu