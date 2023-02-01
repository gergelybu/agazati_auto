import bevezetes
import sorozat
import epuletek

lotto = []

bevezetes.bevezeto()
sorozat.huzas(lotto)
epuletek.beolvas("auto.txt")
print("III/Flotta")
print(f"\tAutók száma: {epuletek.flotta()}")
epuletek.legfiatalabb()
