from datetime import date


class Empresa:
    aumentoId = 1
    def __init__(self, departamen="", emplea="", direcci="", telefo="", razonSo="", ruc=""):
        self.__id = Empresa.aumentoId
        self.departamento = departamen
        self.empleado = emplea
        self.direccion = direcci
        self.telefono = telefo
        self.razonSocial = razonSo
        self.ruc = ruc
        Empresa.aumentoId = Empresa.aumentoId + 1
    
    def mostrarEmpresa(self):
        print("*CLASE EMPRESA*")
        print("id:", self.__id)
        print("direccion:", self.direccion)
        print("telefono:", self.telefono)
        print("razon social:", self.razonSocial)
        print("ruc:", self.ruc)
    
    @property
    def id(self):
        return self.__id


class Empleado:
    aumentoId = 1
    def __init__(self, nomb="", suel="", fechaIn=0):
        self.__id = Empleado.aumentoId
        self.nombre = nomb
        self.sueldo = suel
        self.fechaIngreso = fechaIn
        Empleado.aumentoId = Empleado.aumentoId + 1
    
    def mostrarEmpleado(self):
        print("*CLASE EMPLEADO*")
        print("id:", self.__id)
        print("nombre:", self.nombre)
        print("sueldo:", self.sueldo)
        print("fecha de ingreso:", self.fechaIngreso)

    @property
    def id(self):
        return self.__id


class Administrativo(Empleado):
    aumentoId = 1
    def __init__(self, nomb="", suel="", fechaIn=0, comisi=False):
        super().__init__(nomb, suel, fechaIn)
        self.__id = Administrativo.aumentoId
        self.comision = comisi
        Administrativo.aumentoId = Administrativo.aumentoId + 1
    
    def mostrarAdministrativo(self):
        print("*CLASE ADMINISTRATIVO*")
        print("id:", self.__id)
        print("comision:", self.comision)

    @property
    def id(self):
        return self.__id


class Obrero(Empleado):
    aumentoId = 1
    def __init__(self, nomb="", suel=0, fechaIn=0, sindica=False, contratoCo=False):
        super().__init__(nomb, suel, fechaIn)
        self.__id = Obrero.aumentoId
        self.sindicato = sindica
        self.contratoColectivo = contratoCo
        Obrero.aumentoId = Obrero.aumentoId + 1
    
    def mostrarObrero(self):
        print("*CLASE OBRERO*")
        print("id:", self.__id)
        print("sindicato:", self.sindicato)
        print("contrato colectivo:", self.contratoColectivo)
    
    @property
    def id(self):
        return self.__id


class Departamento:
    aumentoId = 1
    def __init__(self, emplea="", descripci=""):
        self.__id = Departamento.aumentoId
        self.empleado = emplea
        self.descripcion = descripci
        Departamento.aumentoId = Departamento.aumentoId + 1
    
    def mostrarDepartamento(self):
        print("*CLASE DEPARTAMENTO*")
        print("id:", self.__id)
        print("descripcion:", self.descripcion)
    
    @property
    def id(self):
        return self.__id


class Sobretiempo:
    aumentoId = 1
    def __init__(self, horasRe=0, horasEx=0, emplea="", fec="", esta=False):
        self.__id = Sobretiempo.aumentoId
        self.horasRecargo = horasRe
        self.horasExtraordinarias = horasEx
        self.empleado = emplea
        self.fecha = fec
        self.estado = esta
        Sobretiempo.aumentoId = Sobretiempo.aumentoId + 1
    
    def totSobretiempo(self, sueldo=0, horasRec=0, horasExt=0):
        valor_hora = sueldo/240
        return round((valor_hora*(horasRec*0.50+horasExt*2)), 2)
    
    def mostrarSobretiempo(self):
        print("*CLASE SOBRETIEMPO*")
        print("id:", self.__id)
        print("horas recargo:", self.horasRecargo)
        print("horas extraordinarias:", self.horasExtraordinarias)
        print("fecha:", self.fecha)
        print("estado:", self.estado)
    
    @property
    def id(self):
        return self.__id


