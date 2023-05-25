import string
from timeit import timeit
from collections import defaultdict
from ctypes import CDLL, c_char_p

# Load the shared library
lib = CDLL("./lib.so")

# Define the argument and return types of the function
lib.convert_str.argtypes = [c_char_p]
lib.convert_str.restype = c_char_p


def convert_str(str):
    return lib.convert_str(str.encode()).decode()


def word_frequency(paragraph: list[str]) -> dict:
    frequency = defaultdict(int)
    translation_table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    words = " ".join(paragraph).translate(translation_table).lower().split(' ')
    for word in words:
        if word:
            frequency[word] += 1
    
    return dict(frequency)


def c_word_frequency(paragraph: list[str]) -> dict:
    """
    Using punctuation replace and replace multi spaces by ctypes
    """
    frequency = defaultdict(int)
    words = " ".join(paragraph)

    for word in convert_str(words).split(' '):
        if word:
            frequency[word] += 1
    
    return dict(frequency)




paragraph = [
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away.././,try/././21",
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away.the",
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away."
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away.",
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away.",
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away.",
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away."
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away.",
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away.",
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away.",
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away."
    "The quick brown fox",
    "jumps over the lazy dog.",
    "The dog barks,",
    "and the fox runs away.",
]

print(f'Time for python code: {timeit(lambda: word_frequency(paragraph), number=1)}')
print(f'Time for python code with c: {timeit(lambda: c_word_frequency(paragraph), number=1)}')

print(word_frequency(paragraph))
print(c_word_frequency(paragraph))
