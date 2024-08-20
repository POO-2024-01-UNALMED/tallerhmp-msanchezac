from deportista import Deportista
from persona import Persona

class Futbolista(Deportista, Persona):
    listaFutbolistas = []

    def __init__(self, nombre, edad, altura, sexo, anos_practicando, goles_marcados, tarjetas_rojas, pierna_habil, deporte="Futbol"):
        super().__init__(nombre, edad, altura, sexo, anos_practicando, deporte)
        self.__goles_marcados = goles_marcados
        self.__tarjetas_rojas = tarjetas_rojas
        self.__pierna_habil = pierna_habil
        Futbolista.listaFutbolistas.append(self)

    def __str__(self):
        return f"Mi nombre es {self.get_nombre()} soy profesional en el deporte {self.get_deporte()} Tengo {self.get_edad()} años de edad y llevo {self.get_anos_practicando()} años en el deporte"    
 
    #snake_case
    def fet_goles_marcados(self):
        return self.__goles_marcados
    def set_goles_marcados(self, goles_marcados):
        self.__goles_marcados = goles_marcados

    def get_tarjetas_rojas(self):
        return self.__tarjetas_rojas
    def set_tarjetas_rojas(self, tarjetas_rojas):
        self.__tarjetas_rojas = tarjetas_rojas

    def get_pierna_habil(self):
        return self.__pierna_habil
    def set_pierna_habil(self, pierna_habil):
        self.__pierna_habil = pierna_habil

    #camelCase
    def getGolesMarcados(self):
        return self.__goles_marcados
    def setGolesMarcados(self, golesMarcados):
        self.__goles_marcados = golesMarcados

    def getTarjetasRojas(self):
        return self.__tarjetas_rojas
    def setTarjetasRojas(self, tarjetasRojas):
        self.__tarjetas_rojas = tarjetasRojas

    def getPiernaHabil(self):
        return self.__pierna_habil
    def setPiernaHabil(self, piernaHabil):
        self.__pierna_habil = piernaHabil    






