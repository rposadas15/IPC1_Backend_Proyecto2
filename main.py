from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from PacientesEnfermeras import PacientesEnfermeras
Pacientes_Enfermeras = []
# 0 = pacientes
# 1 = enfermeros

from Administrador import Administrador
admin = []

from Doctores import Doctores
doctores = []

from Medicamentos import Medicamentos
medicamentos = []

from Citas import Citas
citas = []

from Pedido import Pedido
pedido = []

from Facturas import Facturas
facturas = []

from Recetas import Recetas
recetas = []

admin.append(Administrador("Carlos", "Jimenez", "admin", "1234"))

#QUITAR
#Pacientes_Enfermeras.append(PacientesEnfermeras('Ronaldo', 'Posadas', '07/07/2002', 'M', 'rposadas_15', '1234', 55258925, 0))
#Pacientes_Enfermeras.append(PacientesEnfermeras('Ronaldo', 'Posadas', '07/07/2002', 'M', 'jaime', '1234', 55258925, 0))
#Pacientes_Enfermeras.append(PacientesEnfermeras('Javier', 'Guerra', '08/08/2003', 'M', 'javier15', '1234', 22156568, 1))
#doctores.append(Doctores('Ronaldo', 'Posadas', '07/07/2002', 'M', 'juan_15', '1234', 'Pediatra', 55258925))
#doctores.append(Doctores('Emiliana', 'Posadas', '07/07/2002', 'F', 'emi15', '1234', 'Pediatra', 55258925))
#medicamentos.append(Medicamentos('Parazetamol', 120.2, 'Dolor de cabeza', 50))
#medicamentos.append(Medicamentos('Hola', 100.2, 'Dolor de cabeza', 50))
#--

app = Flask(__name__)
CORS(app)

@app.route('/', methods = ['GET'])
def inicio():
    print("empezamos")
    return("<h1>EMEPEZAMOS</h1>")

#ADMINISTRADOR

@app.route('/Administrador', methods=['GET'])
def ObtenerAdministradores():
    global admin
    Datos = []
    for persona in admin:
        objeto = {
            'Nombre': persona.getNombre(),
            'Apellido': persona.getApellido(),                
            'Usuario': persona.getUsuario(),
            'Password': persona.getContraseña()                
        }
        Datos.append(objeto)            
    return(jsonify(Datos))

@app.route('/Administrador/<string:usuario>', methods=['GET'])
def ObtenerPersona(usuario): 
    global admin
    for persona in admin:
        if persona.getUsuario() == usuario:
            objeto = {
            'Nombre': persona.getNombre(),
            'Apellido': persona.getApellido(),
            'Usuario': persona.getUsuario(),
            'Password': persona.getContraseña()
            }
            return(jsonify(objeto))
    salida = { "Mensaje": "No existe el Administrador con ese usuario"}
    return(jsonify(salida))

@app.route('/Administrador', methods=['POST'])
def AgregarAdministrador():
    global admin
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    usuario = request.json['usuario']    
    password = request.json['password']
    nuevo = Administrador(nombre, apellido, usuario, password)
    admin.append(nuevo)
    return jsonify({'Mensaje':'Se agrego al Administrador exitosamente',})

@app.route('/Administrador/<string:nombre>', methods=['PUT'])
def ActualizarAdministrador(nombre):
    global admin
    for i in range(len(admin)):
        if nombre == admin[i].getUsuario():
            admin[i].setNombre(request.json['nombre'])
            admin[i].setApellido(request.json['apellido'])
            admin[i].setUsuario(request.json['usuario'])
            admin[i].setContraseña(request.json['password'])
            return jsonify({'Mensaje':'Se actualizo al Administrador exitosamente'})
    return jsonify({'Mensaje':'No se encontro al Administrador para actualizar'})

