import os

def calculate_progress():
    # Annahme: Alle Ordner heißen "DayXX"
    days = [folder for folder in os.listdir('.') if folder.startswith('Day') and folder[3:].isdigit()]
    completed_days = len(days)
    total_days = 100
    progress_percentage = (completed_days / total_days) * 100

    # Fortschrittsanzeige im Markdown-Stil
    progress_bar = f"![Progress](https://progress-bar.dev/{int(progress_percentage)}/?title=Progress)"

    return progress_bar

def update_readme(progress_bar):
    with open("README.md", "r") as file:
        lines = file.readlines()

    # Ersetze den Fortschrittsplatzhalter in der README.md
    with open("README.md", "w") as file:
        for line in lines:
            if line.startswith("![Progress]"):
                file.write(progress_bar + "\n")
            else:
                file.write(line)

if __name__ == "__main__":
    progress_bar = calculate_progress()
    update_readme(progress_bar)