class Prestamos:
    aumentoId = 1
    def __init__(self, fec="", valo=0, numeroPa=0, emplea="", esta=False):
        self.__id = Prestamos.aumentoId
        self.fecha = fec
        self.valor = valo
        self.numPagos = numeroPa
        self.cuota = round((self.valor / self.numPagos), 2)
        self.empleado = emplea
        self.saldo = round((self.cuota * self.numPagos), 2)
        self.estado = esta
        Prestamos.aumentoId = Prestamos.aumentoId + 1

    def mostrarPrestamos(self):
        print("*CLASE PRESTAMOS*")
        print("id:", self.__id)
        print("fecha:", self.fecha)
        print("valor:", self.valor)
        print("numero de pagos:", self.numPagos)
        print("cuota", self.cuota)
        print("saldo", self.saldo)
        print("estado:", self.estado)
    
    @property
    def id(self):
        return self.__id


class Deducciones:
    aumentoId = 1
    def __init__(self, iess=0, comisi=0, antigued=0):
        self.__id = Deducciones.aumentoId
        self.iess = iess
        self.comision = comisi
        self.antiguedad = antigued
        Deducciones.aumentoId = Deducciones.aumentoId + 1

    def mostrarDeducciones(self):
        print("*CLASE DEDUCCIONES*")
        print("id:", self.__id)
        print("iess:", self.iess)
        print("comision:", self.comision)
        print("antiguedad:", self.antiguedad)
    
    @property
    def id(self):
        return self.__id


class Nomina:
    aumentoId = 1
    def __init__(self, emplea="", fec=0, sobretiem="", comisi=0, antigued=0, iess=0, presta=""):
        self.__id = Nomina.aumentoId
        self.empleado = emplea
        self.fecha = fec
        self.sueldo = emplea.sueldo
        self.sobretiempo = sobretiem
        self.totSobret = self.sobretiempo.totSobretiempo(self.sueldo, self.sobretiempo.horasRecargo, self.sobretiempo.horasExtraordinarias)
        self.comision = round((comisi * self.sueldo), 2)
        numeroDias = (self.fecha-self.empleado.fechaIngreso).days
        numeroDias = int(numeroDias)
        self.antiguedad = antigued*numeroDias/365*self.sueldo
        self.antiguedad = round(self.antiguedad, 2)
        self.iess = iess*(self.sueldo+self.totSobret)
        self.iess = round(self.iess, 2)
        self.prestamo = presta
        self.prestamoEmpleado = self.prestamo.cuota
        self.totIng = self.sueldo+self.totSobret+self.comision+self.antiguedad
        self.totIng = round(self.totIng, 2)
        self.totDes = self.iess+self.prestamoEmpleado
        self.totDes = round(self.totDes, 2)
        self.liquidoRecibir = self.totIng - self.totDes
        self.liquidoRecibir = round(self.liquidoRecibir, 2)
        Nomina.aumentoId = Nomina.aumentoId + 1
    
    def mostrarNomina(self):
        print("*CLASE NOMINA*")
        print("id:", self.__id)
        print("fecha:", self.fecha)
        print("sueldo:", self.sueldo)
        print("comision:", self.comision)
        print("antiguedad:", self.antiguedad)
        print("total ingreso:", self.totIng)
        print("iess:", self.iess)
        print("total descuento:", self.totDes)
        print("liquido recibir:", self.liquidoRecibir)
    
    @property
    def id(self):
        return self.__id


# PARA EL INGRESO DE FECHA HACERLO COMO ESTE MODELO -> (AÑO/MES/DIA) -> 2018/12/30

direccion = input("Direccion de la empresa: ")
telefono = input("Telefono de la empresa: ")
razonSocial = input("Razón Social de la empresa: ")
ruc = input("Ruc de la empresa: ")

nombre = input("Nombre del empleado: ")
sueldo = float(input("Sueldo del empleado: "))
fechaIngresoNoDate = input("Fecha de ingreso del empleado: ").split("/")
año, mes, dia = int(fechaIngresoNoDate[0]), int(fechaIngresoNoDate[1]), int(fechaIngresoNoDate[2])
fechaIngreso = date(año, mes, dia)

empleadoTipo = int(input("Empleado [1]administrativo, [2]obrero: "))
if empleadoTipo == 1:
    antiguedad = 0
    comision = int(input("El empleado está sujeto a comisiones [1]si, [2]no: "))
    if comision == 1:
        cobrarComision = float(input("Comision a recargar: ")) / 100
        cobrarComision = round(cobrarComision, 2)
        empleado = Administrativo(nombre, sueldo, fechaIngreso, True)
    else:
        cobrarComision = 0
        empleado = Administrativo(nombre, sueldo, fechaIngreso, False)