@app.route('/Administrador/<string:nombre>', methods=['DELETE'])
def EliminarAdministrador(nombre):
    global admin
    for i in range(len(admin)):
        if nombre == admin[i].getUsuario():
            del admin[i]
            return jsonify({'Mensaje':'Se elimino ad Administrador exitosamente'})
    return jsonify({'Mensaje':'No se encontro al Adminstrador para eliminar'})

#PACIENTES

@app.route('/Pacientes', methods=['GET'])
def ObtenerPacientes():
    global Pacientes_Enfermeras
    Datos = []
    for persona in Pacientes_Enfermeras:
        if persona.getPa_En() == 0:
            objeto = {
                'Nombre': persona.getNombre(),
                'Apellido': persona.getApellido(),
                'Fecha': persona.getFecha(),
                'Sexo': persona.getSexo(),
                'Usuario': persona.getUsuario(),
                'Password': persona.getContraseña(),
                'Telefono': persona.getTelefono(),
                'Paciente': persona.getPa_En()
            }
            Datos.append(objeto)            
    return(jsonify(Datos))

@app.route('/Pacientes/<string:usuario>', methods=['GET'])
def ObtenerPaciente(usuario):    
    global Pacientes_Enfermeras
    for persona in Pacientes_Enfermeras:        
        if persona.getUsuario() == usuario and persona.getPa_En() == 0:
            objeto = {
            'Nombre': persona.getNombre(),
            'Apellido': persona.getApellido(),
            'Fecha': persona.getFecha(),
            'Sexo': persona.getSexo(),
            'Usuario': persona.getUsuario(),
            'Password': persona.getContraseña(),
            'Telefono': persona.getTelefono(),
            'Paciente': persona.getPa_En()
            }
            return(jsonify(objeto))
    salida = {"Mensaje": "No existe el paciente con ese nombre"}
    return(jsonify(salida))

@app.route('/Pacientes', methods=['POST'])
def AgregarPacientes():
    global Pacientes_Enfermeras
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    fecha = request.json['fecha']
    sexo = request.json['sexo']
    usuario = request.json['usuario']    
    password = request.json['password']
    telefono = int(request.json['telefono'])
    paciente = 0
    nuevo = PacientesEnfermeras(nombre, apellido, fecha, sexo, usuario, password, telefono, paciente)
    Pacientes_Enfermeras.append(nuevo)
    return jsonify({'Mensaje':'Se agrego al Paciente exitosamente',})

@app.route('/Pacientes/<string:usuario>', methods=['PUT'])
def ActualizarPaciente(usuario):
    global Pacientes_Enfermeras
    for i in range(len(Pacientes_Enfermeras)):
        if usuario == Pacientes_Enfermeras[i].getUsuario():
            Pacientes_Enfermeras[i].setNombre(request.json['nombre'])
            Pacientes_Enfermeras[i].setApellido(request.json['apellido'])
            Pacientes_Enfermeras[i].setFecha(request.json['fecha'])
            Pacientes_Enfermeras[i].setSexo(request.json['sexo'])
            Pacientes_Enfermeras[i].setUsuario(request.json['usuario'])
            Pacientes_Enfermeras[i].setContraseña(request.json['password'])
            Pacientes_Enfermeras[i].setTelefono(int(request.json['telefono']))
            return jsonify({'Mensaje':'Se actualizo al Paciente exitosamente'})
    return jsonify({'Mensaje':'No se encontro al Paciente para actualizar'})

@app.route('/Pacientes/<string:usuario>', methods=['DELETE'])
def EliminarPaciente(usuario):
    global Pacientes_Enfermeras
    for i in range(len(Pacientes_Enfermeras)):
        if usuario == Pacientes_Enfermeras[i].getUsuario():
            del Pacientes_Enfermeras[i]
            return jsonify({'Mensaje':'Se elimino al Paciente exitosamente'})
    return jsonify({'Mensaje':'No se encontro al Paciente para eliminar'})

#ENFERMEROS

