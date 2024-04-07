from enum import Enum

class Universidad:
    def __init__(self):
        self.investigadores = []
        self.titulares = []
        self.asociados = []
        self.estudiantes = []

    def altaInvestigador(self, investigador):
        if investigador in self.investigadores:
            print(f"Investigador {investigador.nombre} ya existe.")
            return
        self.investigadores.append(investigador)

    def eliminarInvestigador(self, investigador):
        try:
            self.investigadores.remove(investigador)
        except ValueError:
            raise ValueError("El investigador no está registrado")
        
    def listInvestigadores(self):
        return self.investigadores

    def altaTitular(self, titular):
        if titular in self.titulares:
            print(f"Titular {titular.nombre} ya existe.")
            return
        self.titulares.append(titular)

    def eliminarTitular(self, titular):
        try:
            self.titulares.remove(titular)
        except ValueError:
            raise ValueError("El titular no está registrado")

    def listTitulares(self):
        return self.titulares
    
    def altaAsociado(self, asociado):
        if asociado in self.asociados:
            print(f"Asociado {asociado.nombre} ya existe.")
            return
        self.asociados.append(asociado)

    def eliminarAsociado(self, asociado):
        try:
            self.asociados.remove(asociado)
        except ValueError:
            raise ValueError("El asociado no está registrado")

    def listAsociados(self):
        return self.asociados
    
    def altaEstudiante(self, estudiante):
        if estudiante in self.estudiantes:
            print(f"Estudiante {estudiante.nombre} ya existe.")
            return
        self.estudiantes.append(estudiante)

    def eliminarEstudiante(self, estudiante):
        try:
            self.estudiantes.remove(estudiante)
        except ValueError:
            raise ValueError("El estudiante no está registrado")

    def listEstudiantes(self):
        return self.estudiantes

class Persona:
    def __init__(self, nombre, dni, direccion, sexo):
        self.nombre = nombre
        self.dni = dni
        self.direccion = direccion
        if sexo not in ['V', 'M']:
            raise ValueError("El sexo debe ser 'V' o 'M'.")
        self.sexo = sexo

    def devuelveDatos(self):
        return f"Nombre: {self.nombre}, DNI: {self.dni}, Dirección: {self.direccion}, Sexo: {self.sexo}"


class Estudiante(Persona):
    def __init__(self, nombre, dni, direccion, sexo):
        Persona.__init__(self,nombre, dni, direccion, sexo)
        self.asignaturas = []

    def listAsignaturas(self):
        return self.asignaturas

    def añadirAsignaturas(self, asignatura):
        if asignatura in self.asignaturas:
            print(f"Asignatura {asignatura} ya existe en las asignaturas de {self.nombre}.")
            return
        self.asignaturas.append(asignatura)
        print(f"{asignatura} ha sido añadida a las asignaturas de {self.nombre}.")

    def eliminarAsignaturas(self, asignatura):
        try:
            self.asignaturas.remove(asignatura)
            print(f"{asignatura} ha sido eliminada de las asignaturas de {self.nombre}.")
        except ValueError:
            print(f"{asignatura} no está en las asignaturas de {self.nombre}.")

class Departamento():
    DIIC = 1
    DITEC = 2
    DIS = 3


class Miembro(Persona):
    def __init__(self, nombre, dni, direccion, sexo, departamento):
        Persona.__init__(self, nombre, dni, direccion, sexo)
        self.departamento = departamento

    def cambiarDepartamento(self, departamento):
        if departamento != self.departamento:
            self.departamento = departamento
        else:
            print("El miembro ya pertenece a este departamento.")

    def datos(self):
        return f"{Persona.devuelveDatos(self)}, Departamento: {self.departamento}"

class ProfesorAsociado(Miembro):
    def __init__(self, nombre, dni, direccion, sexo, departamento):
        Miembro.__init__(self,nombre, dni, direccion, sexo, departamento)
        self.asignaturas = []

    def listAsignaturas(self):
        return self.asignaturas

    def añadirAsignaturas(self, asignatura):
        if asignatura in self.asignaturas:
            print(f"Asignatura {asignatura} ya existe en las asignaturas de {self.nombre}.")
            return
        self.asignaturas.append(asignatura)
        print(f"{asignatura} ha sido añadida a las asignaturas de {self.nombre}.")

    def eliminarAsignaturas(self, asignatura):
        try:
            self.asignaturas.remove(asignatura)
            print(f"{asignatura} ha sido eliminada de las asignaturas de {self.nombre}.")
        except ValueError:
            print(f"{asignatura} no está en las asignaturas de {self.nombre}.")


class Investigador(Miembro):
    def __init__(self, nombre, dni, direccion, sexo, departamento, area):
        Miembro.__init__(self,nombre, dni, direccion, sexo, departamento)
        self.area = area

    def cambiarArea(self, area):
        if area != self.area:
            self.area = area
        else:
            print("El miembro ya pertenece a este área.")

    def datos(self):
        return f"{Miembro.datos(self)}, Área: {self.area}"