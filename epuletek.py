from auto import Auto

auto_lista = []

def beolvas(fajlnev):
    fajlom = open(fajlnev, "r", encoding='UTF-8')
    fejlec = fajlom.readline().strip()
    sorok = fajlom.readlines()
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("$")
        auto_lista.append(Auto(sor))
        i += 1
    fajlom.close()


def flotta():
    i = 0
    db = 0
    while i < len(auto_lista):
        db += 1
        i += 1
    return db

def legfiatalabb():
    i = 0
    fiatal = 0
    while i < len(auto_lista):
        if auto_lista[fiatal].gyartasi_datum < auto_lista[i].gyartasi_datum:
            fiatal = i
        i += 1
    print("III/Legfiatalabb")
    print(f"\t A legfiatalabb autó: {auto_lista[fiatal].nev}({auto_lista[fiatal].gyartasi_datum})")