@app.route('/Enfermeros', methods=['GET'])
def ObetnerEnfermera():
    global Pacientes_Enfermeras
    Datos = []
    for persona in Pacientes_Enfermeras:
        if persona.getPa_En() == 1:
            objeto = {
                'Nombre': persona.getNombre(),
                'Apellido': persona.getApellido(),
                'Fecha': persona.getFecha(),
                'Sexo': persona.getSexo(),
                'Usuario': persona.getUsuario(),
                'Password': persona.getContraseña(),
                'Telefono': persona.getTelefono(),
                'Paciente': persona.getPa_En()
            }
            Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/Enfermeros/<string:usuario>', methods=['GET'])
def ObtenerEnfermera(usuario):
    global Pacientes_Enfermeras    
    for persona in Pacientes_Enfermeras:        
        if persona.getUsuario() == usuario and persona.getPa_En() == 1:
            objeto = {
                'Nombre': persona.getNombre(),
                'Apellido': persona.getApellido(),
                'Fecha': persona.getFecha(),
                'Sexo': persona.getSexo(),
                'Usuario': persona.getUsuario(),
                'Password': persona.getContraseña(),
                'Telefono': persona.getTelefono(),
                'Paciente': persona.getPa_En()
            }
            return(jsonify(objeto))
    salida = {"Mensaje": "No existe el Enfermero con ese nombre"}
    return(jsonify(salida))

@app.route('/Enfermeros', methods=['POST'])
def AgregarEnfermeras():
    global Pacientes_Enfermeras
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    fecha = request.json['fecha']
    sexo = request.json['sexo']
    usuario = request.json['usuario']    
    password = request.json['password']
    telefono = int(request.json['telefono'])
    paciente = 1
    nuevo = PacientesEnfermeras(nombre, apellido, fecha, sexo, usuario, password, telefono, paciente)
    Pacientes_Enfermeras.append(nuevo)
    return jsonify({'Mensaje':'Se agrego la Enfermero exitosamente',})

@app.route('/Enfermeros/<string:usuario>', methods=['PUT'])
def ActualizarEnfermera(usuario):
    global Pacientes_Enfermeras
    for i in range(len(Pacientes_Enfermeras)):
        if usuario == Pacientes_Enfermeras[i].getUsuario():
            Pacientes_Enfermeras[i].setNombre(request.json['nombre'])
            Pacientes_Enfermeras[i].setApellido(request.json['apellido'])
            Pacientes_Enfermeras[i].setFecha(request.json['fecha'])
            Pacientes_Enfermeras[i].setSexo(request.json['sexo'])
            Pacientes_Enfermeras[i].setUsuario(request.json['usuario'])
            Pacientes_Enfermeras[i].setContraseña(request.json['password'])
            Pacientes_Enfermeras[i].setTelefono(int(request.json['telefono']))            
            return jsonify({'Mensaje':'Se actualizo al Enfermero exitosamente'})
    return jsonify({'Mensaje':'No se encontro la Enfermero para actualizar'})

@app.route('/Enfermeros/<string:usuario>', methods=['DELETE'])
def EliminarEnfermera(usuario):
    global Pacientes_Enfermeras
    for i in range(len(Pacientes_Enfermeras)):
        if usuario == Pacientes_Enfermeras[i].getUsuario():
            del Pacientes_Enfermeras[i]
            return jsonify({'Mensaje':'Se elimino al Enfermero exitosamente'})
    return jsonify({'Mensaje':'No se encontro al Enfermero para eliminar'})

#DOCTORES

@app.route('/Doctores', methods=['GET'])
def ObetnerDoctores():
    global doctores
    Datos = []
    for persona in doctores:        
        objeto = {
            'Nombre': persona.getNombre(),
            'Apellido': persona.getApellido(),
            'Fecha': persona.getFecha(),
            'Sexo': persona.getSexo(),
            'Usuario': persona.getUsuario(),
            'Password': persona.getContraseña(),
            'Especialidad': persona.getEspecialidad(),
            'Telefono': persona.getTelefono()
        }
        Datos.append(objeto)
    return(jsonify(Datos))

