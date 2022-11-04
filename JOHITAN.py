class equipos:
    def _init_(self, TAMANO, ALTURA, PROGRAMACION, FUNCION, COLOR):
        self.TAMANO=TAMANO
        self.ALTURA=ALTURA
        self.PROGRAMACION=PROGRAMACION
        self.FUNCION=FUNCION
        self.COLOR=COLOR
        
Barcelona = equipos("Grande", "1.80", "Phyton", "RECOGER BASURA", "PLATEADO")

print(Barcelona.TAMANO)
print(Barcelona.ALTURA)
print(Barcelona.PROGRAMACION)
print(Barcelona.FUNCION)
print(Barcelona.COLOR)