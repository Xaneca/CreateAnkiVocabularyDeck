# Create Anki Vocabulary Deck Generator
This Python script allows you to create an **Anki flashcard deck** from a simple text file containing new vocabulary and their translations. It can generate cards in **both directions** (New Language → Native Language and vice versa).


## 📁 Vocabulary File Format

The vocabulary should be saved in a plain text file (default: `vocabulary.txt`).  
Each line represents **one vocabulary item**.

You can use **two formats**:

1. **Direct format:**
사과 - apple
책 - book


2. **Copied from Notion (automatic formatting):**
학생 = student
학교 = school

The script will automatically convert Notion-style lines into the proper format.

**Important rules:**
- Use a `-` (dash) as the separator between the **new language** and **native language** after formatting.
- Avoid empty lines.
- Make sure there are no invisible characters like non-breaking spaces.

---

## ⚙️ Script Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `vocabulary_file` | Path to your vocabulary text file | `"vocabulary.txt"` |
| `deck_name` | Name of the deck in Anki | `"Korean Vocabulary"` |
| `Deck_Type` | Determines card directions: <br>0 = Both directions (new → native & native → new) <br>1 = Only new language → native <br>2 = Only native → new | `0` |

## 🚀 Usage

1. Make sure you have Python installed.
2. Install `genanki`:

```bash
pip install genanki
Add your vocabulary to vocabulary.txt.

Run the script:
python create_deck.py
Import the generated .apkg file into Anki.
```

If you add new words, just add them to vocabulary.txt and run the script again.

Keep the same deck name and deck ID to update the existing deck.

## 📌 How It Works

1. Reads all lines from the vocabulary file.
2. Normalizes each line:
   - Converts `[word](link) = translation` into `word - translation`.
   - Trims extra spaces.
3. Generates an Anki deck (`.apkg`) using **genanki**.
4. Optionally updates the vocabulary file with the cleaned format.
5. Each line generates **two cards** if `Deck_Type = 0`.

## ⚠️ Notes & Tips

The script does not automatically remove duplicates. Anki will ignore notes with the same "Front" field if duplicates exist.

If you delete a note in Anki but it still exists in vocabulary.txt, it will be recreated next time you run the script.

Always keep a backup of your vocabulary.txt if you plan to do big edits.

Lines without a - or with invalid format will be ignored (the script prints a warning).

## 📄 Example vocabulary.txt

도시 - city
이름 - name
저 - I, me (formal)
나 - I, me (informal)
남자 - man
여자 - woman
차 (자동차) - car
사람 - person
의자 - chair
탁자 - table
침대 - bed
집 - house
책 - book
컴퓨터 - computer
나무 - tree/wood
소파 - sofa
문 - door
한국 - Korea
중국 - China
일본 - Japan
의사 - doctor
학생 - student
선생님 - teacher
이 - this
그 - that
저 - that (when something is far away)
것 - thing
이것 - this (thing)
그것 - that (thing)
저것 - that (thing)
네 - yes
아니 - no
이다 - to be
