import pandas as pd

class Materias:
    def __init__(self):
        self.materias = {}

    def agregar_materia(self, nombre_materia):
        self.materias[nombre_materia] = []

    def agregar_nota(self, nombre_materia, nota):
        if nombre_materia in self.materias:
            self.materias[nombre_materia].append(nota)
        else:
            print("La materia", nombre_materia, "no está registrada.")

    def obtener_promedio(self, nombre_materia):
        if nombre_materia in self.materias:
            notas = self.materias[nombre_materia]
            total_notas = sum(notas)
            cantidad_notas = len(notas)
            promedio = total_notas / cantidad_notas
            return promedio
        else:
            print("La materia", nombre_materia, "no está registrada.")


class Estudiante:
    def __init__(self, nombre, edad, ID, curso):
        self.nombre = nombre
        self.edad = edad
        self.ID = ID
        self.curso = curso
        self.materias = Materias()

    def agregar_materia(self, nombre_materia):
        self.materias.agregar_materia(nombre_materia)

    def agregar_nota(self, nombre_materia, nota):
        self.materias.agregar_nota(nombre_materia, nota)

    def obtener_promedio_materia(self, nombre_materia):
        return self.materias.obtener_promedio(nombre_materia)

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("ID:", self.ID)
        print("Curso:", self.curso)
        print("Materias y promedios:")

        for nombre_materia in self.materias.materias:
            promedio = self.materias.obtener_promedio(nombre_materia)
            print(nombre_materia + ":", promedio)


def cargar_estudiantes_desde_excel():
    try:
        estudiantes_df = pd.read_excel("estudiantes.xlsx", sheet_name="Estudiantes")
        notas_df = pd.read_excel("estudiantes.xlsx", sheet_name="Notas")
    except FileNotFoundError:
        print("No se encontró el archivo 'estudiantes.xlsx'.")
        return []

    estudiantes = {}
    for _, estudiante in estudiantes_df.iterrows():
        ID = estudiante.get("ID")
        nombre = estudiante.get("Nombre")
        edad = estudiante.get("Edad")
        curso = estudiante.get("Curso")

        if ID and nombre and edad and curso:
            nuevo_estudiante = Estudiante(nombre, edad, ID, curso)
            estudiantes[ID] = nuevo_estudiante
        else:
            print("Datos incompletos para un estudiante.")

    for _, nota in notas_df.iterrows():
        ID = estudiante.get("ID")
        nombre = estudiante.get("Nombre")
        edad = estudiante.get("Edad")
        curso = estudiante.get("Curso")

        if ID and nombre and edad and curso:
            nuevo_estudiante = Estudiante(nombre, edad, ID, curso)
            estudiantes[ID] = nuevo_estudiante
        else:
            print("Datos incompletos para un estudiante.")

    for _, nota in notas_df.iterrows():
        ID = nota.get("ID")
        materia = nota.get("Materia")
        nota_valor = nota.get("Nota")

        if ID and materia and nota_valor:
            estudiante = estudiantes.get(ID)
            if estudiante:
                estudiante.agregar_materia(materia)
                estudiante.agregar_nota(materia, nota_valor)
            else:
                print("No se encontró el estudiante con ID:", ID)
        else:
            print("Datos incompletos para una nota.")

    return list(estudiantes.values())

if __name__ == "__main__":
    estudiantes = cargar_estudiantes_desde_excel()

    if estudiantes:
        for estudiante in estudiantes:
            estudiante.mostrar_informacion()
    else:
        print("No se cargaron estudiantes.")

estudiante1 = Estudiante("Juan", 18, "123456", "Bachillerato")
estudiante1.agregar_materia("Matemáticas")
estudiante1.agregar_materia("Física")

estudiante1.agregar_nota("Matemáticas", 9.5)
estudiante1.agregar_nota("Matemáticas", 8.7)
estudiante1.agregar_nota("Física", 7.8)
estudiante1.agregar_nota("Física", 9.2)

estudiante1.mostrar_informacion()

