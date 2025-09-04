import genanki
import re

################## VARIABLES #################

# If you have the txt file in a different location than this script, change "vocabulary.txt" to the full path of the file
vocabulary_file = "vocabulary.txt"
    # this file can have lines like:
        # [학생](link) = student
        #       or
        # 사과 - apple

# CHANGE AS YOUR NEW LANGUAGE
deck_name = "Korean Vocabulary"

Deck_Type = 0   # [0] - Both new language and native language as front and back cards
                # [1] - Only Card front = new language, Card back = native language
                # [2] - Only Card front = native language, Card back = new language

################## FUNCTIONS ##################

def format_lines(linha: str) -> str:
    m = re.match(r"\[(.*?)\]\(.*?\)\s*=\s*(.*)", linha)
    # first case: incorrect line
    if m:
        return f"{m.group(1).strip()} - {m.group(2).strip()}"
    
    # second case: correct line
    if "-" in linha:
        esquerda, direita = linha.split("-", 1)
        return f"{esquerda.strip()} - {direita.strip()}"
    
    return linha.strip()

def generate_deck(vocabulary):
    my_model = genanki.Model(
        1607392319,
        'Model Vocab',
        fields=[
            {'name': 'Front'},
            {'name': 'Back'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '<div style="text-align:center;">{{Front}}</div>',
                'afmt': '<div style="text-align:center;">{{Front}}<hr id="answer">{{Back}}</div>',
            },
        ])

    # ⚠️ Use always the same DECK ID to be able to update
    my_deck = genanki.Deck(
        2059400110,
        deck_name
    )

    for entry in vocabulary:
        new_lang, nat_lang = [x.strip() for x in entry.split('-')]

        if Deck_Type == 0 or Deck_Type == 1:
            note1 = genanki.Note(
                model=my_model,
                fields=[new_lang, nat_lang]
            )
            my_deck.add_note(note1)
        
        if Deck_Type == 0 or Deck_Type == 2:
            note2 = genanki.Note(
                model=my_model,
                fields=[nat_lang, new_lang]
            )
            my_deck.add_note(note2)
        

    genanki.Package(my_deck).write_to_file(f'{deck_name}.apkg')
    return

################# SCRIPT #####################

if __name__ == "__main__":
    # READ VOCABULARY FROM TXT
    with open(vocabulary_file, "r", encoding="utf-8") as f:
        vocabulary = [line.strip() for line in f if line.strip()]

    vocabulary = [format_lines(l) for l in vocabulary]      # this is because in my case, I had the lines not formatted because of NOTION copy and past
                                                            # this won't affect your file
    
    # UPDATE VOCABULARY FILE AFTER FORMATTING
    with open(vocabulary_file, "w", encoding="utf-8") as f:
        for line in vocabulary:
            f.write(line + "\n")

    generate_deck(vocabulary)

    print(f"✅ Deck Updated: {deck_name}.apkg")

    