@app.route('/Doctores/<string:usuario>', methods=['GET'])
def ObetnerDoctor(usuario):
    global doctores
    for persona in doctores:        
        if persona.getUsuario() == usuario:
            objeto = {
                'Nombre': persona.getNombre(),
                'Apellido': persona.getApellido(),
                'Fecha': persona.getFecha(),
                'Sexo': persona.getSexo(),
                'Usuario': persona.getUsuario(),
                'Password': persona.getContraseña(),
                'Especialidad': persona.getEspecialidad(),
                'Telefono': persona.getTelefono()
            }
            return(jsonify(objeto))
    salida = {"Mensaje": "No existe el Doctor con ese nombre"}
    return(jsonify(salida))

@app.route('/Doctores', methods=['POST'])
def AgregarDoctores():
    global doctores
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    fecha = request.json['fecha']
    sexo = request.json['sexo']
    usuario = request.json['usuario']    
    password = request.json['password']    
    especialidad = request.json['especialidad']
    telefono = int(request.json['telefono'])    
    nuevo = Doctores(nombre, apellido, fecha, sexo, usuario, password, especialidad, telefono)
    doctores.append(nuevo)
    return jsonify({'Mensaje':'Se agrego al Doctor exitosamente',})

@app.route('/Doctores/<string:usuario>', methods=['PUT'])
def ActualizarDoctor(usuario):
    global doctores
    for i in range(len(doctores)):
        if usuario == doctores[i].getUsuario():
            doctores[i].setNombre(request.json['nombre'])
            doctores[i].setApellido(request.json['apellido'])
            doctores[i].setFecha(request.json['fecha'])
            doctores[i].setSexo(request.json['sexo'])
            doctores[i].setUsuario(request.json['usuario'])
            doctores[i].setContraseña(request.json['password'])
            doctores[i].setEspecialidad(request.json['especialidad'])
            doctores[i].setTelefono(int(request.json['telefono']))   
            return jsonify({'Mensaje':'Se actualizo el Doctor exitosamente'})
    return jsonify({'Mensaje':'No se encontro al Doctor para actualizar'})

@app.route('/Doctores/<string:usuario>', methods=['DELETE'])
def EliminarDoctor(usuario):
    global doctores
    for i in range(len(doctores)):
        if usuario == doctores[i].getUsuario():
            del doctores[i]
            return jsonify({'Mensaje':'Se elimino al Doctor exitosamente'})
    return jsonify({'Mensaje':'No se encontro al Doctor para eliminar'})

#MEDICAMENTOS

@app.route('/Medicamentos', methods=['GET'])
def ObtenerMedicamentos():
    global medicamentos
    Datos = []
    for persona in medicamentos:
        objeto = {
            'Nombre': persona.getNombre(),
            'Precio': persona.getPrecio(),
            'Descripcion': persona.getDescripcion(),
            'Cantidad': persona.getCantidad()
        }
        Datos.append(objeto)            
    return(jsonify(Datos))

@app.route('/Medicamentos/<string:nombre>', methods=['GET'])
def ObtenerMedicamento(nombre):
    global medicamentos
    for persona in medicamentos:        
        if persona.getNombre() == nombre:
            objeto = {
            'Nombre': persona.getNombre(),
            'Precio': persona.getPrecio(),
            'Descripcion': persona.getDescripcion(),
            'Cantidad': persona.getCantidad()
            }
            return(jsonify(objeto))
    salida = {"Mensaje": "No existe el Medicamento con ese nombre"}
    return(jsonify(salida))

