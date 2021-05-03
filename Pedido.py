class Pedido:

    def __init__(self, paciente, medicamentos):        
        self.paciente = paciente
        self.medicamentos = []

    #Get

    def getPaciente(self):
        return self.paciente

    def Agregar_Carrito(self, objeto):
        self.medicamentos.append(objeto)        

    #Set

    def setPaciente(self, paciente):
        self.paciente = paciente
