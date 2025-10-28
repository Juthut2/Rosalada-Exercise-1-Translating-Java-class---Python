class GamayNgaIro:
    
    def __init__(self, ngalan_iro, edad_iro):
        self.ngalan_iro = ngalan_iro
        self.edad_iro = edad_iro

    def tingog(self):
        print("Aw! Aw!")

    def adlawng_natawhan(self):
        self.edad_iro += 1
        print(f"Malipayong adlawng natawhan! Si {self.ngalan_iro} karon kay {self.edad_iro} anyos na.")

    def ipakita_detalyado(self):
        return f"Ngalan sa Iro: {self.ngalan_iro}, Edad: {self.edad_iro}"

if __name__ == "__main__":
    akong_iro = GamayNgaIro("Max", 5)
    akong_iro.tingog()
    akong_iro.adlawng_natawhan()
    print(akong_iro.ipakita_detalyado())
