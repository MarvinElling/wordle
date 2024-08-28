# %%
import config

with open('src/wordle_solver/words_de.txt', 'r') as f:
    global words
    words = f.read().splitlines()

words = [word.upper() for word in set(words) if len(word) == config.WORD_LENGTH]
# words = [
#     'SAUGT', 'SORGE', 'FADEN', 
#     'TRAUM', 'TEILE',
#     # 'SIPPE', 'HOCHS', 'SIEHE', 
#     # 'SUGAR', 'RAUCH', 'CHILI', 
#     # 'ETATS', 'LIANE', 'ADNAN', 
#     'GANGS', 'YAHOO', 'SPIEL',
# ]

def word_suggestor(
        good_letters: str,
        bad_letters: str,
        position: str,
        not_position: list[list[str|int]],
        ) -> list[str]:
    _ = ''
    suggestions = [
        word for word in words
        if all(
            letter in good_letters and
            letter not in bad_letters
            for letter in word
        )
    ]
    filtered_suggestions = []
    for word in suggestions:
        if all(letter in word for letter in good_letters):
            filtered_suggestions.append(word)
    suggestions = list(set(filtered_suggestions))
    return suggestions


if __name__ == '__main__':
    a = word_suggestor(
        good_letters="SPIE",
        bad_letters="",
        position="",
        not_position=[],
    )
    print(a)