import pandas as pd
import os
import logging
import re

# Configure o logger (se você quiser um logger específico para o CID)
cid_logger = logging.getLogger('cid_service')
cid_logger.setLevel(logging.INFO)
# ... (Configure handlers se necessário)

class CIDService:
    def __init__(self, cid_data_dir):
        """
        Inicializa o CIDService.

        Args:
            cid_data_dir (str): Diretório contendo os arquivos de dados CID.
        """
        self.cid_data_dir = cid_data_dir
        self.arquivo_cid_concatenado = "cid_concatenado.txt" # Nome do arquivo concatenado
        self.cid_dictionary = self._carregar_dicionario_cid() # Carrega o dicionário na inicialização

    def _verificar_arquivo_concatenado(self):
        """
        Verifica se o arquivo CID concatenado existe.

        Returns:
            bool: True se o arquivo existe, False caso contrário.
        """
        caminho_arquivo = os.path.join(self.cid_data_dir, self.arquivo_cid_concatenado)
        return os.path.exists(caminho_arquivo)

    def concatenar_arquivos_cid(self):
        """
        Concatena todos os arquivos .cnv do diretório CID em um único arquivo.
        """
        arquivos = [
            f for f in os.listdir(self.cid_data_dir)
            if f.lower().endswith(".cnv") and f.lower() != self.arquivo_cid_concatenado.lower()
        ]
        cid_logger.info(f"Arquivos .cnv encontrados para concatenar: {arquivos}")

        if not arquivos:
            cid_logger.warning(f"Nenhum arquivo com extensão '.cnv' encontrado (ou todos são o arquivo de saída) em: {self.cid_data_dir}")
            return

        caminho_saida = os.path.join(self.cid_data_dir, self.arquivo_cid_concatenado)
        try:
            with open(caminho_saida, 'w', encoding='utf-8') as saida:
                for nome_arquivo in arquivos:
                    caminho = os.path.join(self.cid_data_dir, nome_arquivo)
                    try:
                        with open(caminho, 'r', encoding='latin-1', errors='ignore') as f:
                            conteudo = f.read()
                            saida.write(f"### {nome_arquivo} ###\n")
                            saida.write(conteudo + '\n')
                        cid_logger.info(f"Arquivo concatenado com sucesso: {nome_arquivo}")
                    except FileNotFoundError:
                        cid_logger.error(f"Arquivo não encontrado durante a concatenação: {nome_arquivo}")
                    except Exception as e:
                        cid_logger.error(f"Erro ao processar arquivo '{nome_arquivo}' durante a concatenação: {e}")
            cid_logger.info(f"Todos os arquivos CID concatenados com sucesso em: {self.arquivo_cid_concatenado}")
        except Exception as e:
            cid_logger.error(f"Erro ao criar/escrever no arquivo concatenado '{self.arquivo_cid_concatenado}': {e}")

    def _carregar_dicionario_cid(self):
        """
        Carrega o dicionário CID a partir do arquivo TXT concatenado.

        Returns:
            dict: Dicionário onde as chaves são os códigos CID e os valores são as descrições.
        """
        dicionario_cid = {}
        caminho_arquivo = os.path.join(self.cid_data_dir, self.arquivo_cid_concatenado)
        if not self._verificar_arquivo_concatenado():
            cid_logger.warning(f"Arquivo CID concatenado '{self.arquivo_cid_concatenado}' não encontrado. Tentando concatenar os arquivos.")
            self.concatenar_arquivos_cid()
            if not self._verificar_arquivo_concatenado():
                cid_logger.error(f"Arquivo CID concatenado '{self.arquivo_cid_concatenado}' ainda não encontrado. Impossível criar o dicionário CID.")
                return dicionario_cid  # Retorna um dicionário vazio

        try:
            with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as arquivo:
                current_file = None
                for line in arquivo:
                    line = line.strip()
                    if line.startswith("###"):
                        current_file = line.split("###")[1].strip()
                        continue
                    partes = re.findall(r'\s*(\S+)\s+(.+)', line)
                    if partes:
                        codigo_cid = partes[0][0].strip()
                        descricao_cid = partes[0][1].strip().split(' A')[0].split(',')[0].strip()
                        if codigo_cid and descricao_cid:
                            dicionario_cid[codigo_cid] = descricao_cid
        except FileNotFoundError:
            cid_logger.error(f"Arquivo CID concatenado não encontrado: {self.arquivo_cid_concatenado}")
        except Exception as e:
            cid_logger.error(f"Ocorreu um erro ao ler o arquivo CID concatenado: {e}")
            cid_logger.exception(e)
        cid_logger.info(f"Dicionário CID carregado com sucesso com {len(dicionario_cid)} entradas.")
        return dicionario_cid

