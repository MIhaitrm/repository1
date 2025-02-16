from domeniu.echipa import Echipa
from teste.teste import Teste

teste = Teste()
teste.ruleaza_toate_teste()


with open("gigi.txt","a") as f:
    nume_echipe = ["rapid","dinamo","steaua"]
    for i in range(len(nume_echipe)):
        echipa = Echipa(i, nume_echipe[i])
        f.write(str(echipa)+"\n")

with open("gigi.txt","r") as f:
    lines = f.readlines()
    echipe = []
    for line in lines:
        line = line.strip()
        parts = line.split(",")
        id_echipa = int(parts[0])
        nume = parts[1]
        echipa = Echipa(id_echipa, nume)
        echipe.append(echipa)


for echipa in echipe:
    print(echipa)
