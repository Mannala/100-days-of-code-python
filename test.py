import os, re

def count_completed_days():
    # Alle Ordner im aktuellen Verzeichnis durchsuchen
    # current_dir = os.getcwd()
    # days_pattern = re.compile(r'^day\d+$', re.IGNORECASE)  # Regex für "dayXX" Ordner (case insensitive)
    # completed_days = 0
    #
    # # Überprüfen, welche Ordner dem Muster "dayXX" entsprechen
    # for folder in os.listdir(current_dir):
    #     if os.path.isdir(folder) and days_pattern.match(folder):
    #         completed_days += 1

    readme_path = "Readme.md"

    # Prüfen, ob die Datei existiert
    if not os.path.exists(readme_path):
        print(f"Datei {readme_path} nicht gefunden.")
        return 0  # Falls die Datei nicht existiert, gebe 0 zurück

    # Regulärer Ausdruck für bearbeitete Tage
    day_pattern = re.compile(r"\[Day (\d+)[^\]]*\]", re.IGNORECASE)  # Sucht nach z. B. "[Day 1]"

    completed_days = []  # Speichert die gefundenen Tage als Zahlen

    # Lese die Datei zeilenweise
    with open(readme_path, "r") as file:
        for line in file:
            match = day_pattern.search(line)
            if match:
                completed_days.append(int(match.group(1)))  # Speichert die Zahl z. B. 1, 2, 3...

        return len(completed_days)  # Gibt die Anzahl der bearbeiteten Tage zurück



# Testaufruf
completed = count_completed_days()
print(completed)
