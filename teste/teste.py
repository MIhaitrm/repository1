
from domeniu.echipa import Echipa
from erori.eroare_validare import EroareValidare
from validare.validator_echipa import ValidatorEchipa


class Teste:

    def ruleaza_toate_teste(self):
        print("incepem testele...")
        self.__ruleaza_teste_domeniu()
        self.__ruleaza_teste_validare()
        print("teste finalizate cu succes!")

    def __ruleaza_teste_domeniu(self):
        print("incepem testele pentru domeniu...")
        id_echipa = 23
        nume = "Gigi"
        echipa = Echipa(id_echipa,nume)
        assert echipa.get_id_echipa() == 23
        assert echipa.get_nume() == nume
        print("teste domeniu finalizate cu succes!")

    def __ruleaza_teste_validare(self):
        print("incepem testele pentru validare...")
        id_echipa = 23
        nume = "Gigi"
        echipa = Echipa(id_echipa,nume)
        validator_echipa = ValidatorEchipa()
        validator_echipa.valideaza_echipa(echipa)
        id_echipa_rau = -23
        nume_rau = ""
        echipa_rea = Echipa(id_echipa_rau, nume_rau)
        try:
            validator_echipa.valideaza_echipa(echipa_rea)
            assert False
        except EroareValidare as e:
            assert str(e) == "id invalid!\nnume invalid!\n"
        print("testele validare finalizate cu succes!")