# 🏥 Projeto DataSUS  
### *Desvendando a Saúde Pública Brasileira com Dados*

![Feito com 💙 pelo SUS](https://img.shields.io/badge/feito%20com-SUS-blue)

Mergulhe na análise de dados do Sistema Único de Saúde (SUS) com Python! Este repositório reúne ferramentas e estudos que transformam os dados públicos do **DataSUS** em insights acessíveis e relevantes para a sociedade.

---

## 🎯 Objetivo

Traduzir grandes volumes de dados brutos do SUS em informações claras e úteis, revelando padrões de **mortalidade**, **nascimentos**, **internações**, **causas evitáveis** e **desigualdades regionais**.

> “Transformar dados em conhecimento é transformar vidas.”

---

## 📦 Bases de Dados Utilizadas

- **SIM** – Sistema de Informações sobre Mortalidade  
- **SIH** – Sistema de Informações Hospitalares  
- **SINASC** – Sistema de Informações sobre Nascidos Vivos  
- Arquivos auxiliares: dicionários `.cnv`, definidores `.def`, entre outros

---

## 🛠️ Bibliotecas Essenciais

Para rodar este projeto, você precisará do **Python** e das seguintes bibliotecas:

```bash
pip install pandas dbfread chardet pyodbc
pandas – análise e manipulação de dados

dbfread – leitura de arquivos .dbf

chardet – detecção de codificação de arquivos .txt / .cnv

pyodbc – leitura de .dbc via drivers ODBC (opcional)

logging (built-in) – registro e rastreamento de execução

re (built-in) – expressões regulares para parsing avançado

📁 Extensões de Arquivos Tratadas

Extensão	Descrição
.dbc	Arquivo de banco compactado — bases como SIM, SIH
.dbf	Formato legado — usado em tabelas e cadastros
.cnv	Tabelas de conversão e dicionários de variáveis
.def	Arquivo definidor para leitura com TabWin (DataSUS)
⚙️ Etapas do Projeto
📥 Coleta de arquivos de diferentes formatos

🧼 Limpeza e padronização de variáveis (ex: idade, CID-10, tipo de parto)

🔗 Cruzamentos entre bases

📊 Visualização de dados: gráficos e dashboards interativos

💡 Por que isso importa?
Porque dados confiáveis e bem tratados são essenciais para:

Identificar desigualdades em saúde

Avaliar políticas públicas

Informar a sociedade e pesquisadores

Salvar vidas com base em evidências

✨ Resultados esperados
Relatórios com causas mais frequentes de óbito infantil

Indicadores de mortalidade evitável

Visualizações em Power BI e Python

Tabelas limpas e documentadas para reutilização

Feito com 💙 pelo SUS.
