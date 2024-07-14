
# Anagram Detection 7kyu

def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    return sorted(test) == sorted(original)