class Motor:
    def __init__(self,tipo_motor):
        if tipo_motor == 1:
            self.consumo = 7
            self.costo = 5
            self.potencia = 1
        elif tipo_motor == 2:
            self.consumo = 14
            self.costo = 7
            self.potencia = 2
        else:
            self.consumo = 21
            self.costo = 9
            self.potencia = 3