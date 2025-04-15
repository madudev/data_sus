from dbfread import DBF
import pandas as pd
import os
from utils import criar_dicionario_municipios  # Importe a função do arquivo utils

class DBFProcessor:
    def __init__(self, dbf_path):
        self.dbf_path = dbf_path
        self.dicionario_mun_natu = criar_dicionario_municipios(self.dbf_path)  # Passe dbf_path

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
            else:
                print("A coluna CODMUNNATU não foi encontrada no arquivo DBF.")

        except FileNotFoundError:
            print(f"Erro: Arquivo DBF não encontrado em: {self.dbf_path}")
        except Exception as e:
            print(f"Ocorreu um erro ao processar o arquivo DBF: {e}")

if __name__ == '__main__':
    # Exemplo de uso (o usuário deve fornecer o caminho real do arquivo DBF)
    dbf_path = "data/raw/DOINF23.dbf"  # Substitua pelo caminho real
    processor = DBFProcessor(dbf_path)
    processor.process_dbf()