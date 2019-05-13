from random_word import RandomWords


def get_band_name(optional_word):
    r = RandomWords()
    random_word = str(r.get_random_word())
    random_word2 = str(r.get_random_word())
    and_the = "and the"
    band_name = optional_word + " " + and_the + " " + random_word + " " + random_word2
    return band_name
