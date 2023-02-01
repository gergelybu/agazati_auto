import random

def huzas(lotto):
    i = 0
    while i < 5:
        huzas = random.randint(1, 90)
        if i < 4:
            print(huzas, end=" ; ")
        else:
            print(huzas)
        lotto.append(huzas)
        i += 1
    egyjegyuek = egyjegyuek_szama(lotto)
    konzol_kiir(egyjegyuek)
    file_kiir(lotto)


def egyjegyuek_szama(lotto):
    i = 0
    db = 0
    while i < len(lotto):
        if lotto[i] < 10:
            db += 1
        i += 1
    return db

def konzol_kiir(kiiras):
	print(f"Az egyjegyűek száma: {kiiras}")

def file_kiir(lotto):
    i = 0
    fajl = open("szamok.txt", "w")
    while i < len(lotto):
        if i < 4:
            szoveg = str(lotto[i]) + ", "
            fajl.write(szoveg)
        else:
            szoveg = str(lotto[i]) + "\n"
            fajl.write(szoveg)
        i += 1
    fajl.close