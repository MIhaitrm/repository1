from erori.eroare_validare import EroareValidare


class ValidatorEchipa:

    def valideaza_echipa(self,echipa):
        """

        :param echipa:
        :return:
        """
        erori = ""
        if echipa.get_id_echipa()<0:
            erori += "id invalid!\n"
        if echipa.get_nume() == "":
            erori += "nume invalid!\n"
        if len(erori) > 0:
            raise EroareValidare(erori)