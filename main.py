import regex
import numpy as np


def words(text):
    return regex.findall(r'\w+', text.lower())


WORDS = regex.split(r'[\n, ]', open('./dataset/word counter.txt', encoding='utf-8').read())
WORDS = dict(zip(WORDS[::2], list(map(int, WORDS[1::2]))))

def P(word, N=np.sum(np.array(list(WORDS.values())))):
    """Probability of `word`."""
    # print(WORDS[word])
    return WORDS[word] / N


def correction(word):
    """Most probable spelling correction for word."""
    return max(candidates(word), key=P)


def candidates(word):
    """Generate possible spelling corrections for word."""
    return known([word]) or known(edits1(word)) or known(edits2(word)) or [word]


def known(words):
    """The subset of `words` that appear in the dictionary of WORDS."""
    return set(w for w in words if w in WORDS)


def edits1(word):
    """All edits that are one edit away from `word`."""
    letters = 'აბგდევზთიკლმნოპჟრსტუფქღყშჩცძწჭყხჯჰ'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    """All edits that are two edits away from `word`."""
    tmp = (e2 for e1 in edits1(word) for e2 in edits1(e1))
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

word = 'სწვავე'
print(correction(word))
# print(edits2(word))
