class Facturas:

    def __init__(self, fecha, paciente, doctor, precio_c, costo_o, costo_i, total):
        self.fecha = fecha        
        self.paciente = paciente
        self.doctor = doctor
        self.precio_c = precio_c
        self.costo_o = costo_o
        self.costo_i = costo_i
        self.total = total

    #Get
    def getFecha(self):
        return self.fecha

    def getPaciente(self):
        return self.paciente

    def getDoctor(self):
        return self.doctor
    
    def getPrecio_c(self):
        return self.precio_c

    def getCosto_o(self):
        return self.costo_o

    def getCosto_i(self):
        return self.costo_i

    def getTotal(self):
        return self.total

    #Set
    def setFecha(self, fecha):
        self.fecha = fecha

    def setPaciente(self, paciente):
        self.paciente = paciente
    
    def setDoctor(self, doctor):
        self.doctor = doctor
    
    def setPrecio_c(self, precio_c):
        self.precio_c = precio_c

    def setCosto_o(self, costo_o):
        self.costo_o = costo_o
        
    def setCosto_i(self, costo_i):
        self.costo_i = costo_i

    def setTotal(self, total):
        self.total = total
