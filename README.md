```markdown
# 🏥 Projeto DataSUS: Desvendando a Saúde Pública Brasileira com Dados

Este repositório reúne análises e ferramentas desenvolvidas para explorar as bases públicas do Sistema Único de Saúde (SUS) por meio de Python e técnicas de ciência de dados.

📦 **Fontes utilizadas:** SIM (Mortalidade), SIH (Internações), SINASC (Nascidos vivos), entre outras bases do DataSUS.

🎯 **Objetivo:** Traduzir dados brutos em *insights* relevantes para a saúde pública, promovendo transparência, aprendizado e impacto social.

## 🛠️ Bibliotecas e Extensões Essenciais

Para executar este projeto, você precisará ter o Python instalado e as seguintes bibliotecas:

- **pandas:** Para manipulação e análise de dados tabulares.
  ```bash
  pip install pandas
  ```
- **dbfread:** Para leitura eficiente de arquivos DBF (utilizados em algumas bases do DATASUS).
  ```bash
  pip install dbfread
  ```
- **chardet:** Útil para detecção da codificação de caracteres em arquivos de texto, como os arquivos `.cnv`.
  ```bash
  pip install chardet
  ```
- **logging:** Para registrar eventos e facilitar o acompanhamento da execução do código.
  ```bash
  pip install logging
  ```
- **re (módulo built-in do Python):** Para trabalhar com expressões regulares, útil na análise de arquivos de texto não estruturados.

O projeto também lida com diferentes extensões de arquivos comuns nas bases do DATASUS:

- **.dbc:** Formato de banco de dados utilizado em algumas bases. A biblioteca `pandas` pode ler alguns arquivos `.dbc` diretamente ou através de outros pacotes como `pyodbc` se a conexão ODBC estiver configurada.
  ```bash
  pip install pyodbc
  ```
- **.dbf:** Formato de banco de dados legado, amplamente utilizado. A biblioteca `dbfread` é eficaz para ler esses arquivos.
- **.cnv:** Formato de arquivo de texto comumente encontrado nos dicionários de dados e tabelas de conversão do DATASUS. A leitura é feita com as funções padrão do Python, utilizando a detecção de codificação com `chardet` para garantir a interpretação correta dos caracteres.

## ⚙️ Etapas do Projeto

1.  **Coleta e leitura de arquivos**: `.dbc`, `.dbf` e `.cnv`.
2.  **Limpeza e padronização de variáveis**: Ex: idade, causa básica (CID-10), tipo de parto.
3.  **Cruzamento de informações**: Ex: escolaridade da mãe × causa da morte, região de internação × tempo de permanência.
4.  **Geração de gráficos e dashboards exploratórios**: Visualização de tendências, distribuições e relações nos dados.

## 💡 Por Quê?

Dados de qualidade são fundamentais para entender e melhorar as políticas públicas de saúde no Brasil. Este projeto busca contribuir para essa compreensão, oferecendo ferramentas e análises que podem auxiliar pesquisadores, profissionais de saúde e cidadãos interessados na área.

> “Transformar dados em conhecimento é transformar vidas.”





