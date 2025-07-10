import os

IMG_WIDTH = 512
IMG_HEIGHT = 512

base_dir = os.path.dirname(os.path.abspath(__file__))
labels_dir = os.path.join(base_dir, "labels")

def voc_para_yolo(xmin, ymin, xmax, ymax, img_w, img_h):
    x_center = (xmin + xmax) / 2 / img_w
    y_center = (ymin + ymax) / 2 / img_h
    width = (xmax - xmin) / img_w
    height = (ymax - ymin) / img_h
    return x_center, y_center, width, height

def converter_labels():
    for split in ["train", "val", "test"]:
        pasta = os.path.join(labels_dir, split)
        for arquivo in os.listdir(pasta):
            if not arquivo.endswith(".txt"):
                continue
            novo_conteudo = []
            caminho = os.path.join(pasta, arquivo)
            with open(caminho, "r") as f:
                linhas = f.readlines()
                for linha in linhas:
                    partes = linha.strip().split()
                    if len(partes) == 4:
                        xmin, ymin, xmax, ymax = map(int, partes)
                        x, y, w, h = voc_para_yolo(xmin, ymin, xmax, ymax, IMG_WIDTH, IMG_HEIGHT)
                        novo_conteudo.append(f"0 {x:.6f} {y:.6f} {w:.6f} {h:.6f}\n")
            # Substitui o conteúdo do arquivo
            with open(caminho, "w") as f:
                f.writelines(novo_conteudo)

if __name__ == "__main__":
    print("🔄 Convertendo labels para formato YOLO...")
    converter_labels()
    print("✅ Labels convertidas com sucesso!")