import re

def count_bits(n):
    bits = "{0:b}".format(n)
    return sum([int(i) for i in str(bits)])

def likes(names):
    if len(names) == 1:
        return f"{names[0]} likes this"
    elif 1 < len(names) < 4:
        return f"{', '.join(names[:-1])} and {names[-1]} like this"
    elif len(names) >= 4:
        return f"{', '.join(names[:2])} and {len(names) - 2} others like this"
    else:
        return "no one likes this"

def disemvowel(string_: str):
    return re.sub(r'[aeiouAEIOU]', '', string_)

def get_count(sentence):
    return len([w for w in sentence if w in "aeiouAEIOU"])

def duplicate_encode(word):
    word = word.lower()
    new_word = ""
    for c in word:
        if not re.search("[a-zA-Z]", c):
            regex = "\\" + c
        else:
            regex = c
        iterations = re.findall(regex, word)
        if  len(iterations) > 1:
            new_word += ")"
        else:
            new_word += "("
    return new_word

def duplicate_encode2(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

