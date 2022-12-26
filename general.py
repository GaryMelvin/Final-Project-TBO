file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\word\\verb.txt", "r")
kata_kerja = file.read().split("\n")
file.close()
file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\word\\noun.txt", "r")
kata_benda = file.read().split("\n")
file.close()
file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\word\\adj.txt", "r")
kata_sifat = file.read().split("\n")
file.close()
file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\word\\adv.txt", "r")
kata_keterangan = file.read().split("\n")
file.close()
file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\word\\num.txt", "r")
numeralia = file.read().split("\n")
file.close()
file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\word\\prep.txt", "r")
preposisi = file.read().split("\n")
file.close()
file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\word\\prop_noun.txt", "r")
proper_noun = file.read().split("\n")
file.close()
file = open("C:\\Users\\hp\\OneDrive\\Documents\\Belajar Pemrograman\\JAVA PBO\\TBO\\FP TBO\\word\\pronoun.txt", "r")
kata_ganti = file.read().split("\n")

file.close()

alphabet = kata_kerja + kata_benda + kata_sifat + kata_keterangan + numeralia + preposisi + proper_noun + kata_ganti

def check_alphabet(array):
    for i in array:
        if i not in alphabet:
            return False
    return True