class Citas:

    def __init__(self, fecha, hora, paciente, motivo, estado, doctor):
        self.fecha = fecha
        self.hora = hora
        self.paciente = paciente
        self.motivo = motivo
        self.estado = estado
        self.doctor = doctor

    #Get
    def getFecha(self):
        return self.fecha

    def getHora(self):
        return self.hora

    def getPaciente(self):
        return self.paciente
    
    def getMotivo(self):
        return self.motivo

    def getEstado(self):
        return self.estado

    def getDoctor(self):
        return self.doctor

    #Set
    def setFecha(self, fecha):
        self.fecha = fecha

    def setHora(self, hora):
        self.hora = hora
    
    def setPaciente(self, paciente):
        self.paciente = paciente
    
    def setMotivo(self, motivo):
        self.motivo = motivo

    def setEstado(self, estado):
        self.estado = estado

    def setDoctor(self, doctor):
        self.doctor = doctor
