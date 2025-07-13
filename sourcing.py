import os 
import django 
import requests 

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pfol.settings')
django.setup()

from p_app.models import Saying

def import_greek_sayings():
    file_path = os.path.join(os.path.dirname(__file__), 'greek.txt')

    with open(file_path, 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) != 3:
                print(f"Skipping malformed line: {line}")
                continue

            original, translation, explanation = parts

            Saying.objects.create(
                original_text=original,
                translation=translation,
                explanation=explanation,
                culture='Greek',
                tone='reflective',  # or dynamic in future
                source='Greek Proverbs Collection'
            )
            count += 1

    print(f"✅ Imported {count} Greek sayings.")

def import_hebrew_proverbs():
    url = "https://www.sefaria.org/api/v3/texts/Proverbs"
    params = {"language": "he,en", "context": 0}
    response = requests.get(url, params=params)
    data = response.json()

    count = 0
    for he, en in zip(data.get('he', []), data.get('text', [])):
        if not he or not en:
            continue
        Saying.objects.create(
            original_text=he,
            translation=en,
            explanation="A proverb from old Hebrew scriptures.",
            culture="Hebrew",
            tone="reflective",
            source="Sefaria API"
        )
        count += 1

    print(f"✅ Imported {count} Hebrew proverbs.")

if __name__ == '__main__':
    import_greek_sayings()
    import_hebrew_proverbs()
