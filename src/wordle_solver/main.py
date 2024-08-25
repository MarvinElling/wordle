# %%
import config

with open('words_de.txt', 'r') as f:
    global words
    words = f.read().splitlines()

words = [word.upper() for word in set(words) if len(word) == config.WORD_LENGTH]

def word_suggestor(
        good_letters: str,
        bad_letters: str,
        position: str,
        not_position: list[list[str|int]],
        ) -> list[str]:
    suggestions = [
        word for word in words
        if all(
            letter in good_letters or
            letter not in bad_letters
            for letter in word
        )
    ]
    return suggestions


if __name__ == '__main__':
    a = word_suggestor(
        good_letters="SPIEL",
        bad_letters="",
        position="",
        not_position=[],
    )
    print(a)