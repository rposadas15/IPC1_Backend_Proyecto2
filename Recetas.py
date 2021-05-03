class Recetas:

    def __init__(self, nombre, fecha, paciente, padecimiento, descripcion):
        self.nombre = nombre
        self.fecha = fecha        
        self.paciente = paciente
        self.padecimiento = padecimiento
        self.descripcion = descripcion

    #Get
    def getNombre(self):
        return self.nombre

    def getFecha(self):
        return self.fecha

    def getPaciente(self):
        return self.paciente
    
    def getPadecimiento(self):
        return self.padecimiento

    def getDescripcion(self):
        return self.descripcion

    #Set
    def setNombre(self, nombre):
        self.nombre = nombre

    def setFecha(self, fecha):
        self.fecha = fecha
    
    def setPaciente(self, paciente):
        self.paciente = paciente
    
    def setPadecimiento(self, padecimiento):
        self.padecimiento = padecimiento

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion