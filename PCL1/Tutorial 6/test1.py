a = 2
result = {}
result.update({"a":a})
a = 69
result.update({"a":a})

def ddp(adj, noun):
    for word in noun:
        if word[-5:] == "iness":
            base = word[:-5] + "y"
            if base in adj:
                result.update({word: base})
        if (word[-4:] == "ness"):
            base = word[:-4]
            if base in adj:
                result.update({word: base})
                
    return result

if __name__ == "__main__":
    adjectives = ["happy", "sad", "angry", "kind", "dark"]
    nouns = ["happiness", "sadness", "anger", "kindness", "darkness", "joyfulness"]
    
    print(ddp(adjectives, nouns))