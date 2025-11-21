# Projeto: Coleta de Lixo e Descarte Irregular em Belém-PA

Este projeto é desenvolvido para o **Instituto I2A2** e tem como objetivo organizar, processar e visualizar dados sobre coleta de lixo e descarte irregular na cidade de Belém, Pará. Ele integra dados de setores de coleta, bairros e áreas geográficas para facilitar análise espacial e suporte à tomada de decisão.

## 📁 Estrutura do Projeto
```
📁 Data_ambiental/
├── 📂 data/
|   ├──process          # dados organizados ou processados
|   └──raw              # dados bruto, baixados ou coletados
├── 📂 notebook/       
├── 📂 sandbox/         # Códigos baguncados
├── 📂 src/             # funcoes e codigos complementares
└── README.md
```
## 💻 Como configurar o ambiente
> ⚠️ O arquivo `requirements.txt` contém todas as dependências para instalação do ambiente.

### Criando ambiente de desenvolvimento
```bash
conda create -n data_ambiental python=3.11
conda activate data_ambiental
```
### Instalando dependências 
via conda
```
conda install numpy pandas geopandas shapely folium requests aiohttp
```
ou via pip
```
pip install -r requirements.txt
```