@app.route('/Medicamentos', methods=['POST'])
def AgregarMedicamento():
    global admin
    nombre = request.json['nombre']
    precio = request.json['precio']
    descripcion = request.json['descripcion']    
    cantidad = int(request.json['cantidad'])
    nuevo = Medicamentos(nombre, precio, descripcion, cantidad)
    medicamentos.append(nuevo)
    return jsonify({'Mensaje':'Se agrego el Medicamento exitosamente',})

@app.route('/Medicamentos/<string:nombre>', methods=['PUT'])
def ActualizarMedicamento(nombre):
    global medicamentos
    for i in range(len(medicamentos)):
        if nombre == medicamentos[i].getNombre():
            medicamentos[i].setNombre(request.json['nombre'])
            medicamentos[i].setPrecio(request.json['precio'])
            medicamentos[i].setDescripcion(request.json['descripcion'])
            medicamentos[i].setCantidad(int(request.json['cantidad']))
            return jsonify({'Mensaje':'Se actualizo el Medicamento exitosamente'})
    return jsonify({'Mensaje':'No se encontro el Medicamento para actualizar'})

@app.route('/Medicamentos/<string:nombre>', methods=['DELETE'])
def EliminarMedicamento(nombre):
    global medicamentos
    for i in range(len(medicamentos)):
        if nombre == medicamentos[i].getNombre():
            del medicamentos[i]
            return jsonify({'Mensaje':'Se elimino el Medicamento exitosamente'})
    return jsonify({'Mensaje':'No se encontro el Medicamento para eliminar'})

#CITAS

@app.route('/Citas', methods=['GET'])
def ObtenerCitas():
    global citas
    Datos = []
    for persona in citas:
        objeto = {
            'Fecha': persona.getFecha(),
            'Hora': persona.getHora(),
            'Paciente': persona.getPaciente(),
            'Motivo': persona.getMotivo(),
            'Estado': persona.getEstado(),
            'Doctor': persona.getDoctor()
        }
        Datos.append(objeto)            
    return(jsonify(Datos))

@app.route('/Citas/<string:paciente>', methods=['GET'])
def ObtenerCitaPaciente(paciente):
    global citas
    for persona in citas:        
        if persona.getPaciente() == paciente:
            objeto = {
                'Fecha': persona.getFecha(),
                'Hora': persona.getHora(),
                'Paciente': persona.getPaciente(),
                'Motivo': persona.getMotivo(),
                'Estado': persona.getEstado(),
                'Doctor': persona.getDoctor()
            }
            return(jsonify(objeto))
    salida = {"Mensaje": "No existe la Cita del Paciente con ese nombre"}
    return(jsonify(salida))

@app.route('/Citas', methods=['POST'])
def AgregarCita():
    global citas
    fecha = request.json['fecha']
    hora = request.json['hora']
    paciente = request.json['paciente']
    motivo = request.json['motivo']
    estado = request.json['estado'] 
    doctor = request.json['doctor']
    nuevo = Citas(fecha, hora, paciente, motivo, estado, doctor)
    citas.append(nuevo)
    return jsonify({'Mensaje':'Se agrego la Cita al Paciente exitosamente',})

@app.route('/Citas/<string:paciente>', methods=['PUT'])
def ActualizarCita(paciente):
    global citas
    for i in range(len(citas)):
        if paciente == citas[i].getPaciente():
            citas[i].setFecha(request.json['fecha'])
            citas[i].setHora(request.json['hora'])
            citas[i].setPaciente(request.json['paciente'])
            citas[i].setMotivo(request.json['motivo'])
            citas[i].setEstado(request.json['estado'])
            citas[i].setDoctor(request.json['doctor'])
            return jsonify({'Mensaje':'Se actualizo la Cita del Paciente exitosamente'})
    return jsonify({'Mensaje':'No se encontro la Cita del Paciente para actualizar'})

@app.route('/Citas/<string:paciente>', methods=['DELETE'])
def EliminarCita(paciente):
    global citas
    for i in range(len(citas)):
        if paciente == citas[i].getPaciente():
            del citas[i]
            return jsonify({'Mensaje':'Se elimino el Medicamento exitosamente'})
    return jsonify({'Mensaje':'No se encontro el Medicamento para eliminar'})