else:
    cobrarComision = 0
    sindicato = int(input("El empleado pertenece a algún sindicato [1]si, [2]no: "))
    contratoColectivo = int(input("El empleado tiene algún contrato colectivo [1]si, [2]no: "))
    antiguedad = float(input("Cargo por antiguedad: "))/100
    antiguedad = round(antiguedad, 2)
    if sindicato == 1:
        if contratoColectivo == 1:
            empleado = Obrero(nombre, sueldo, fechaIngreso, True, True)
        else:
            empleado = Obrero(nombre, sueldo, fechaIngreso, True, False)
    else:
        if contratoColectivo == 1:
            empleado = Obrero(nombre, sueldo, fechaIngreso, False, True)
        else:
            empleado = Obrero(nombre, sueldo, fechaIngreso, False, False)

descripcionDepartamento = input("Descripción del departamento: ")

realizaPrestamo = int(input("El empleado realizó un prestamo [1]si, [2]no: "))
if realizaPrestamo == 1:
    #Realizo prestamo
    fechaPrestamoNoDate = input("Fecha del prestamo: ").split("/")
    año, mes, dia = int(fechaPrestamoNoDate[0]), int(fechaPrestamoNoDate[1]), int(fechaPrestamoNoDate[2])
    fechaPrestamo = date(año, mes, dia)
    valor = float(input("Valor Prestamo: "))
    numeroPagos = int(input("Numero de pagos: "))
    if numeroPagos > 0:
        estadoPres = True
    else:
        estadoPres = False
    prestamos = Prestamos(fechaPrestamo, valor, numeroPagos, empleado, estadoPres)
else:
    #No realizo prestamo
    prestamos = Prestamos("", 0, 0, empleado, False)

realizaSobretiempo = int(input("El empleado realizó sobretiempo [1]si, [2]no: "))
if realizaSobretiempo == 1:
    #Realizo sobretiempo
    horasRecargo = int(input("Horas recargo: "))
    horasExtraordinarias = int(input("Horas Extraordinarias: "))
    fechaSobretiempoNoDate = input("Fecha Sobretiempo: ").split("/")
    año, mes, dia = int(fechaSobretiempoNoDate[0]), int(fechaSobretiempoNoDate[1]), int(fechaSobretiempoNoDate[2])
    fechaSobretiempo = date(año, mes, dia)
    if horasRecargo != 0 or horasExtraordinarias != 0:
        estadoSobret = True
    else:
        estadoSobret = False
    sobretiempo = Sobretiempo(horasRecargo, horasExtraordinarias, empleado, fechaSobretiempo, estadoSobret)
else:
    #No realizo sobretiempo
    sobretiempo = Sobretiempo(0, 0, empleado, "", False)

porcentajeIess = float(input("Porcentaje a cobrar del sueldo para el iess: "))/100
porcentajeIess = round(porcentajeIess, 4)
realizoComision = isinstance(empleado, Administrativo)

fechaNominaNoDate = input("Fecha de emisión de la nomina: ").split("/")
año, mes, dia = int(fechaNominaNoDate[0]), int(fechaNominaNoDate[1]), int(fechaNominaNoDate[2])
fechaNomina = date(año, mes, dia)

empresa = Empresa(Departamento(empleado, descripcionDepartamento), empleado, direccion, telefono, razonSocial, ruc)
deducciones = Deducciones(porcentajeIess, cobrarComision, antiguedad)
nomina = Nomina(empleado, fechaNomina, sobretiempo, deducciones.comision, deducciones.antiguedad, deducciones.iess, prestamos)


print("")
empresa.mostrarEmpresa()
empleado.mostrarEmpleado()
if isinstance(empleado, Administrativo):
    empleado.mostrarAdministrativo()
else:
    empleado.mostrarObrero()
empresa.departamento.mostrarDepartamento()
prestamos.mostrarPrestamos()
sobretiempo.mostrarSobretiempo()
deducciones.mostrarDeducciones()
print("")
nomina.mostrarNomina()
