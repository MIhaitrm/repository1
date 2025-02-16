class Echipa:
    def __init__(self,id_echipa,nume):
        self.__id_echipa = id_echipa
        self.__nume = nume

    def get_id_echipa(self):
        return self.__id_echipa
    def get_nume(self):
        return self.__nume
    def set_nume(self,nume):
        self.__nume = nume

    def __str__(self):
        return f"{self.__id_echipa},{self.__nume}"