#FACTURAS

@app.route('/Facturas', methods=['GET'])
def ObtenerFacturas():
    global facturas
    Datos = []
    for persona in facturas:
        objeto = {
            'Fecha': persona.getFecha(),
            'Paciente': persona.getPaciente(),
            'Doctor': persona.getDoctor(),
            'Precio_c': persona.getPrecio_c(),
            'Costo_o': persona.getCosto_o(),
            'Costo_i':persona.getCosto_i(),
            'Total': persona.getTotal()
        }
        Datos.append(objeto)            
    return(jsonify(Datos))

@app.route('/Facturas/<string:paciente>', methods=['GET'])
def ObtenerFactura(paciente):
    global facturas
    for persona in facturas:        
        if persona.getPaciente() == paciente:
            objeto = {
                'Fecha': persona.getFecha(),
                'Paciente': persona.getPaciente(),
                'Doctor': persona.getDoctor(),
                'Precio_c': persona.getPrecio_c(),
                'Costo_o': persona.getCosto_o(),
                'Costo_i':persona.getCosto_i(),
                'Total': persona.getTotal()
            }
            return(jsonify(objeto))
    salida = {"Mensaje": "No existe la Factura del Paciente con ese nombre"}
    return(jsonify(salida))

@app.route('/Facturas', methods=['POST'])
def AgregarFactura():
    global facturas
    fecha = request.json['fecha']    
    paciente = request.json['paciente']
    doctor = request.json['doctor']
    precio_c = request.json['precio_c']
    costo_o = request.json['costo_o']
    costo_i = request.json['costo_i']
    total = request.json['total']
    nuevo = Facturas(fecha, paciente, doctor, precio_c, costo_o, costo_i, total)
    facturas.append(nuevo)
    return jsonify({'Mensaje':'Se agrego la Factura al Paciente exitosamente',})

@app.route('/Facturas/<string:paciente>', methods=['PUT'])
def ActualizarFactura(paciente):
    global facturas
    for i in range(len(facturas)):
        if paciente == facturas[i].getPaciente():
            facturas[i].setFecha(request.json['fecha'])
            facturas[i].setPaciente(request.json['paciente'])
            facturas[i].setDoctor(request.json['doctor'])
            facturas[i].setPrecio_c(request.json['precio_c'])
            facturas[i].setCosto_o(request.json['costo_o'])
            facturas[i].setCosto_i(request.json['costo_i'])
            facturas[i].setTotal(request.json['total'])
            return jsonify({'Mensaje':'Se actualizo la Factura del Paciente exitosamente'})
    return jsonify({'Mensaje':'No se encontro la Factura del Paciente para actualizar'})

@app.route('/Facturas/<string:paciente>', methods=['DELETE'])
def EliminarFactura(paciente):
    global facturas
    for i in range(len(facturas)):
        if paciente == facturas[i].getPaciente():
            del facturas[i]
            return jsonify({'Mensaje':'Se elimino la Factura exitosamente'})
    return jsonify({'Mensaje':'No se encontro la Factura para eliminar'})

#PEDIDO

@app.route('/Pedido', methods=['GET'])
def ObtenerPedidos():
    global pedido
    Datos = []
    for persona in pedido:
        objeto = {            
            'Paciente': persona.getPaciente()            
        }
        Datos.append(objeto)            
    return(jsonify(Datos))

@app.route('/Pedido/<string:paciente>', methods=['GET'])
def ObtenerPedido(paciente):
    global pedido
    for persona in pedido:        
        if persona.getPaciente() == paciente:
            objeto = {                
                'Paciente': persona.getPaciente()
            }
            return(jsonify(objeto))
    salida = {"Mensaje": "No existe la Factura del Paciente con ese nombre"}
    return(jsonify(salida))

