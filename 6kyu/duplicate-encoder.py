import collections
def duplicate_encode(word):
    count = collections.Counter(word.lower())
    result = ""
    for i in word:
        for e in count:
            if i.lower() == e.lower():
                if count[e] > 1:
                    result += ")"
                else:
                    result += "("
                
                
    return result
