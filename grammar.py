import general
production = {
    "K" : ['S P','O P','S Ket','O Ket','S P Pel','S P Ket','O P Pel','O P Ket','S P O','S P S','O P S','O P O','S P O Pel','O P O Pel','O P S Pel','S P S Pel','S P O Ket','O P O Ket','O P S Ket','S P S Ket'],
    "S" : ['NP'],
    "P" : ['VP','AdjP'],
    "O" : ['NP','VP','Adv NP'],
    "Pel" : ['AdjP', 'PP'],
    "Ket" : ['PP','AdjP','NP','VP','Adv'],
    "NP" : ['PropNoun','NP Noun','Pronoun','Noun','Num NP','NP Pronoun','NP PropNoun','Num','NP Adj','NP VP','NP Adv','Adv NP','Adj NP','Noun NP','NumP NP','NP PP','NP Num'],
    "VP" : ['Verb','Adv','Adj','Adv VP','AdjP VP','VP Verb','VP Pronoun','VP Noun','VP NP','Adv Verb'],
    "AdjP" : ['Adj','Adv AdjP','Adj Adv','Adj Pronoun','Adj Noun','AdjP NP','AdjP NumP'],
    "PP" : ['Prep NP','Prep AdjP','Prep Num','Prep','PP NP','PP VP','Pronoun','PP AdjP','Prep PropNoun','Prep NumP'],
    "Verb" : general.kata_kerja,
    "Noun" : general.kata_benda,
    "Adj" : general.kata_sifat,
    "Adv" : general.kata_keterangan,
    "Num" : general.numeralia,
    "Prep" : general.preposisi,
    "PropNoun" : general.proper_noun,
    "Pronoun" : general.kata_ganti
}
main_production = {
    "S" : ['NP'],
    "P" : ['VP','AdjP'],
    "O" : ['NP','VP','Adv NP'],
    "Pel" : ['AdjP', 'PP'],
    "Ket" : ['PP','AdjP','NP','VP','Adv']
}
variable = list(production.keys())
start_symbol = ["K"]
def check_production(array):
    count = []
    for i in array:
        for j in variable:
            if i in production[j]:
                count.append(j)
    return count

def check_symbol(array):
    for i in array:
        if i in start_symbol:
            return True
    return False