@app.route('/Pedido', methods=['POST'])
def AgregarPedido():
    global pedido    
    paciente = request.json['paciente']
    medicamento = []
    nuevo = Pedido(paciente, medicamento)
    pedido.append(nuevo)
    return jsonify({'Mensaje':'Se agrego el Pedido del Paciente exitosamente',})

@app.route('/Pedido/<string:paciente>', methods=['PUT'])
def ActualizarPedido(paciente):
    global pedido
    for i in range(len(pedido)):
        if paciente == pedido[i].getPaciente():            
            pedido[i].setPaciente(request.json['paciente'])
            return jsonify({'Mensaje':'Se actualizo el Pedido del Paciente exitosamente'})
    return jsonify({'Mensaje':'No se encontro el Pedido del Paciente para actualizar'})

@app.route('/Pedido/<string:paciente>', methods=['DELETE'])
def EliminarPedido(paciente):
    global pedido
    for i in range(len(pedido)):
        if paciente == pedido[i].getPaciente():
            del pedido[i]
            return jsonify({'Mensaje':'Se elimino el Pedido exitosamente'})
    return jsonify({'Mensaje':'No se encontro el Pedido para eliminar'})

#RECETAS

@app.route('/Recetas', methods=['GET'])
def ObtenerRecetas():
    global recetas
    Datos = []
    for persona in recetas:
        objeto = {            
            'Nombre': persona.getNombre(),
            'Fecha': persona.getFecha(),
            'Paciente': persona.getPaciente(),
            'Padecimiento': persona.getPadecimiento(),
            'Descripcion': persona.getDescripcion()
        }
        Datos.append(objeto)            
    return(jsonify(Datos))

@app.route('/Recetas/<string:nombre>', methods=['GET'])
def ObtenerReceta(nombre):
    global recetas
    for persona in recetas:        
        if persona.getNombre() == nombre:
            objeto = {                
                'Nombre': persona.getNombre(),
                'Fecha': persona.getFecha(),
                'Paciente': persona.getPaciente(),
                'Padecimiento': persona.getPadecimiento(),
                'Descripcion': persona.getDescripcion()
            }
            return(jsonify(objeto))
    salida = {"Mensaje": "No existe la Receta con ese nombre"}
    return(jsonify(salida))

@app.route('/Recetas', methods=['POST'])
def AgregarReceta():
    global recetas
    nombre = request.json['nombre']
    fecha = request.json['fecha']
    paciente = request.json['paciente']    
    padecimiento = request.json['padecimiento']
    descripcion = request.json['descripcion']
    nuevo = Recetas(nombre, fecha, paciente, padecimiento, descripcion)
    recetas.append(nuevo)
    return jsonify({'Mensaje':'Se agrego la Receta exitosamente',})

@app.route('/Recetas/<string:nombre>', methods=['PUT'])
def ActualizarReceta(nombre):
    global recetas
    for i in range(len(recetas)):
        if nombre == recetas[i].getNombre():            
            recetas[i].setNombre(request.json['nombre'])
            recetas[i].setFecha(request.json['fecha'])
            recetas[i].setPaciente(request.json['paciente'])
            recetas[i].setPadecimiento(request.json['padecimiento'])
            recetas[i].setDescripcion(request.json['descripcion'])
            return jsonify({'Mensaje':'Se actualizo la Receta exitosamente'})
    return jsonify({'Mensaje':'No se encontro la Receta para actualizar'})

@app.route('/Recetas/<string:nombre>', methods=['DELETE'])
def EliminarReceta(nombre):
    global recetas
    for i in range(len(recetas)):
        if nombre == recetas[i].getNombre():
            del recetas[i]
            return jsonify({'Mensaje':'Se elimino la Receta exitosamente'})
    return jsonify({'Mensaje':'No se encontro la Receta para eliminar'})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 3000, debug = True)
