from dbfread import DBF
import pandas as pd
import os
from .cid.cid_service import CIDService
from .utils import criar_dicionario_municipios  # Importe a função utils

class DBFProcessor:
    def __init__(self, dbf_path):
        self.dbf_path = dbf_path
        self.dicionario_mun_natu = criar_dicionario_municipios(dbf_path)  # Chame a função diretamente

    def process_dbf(self):
        """
        Processa o arquivo DBF, adicionando a coluna de nomes de município.
        """
        try:
            table = DBF(self.dbf_path, encoding='latin-1')
            df = pd.DataFrame(iter(table))

            if 'CODMUNNATU' in df.columns:
                df['MUN_NATU_DESC'] = df['CODMUNNATU'].astype(str).map(self.dicionario_mun_natu)
                print(df[['CODMUNNATU', 'MUN_NATU_DESC']].head())
                return df  # Retorna o DataFrame processado
            else:
                print("A coluna CODMUNNATU não foi encontrada no arquivo DBF.")
                return None

        except FileNotFoundError:
            print(f"Erro: Arquivo DBF não encontrado em: {self.dbf_path}")
            return None
        except Exception as e:
            print(f"Ocorreu um erro ao processar o arquivo DBF: {e}")
            return None

if __name__ == '__main__':
    dbf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/raw/DOINF23.dbf")
    cid_data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../dictionaries/CID")

    cid_service = CIDService(cid_data_dir)
    cid_service._carregar_dicionario_cid() # Garante que o dicionário CID seja carregado

    processor = DBFProcessor(dbf_path)
    df_processado = processor.process_dbf()

    if df_processado is not None:
        if 'LINHAA' in df_processado.columns:
            df_processado['DESCRICAO_CID_A'] = df_processado['LINHAA'].map(cid_service.cid_dictionary.get)
            print("\nPrimeiras linhas com descrição CID (Linha A):")
            print(df_processado[['LINHAA', 'DESCRICAO_CID_A']].head())
        else:
            print("\nA coluna LINHAA não foi encontrada no arquivo DBF.")

        print("\nPrimeiras linhas do DataFrame processado:")
        print(df_processado.head())