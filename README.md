<h1 align="center">🌅 Video Creator</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge">
  <img src="https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge" alt="Status Badge">
</p>

<p align="center">
  <i>Programa que transforma uma sequência de imagens em um vídeo.</i><br>
  <b>Autor:</b> Caetano Bordin
</p>

---

## 🧩 Sobre o Projeto

O **Video Creator** utiliza imagens de um pôr do sol para criar um vídeo automaticamente.

O programa encontra as imagens dentro de uma pasta, identifica suas dimensões e utiliza o **OpenCV** para juntá-las em sequência, gerando um arquivo de vídeo.

---

## 🧰 Tecnologias Utilizadas

* **Python**
* **OpenCV (cv2)**
* **OS** — gerenciamento dos arquivos da pasta.

---

## ⚙️ Funcionalidades

* 📁 Leitura das imagens de uma pasta;
* 🖼️ Identificação do tamanho das imagens;
* 🎞️ Criação de um arquivo de vídeo;
* ⏩ Organização das imagens em sequência;
* 💾 Exportação do vídeo como `sol.mp4`.

---

## 📚 Aprendizados

* Manipulação de arquivos e pastas com `os`;
* Leitura de imagens com OpenCV;
* Utilização de `VideoWriter`;
* Trabalho com dimensões de imagens;
* Criação de vídeos a partir de vários frames.

---

## 🕹️ Como Executar

1. Instale o OpenCV:

```bash
pip install opencv-python
```

2. Coloque as imagens do pôr do sol dentro da pasta:

```text
images/
```

3. Execute o programa:

```bash
python main.py
```

4. O vídeo será gerado como:

```text
sol.mp4
```

---

## 📜 Licença

O código pode ser usado somente para **fins educacionais**.

É permitida a modificação e redistribuição, desde que os autores sejam citados e a licença original seja mantida.

O software é fornecido **"como está"**, sem garantias de qualquer tipo. Os autores não são responsáveis por danos decorrentes de seu uso.

---

## 👨‍💻 Autor

**Caetano Bordin**

🔗 [@Caetano-2012](https://www.github.com/Caetano-2012)

---
