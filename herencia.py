class Colegio:
    def __init__(self,colegio,comuna):
        self.colegio = colegio
        self.comuna = comuna


class Alumno(Colegio):
    def __init__(self,colegio,comuna,nombre,correo):
        super().__init__(colegio,comuna)
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"El Alumno {self.nombre} con email {self.correo}, esta en el liceo/colegio {self.colegio}\nQue esta en la comuna de {self.comuna}"

    def matricula(self):
        print("Matriculado")
        return self
    

jimmy = Alumno("CEAH","Quinta Normal","Jimmy Duarte", "jimmy@jimmy.cl")

print(jimmy)

jimmy.matricula()

