import pytesseract
from PIL import Image
from pathlib import Path
from openpyxl import Workbook
from loguru import logger

# Configurações dos diretórios de entrada e saída
input_dir = "./Entrada"
output_dir = "./Saida"

logger.add("ocr_extractor.log", rotation="1 MB")

def extract_text_from_image(image_path: str) -> str:
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        logger.info(f"Successfully extracted text from {image_path}")
        return text
    except Exception as e:
        logger.error(f"Error extracting text from {image_path}: {e}")
        return ""

def save_to_excel(data: list, output_path: str):
    wb = Workbook()
    ws = wb.active
    ws.title = "Resultados"

    # Write header
    ws.append(["Rank", "Name", "Points"])

    # Write data
    for player in data:
        ws.append([player['rank'], player['name'], player['points']])

    wb.save(output_path)
    logger.info(f"Successfully saved results to {output_path}")

def parse_text(text: str) -> list:
    lines = text.split('\n')
    players = []
    rank = 1

    for i in range(1, len(lines), 2):
        if i + 1 < len(lines):
            player_info = lines[i].split()
            points = lines[i + 1].strip()

            if len(player_info) > 1 and points.replace(',', '').isdigit():
                name = ' '.join(player_info[:-1])
                players.append({
                    'rank': rank,
                    'name': name,
                    'points': points
                })
                rank += 1

    return players

def main():
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    
    # Ensure output directory exists
    output_path.mkdir(parents=True, exist_ok=True)

    # List all JPG files in the input directory
    images = list(input_path.glob("*.jpg"))
    logger.info(f"Found {len(images)} images")
    print(f"Found {len(images)} images")

    all_players = []

    for idx, image in enumerate(images, start=1):
        logger.info(f"Processing image: {image}")
        print(f"Processing image: {image}")
        text = extract_text_from_image(image)

        # Save the OCR text result to a file
        text_output = output_path / f"fig{idx}.txt"
        with text_output.open('w') as f:
            f.write(text)

        players = parse_text(text)
        all_players.extend(players)
        for player in players:
            print(f"Processed player: {player['name']}")

    # Save all results to Excel
    if all_players:
        excel_output = output_path / "resultados.xlsx"
        save_to_excel(all_players, excel_output)
    else:
        logger.warning("No players were processed. No Excel file created.")

    logger.info("Processing completed.")
    print("Processing completed.")

if __name__ == "__main__":
    main()

