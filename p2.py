def sortSentence(s: str) -> str:
    return ' '.join([w[:-1] for w in sorted(s.split(), key=lambda x: x[-1])])

print(sortSentence("is2 sentence4 This1 a3"))