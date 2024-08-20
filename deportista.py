from persona import Persona

class Deportista(Persona):
    def __init__(self, nombre, edad, altura, sexo, anos_practicando, deporte = "Futbol"):
        super().__init__(nombre, edad, altura, sexo)
        self.__deporte = deporte
        self.__anosPracticando = anos_practicando

        #snake_case
        def get_deporte(self):
            return self.__deporte
        def set_deporte(self, deporte):
            self.__deporte = deporte

        def get_anos_practicando(self):
            return self._anosPracticando
        def set_anos_practicando(self, anosPracticando):
            self._anosPracticando = anosPracticando

        #camelcase
        def getDeporte(self):
            return self.__deporte
        def setDeporte(self, deporte):
            self.__deporte = deporte

        def getAñosPracticando(self):
            return self.__anosPracticando
        def setAñosPracticando(self, anosPracticando):
            self.__anosPracticando = anosPracticando        