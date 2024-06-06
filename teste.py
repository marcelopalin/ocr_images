from PIL import Image
import pytesseract

# Carregar a imagem processada
image_path = "Saida/Processed/processed_1.jpg"
image = Image.open(image_path)

# Executar o OCR na imagem processada
text = pytesseract.image_to_string(image)

# Exibir o texto extraído para comparação
print(text)
