# Projeto_2_IIA
## Detecção de Copas de Árvores Urbanas com YOLOv8

Este projeto tem como objetivo aplicar técnicas modernas de **detecção de objetos** utilizando **YOLOv8**, treinado em imagens aéreas urbanas da cidade de Campo Grande/MS, com foco na **identificação individual de copas de árvores**.

## 🧷Autores

João Victor Pereira Vieira - 211036114 
Felipe Oliveira do Nascimento Florentino - 202021767

## 📁 Estrutura do Projeto

```plaintext

PROJETO_2_IIA/
├── dataset/
│   ├── bbox_txt/               # Labels originais no formato VOC
│   ├── gt/                     # (Possivelmente não utilizado)
│   ├── img_list/               # Listas de divisão (train.txt, val.txt, test.txt)
│   ├── rgb/                    # Imagens originais em alta resolução
│   ├── MMdetecion_v_2_0.ipynb  # Notebook original do repositório base
│   └── README                  # README original da base de dados
│
├── images/                     # Imagens divididas por treino/val/teste para o YOLO
│   ├── train/
│   ├── val/
│   └── test/
│
├── labels/                     # Labels convertidas para o formato YOLO
│   ├── train/
│   ├── val/
│   └── test/
│
├── runs/detect/                # Saída gerada pelo treinamento e predição do YOLO
│   ├── detectar_arvores/
│   ├── detectar_arvores2/
│   ├── detectar_arvores3/
|   ├── detectar_arvores32/
│   └── predict*/               # Pasta com predições feitas
│
├── convert_labels_to_yolo.py   # Script que converte labels VOC para YOLO
├── prepare_dataset.py          # Organiza as imagens e labels no formato esperado pelo YOLO
├── notebook.ipynb              # Notebook com todo o fluxo: treino, predição, visualização
├── data.yaml                   # Arquivo de configuração do dataset para o YOLOv8
├── requirements.txt            # Dependências do projeto (pip install -r requirements.txt)
├── resultados.txt              # Métricas salvas automaticamente após a validação
└── projeto2-iia-2025-1.pdf     # Especificação oficial do projeto (PDF fornecido pelo professor)

```
## 🧠 Dataset Utilizado

- Baseado no artigo: **[Benchmarking Anchor-based and Anchor-free DL Methods for Tree Detection](https://www.mdpi.com/2072-4292/13/13/2482)**
- Imagens RGB de 512x512 pixels (recortes de ortoimagens aéreas)
- Anotações manuais convertidas para bounding boxes
- Aproximadamente 3300 árvores anotadas

## ⚙️ Como executar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/Projeto_2_IIA.git
cd Projeto_2_IIA

```
2. Instale as dependências 

```bash
pip install -r requirements.txt
```
3. Rode Scripts de preparação no terminal

```bash
python prepare_dataset.py
python convert_labels_to_yolo.py
```

4. Execute o notebook `notebook.ipynb` para:

- Treinar o modelo

- Avaliar as métricas

- Visualizar as predições interativas com `IPython` e `ipywidgets`

OBS: Já vou deixar os resultados de um treinamento prontos no código, mas se quiser limpar só executar o último bloco do notebook, onde ele faz a limpeza total

## 📊 Resultados

- As métricas são salvas automaticamente em `resultados.txt`após o treino

- Exemplo da saída que consegui com 100 epochs:

``` plaintext
📊 MÉTRICAS DO MODELO YOLOv8
============================
mAP50: 0.7174
mAP50-95: 0.4103
Precision (mp): 0.7539
Recall (mr): 0.6298
Velocidade de inferência (ms/imagem): 40.05
```

## 📸 Visualização

Visualização interativa de predições com botões "Próxima" e "Anterior", diretamente no notebook, usando `IPython.display` + `ipywidgets`.

## 🧼 Limpeza

O notebook permite remover com segurança os diretórios `runs/` e o arquivo `resultados.txt`, com confirmação via input para evitar exclusões acidentais.