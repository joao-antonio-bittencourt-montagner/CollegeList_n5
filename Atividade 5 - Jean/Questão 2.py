def complemento_dna(dna):
    complemento = {"A": "T", "C": "G", "G": "C", "T": "A"}
    return ''.join([complemento[base] for base in dna])

dna = input("Digite a sequencia de DNA: ").upper()
print('A sequência é: ',dna)
print("A sequncia complementar é:", complemento_dna(dna))