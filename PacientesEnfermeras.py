class PacientesEnfermeras:    
    
    def __init__(self, nombre, apellido, fecha, sexo, usuario, contraseña, telefono, pa_en):
        self.nombre = nombre
        self.apellido = apellido        
        self.fecha = fecha
        self.sexo = sexo
        self.usuario = usuario
        self.contraseña = contraseña
        self.telefono = telefono
        self.pa_en = pa_en        

    #Get
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getFecha(self):
        return self.fecha

    def getSexo(self):
        return self.sexo
    
    def getUsuario(self):
        return self.usuario
    
    def getContraseña(self):
        return self.contraseña

    def getTelefono(self):
        return self.telefono

    def getPa_En(self):
        return self.pa_en

    #Set
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setApellido(self, apellido):
        self.apellido = apellido
    
    def setFecha(self, fecha):
        self.fecha = fecha

    def setSexo(self, sexo):
        self.sexo = sexo
    
    def setUsuario(self, usuario):
        self.usuario = usuario
    
    def setContraseña(self, contraseña):
        self.contraseña = contraseña

    def setTelefono(self, telefono):
        self.telefono = telefono
    
    def setPa_En(self, pa_en):
        self.pa_en = pa_en
