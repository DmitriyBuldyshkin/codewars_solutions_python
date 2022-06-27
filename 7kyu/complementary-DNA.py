def DNA_strand(dna):
    symbols = {"A": "T", "T": "A", "C": "G", "G":"C"}
    res = ""
    for let in dna:
        if let in symbols:
            res += symbols[let]
    return res
