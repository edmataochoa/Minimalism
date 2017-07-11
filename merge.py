class Word:
    """docstring for ."""
    def __init__(self, lexical_item):
        #super(, self).__init__()
        self.name = name
        self.category = "TBD"

lexicon = {
"house" :   ["N", "sg"],
"to be" :   ["V"],
"red"   :   ["ADJ", "color"]
}

def merge(a, *args):
    sequence = ""
    if args:
        sequence += a
        for word in args:
            sequence += " " + word
        return sequence
    else:
        return a

def get_category(word):
    try:
        pos = lexicon.get(word)[0]
    except:
        return "The Lexicon has not yet learned " + word.upper()
    result = "Grammatical category for " + word.upper() + ": "
    if pos == "V":
        return result + "verb"
    elif pos == "N":
        return result + "noun"
    elif pos == "ADJ":
        return result + "adjective"

print(merge("house"))

# print(get_category("to be"))
# print(get_category("house"))
# print(get_category("red"))
# print(get_category("blue"))
