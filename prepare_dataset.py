import os
import shutil

# Caminhos base
base_dir = os.path.dirname(os.path.abspath(__file__))
dataset_dir = os.path.join(base_dir, "dataset")
rgb_dir = os.path.join(dataset_dir, "rgb")
bbox_dir = os.path.join(dataset_dir, "bbox_txt")
img_list_dir = os.path.join(dataset_dir, "img_list")

output_images_dir = os.path.join(base_dir, "images")
output_labels_dir = os.path.join(base_dir, "labels")

# Divisões
splits = ["train", "val", "test"]

# Função para criar pastas se não existirem
def criar_pastas():
    for split in splits:
        os.makedirs(os.path.join(output_images_dir, split), exist_ok=True)
        os.makedirs(os.path.join(output_labels_dir, split), exist_ok=True)

# Função para copiar imagens e labels
def copiar_arquivos():
    for split in splits:
        lista_path = os.path.join(img_list_dir, f"{split}.txt")
        with open(lista_path, "r") as f:
            nomes = [linha.strip() for linha in f.readlines()]
        
        for nome in nomes:

            nome = nome.strip()
            nome_base, _ = os.path.splitext(nome)
            nome_sem_ext = os.path.splitext(nome)[0]
            extensao = os.path.splitext(nome)[1] or ".png"
   
            # Caminhos dos arquivos de origem
            img_src = os.path.join(rgb_dir, nome)
            label_src = os.path.join(bbox_dir, nome_base + ".txt")

            # Caminhos dos arquivos de destino
            img_dst = os.path.join(output_images_dir, split, nome)
            label_dst = os.path.join(output_labels_dir, split, nome_base + ".txt")

            # Copia os arquivos
            if os.path.exists(img_src):
                shutil.copyfile(img_src, img_dst)
            else:
                print(f"[AVISO] Imagem não encontrada: {img_src}")
            if os.path.exists(label_src):
                shutil.copyfile(label_src, label_dst)
            else:
                print(f"[AVISO] Label não encontrada: {label_src}")

# Execução
if __name__ == "__main__":
    print("⏳ Criando estrutura de pastas...")
    criar_pastas()
    print("✅ Pastas prontas. Copiando arquivos...")
    copiar_arquivos()
    print("🏁 Concluído com sucesso!")