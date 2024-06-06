# OCR IMAGES

Requisitos:

sudo apt update
sudo apt upgrade -y
sudo apt install tesseract-ocr -y
sudo apt install libtesseract-dev -y
sudo apt install tesseract-ocr-[langcode]

**Observação**: se usar zsh utilize tesseract-ocr-\[langcode\]


# Exemplo para instalar o pacote de português:
sudo apt install tesseract-ocr-por


No .bashrc na raíz do seu linux (/home/ubuntu):

```s
export TESSDATA_PREFIX=/usr/share/tesseract-ocr/4.00/tessdata/
```

Recarregue o terminal e teste se imprime:

```s
echo $TESSDATA_PREFIX
```

Crie o ambiente python

```s
python3 -m venv .venv
```

Ative-o:

```s
source .venv/bin/activate
```

Instale os pacotes com o comando:

```s
pip3 install -r requirements.txt
```

Execute o script:

```s
python main.py
```

