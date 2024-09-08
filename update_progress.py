from PIL import Image, ImageDraw, ImageFont
import os
import re

def create_progress_image(progress_percentage, output_path):
    width, height = 400, 50
    background_color = (255, 255, 255)
    bar_color = (76, 175, 80)
    text_color = (0, 0, 0)

    # Neues Bild erstellen
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Fortschrittsbalken zeichnen
    bar_width = int(width * (progress_percentage / 100))
    draw.rectangle([0, 0, bar_width, height], fill=bar_color)

    # Fortschrittsprozentzahl zeichnen
    font = ImageFont.load_default()
    text = f"{progress_percentage:.1f}%"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
    draw.text(((width - text_width) // 2, (height - text_height) // 2), text, fill=text_color, font=font)

    # Bild speichern
    image.save(output_path)

def count_completed_days():
    # Alle Ordner im aktuellen Verzeichnis durchsuchen
    current_dir = os.getcwd()
    days_pattern = re.compile(r'^day\d+$', re.IGNORECASE)  # Regex für "dayXX" Ordner (case insensitive)
    completed_days = 0

    # Überprüfen, welche Ordner dem Muster "dayXX" entsprechen
    for folder in os.listdir(current_dir):
        if os.path.isdir(folder) and days_pattern.match(folder):
            completed_days += 1

    return completed_days

def update_readme(completed_days, total_days):
    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print(f"Datei {readme_path} nicht gefunden.")
        return

    with open(readme_path, "r") as file:
        lines = file.readlines()

    progress_text = f"{completed_days} Tage von {total_days} abgeschlossen"

    # Finde und aktualisiere den Fortschrittstext in README.md
    with open(readme_path, "w") as file:
        progress_found = False
        for line in lines:
            if "Tage von" in line:
                file.write(progress_text + "\n")
                progress_found = True
            else:
                file.write(line)
        # Falls der Fortschrittstext nicht vorhanden ist, füge ihn hinzu
        if not progress_found:
            file.write("\n" + progress_text + "\n")

if __name__ == "__main__":
    # Berechne die Anzahl der abgeschlossenen Tage basierend auf vorhandenen Ordnern
    completed_days = count_completed_days()
    total_days = 100
    progress_percentage = (completed_days / total_days) * 100

    # Fortschrittsbild erstellen
    create_progress_image(progress_percentage, "progress.png")

    # README.md aktualisieren
    update_readme(completed_days, total_days)
