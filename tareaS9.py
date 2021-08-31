class Empresa:
    aumentoId = 1
    def __init__(self, departamen, emplea, direcci, telefo, razonSo, ruc):
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
    def __init__(self, nomb, suel, fechaIn):
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
    def __init__(self, nomb, suel, fechaIn, comisi):
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
    def __init__(self, nomb, suel, fechaIn, sindica, contratoCo):
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
    def __init__(self, emplea, descripci):
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
    def __init__(self, horasRe, horasEx, emplea, fec, esta):
        self.__id = Sobretiempo.aumentoId
        self.horasRecargo = horasRe
        self.horasExtraordinarias = horasEx
        self.empleado = emplea
        self.fecha = fec
        self.estado = esta
        Sobretiempo.aumentoId = Sobretiempo.aumentoId + 1
    
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
    def __init__(self, fec, valo, numeroPa, cuo, emplea, esta):
        self.__id = Prestamos.aumentoId
        self.fecha = fec
        self.valor = valo
        self.numPagos = numeroPa
        self.cuota = cuo
        self.empleado = emplea
        self.saldo = self.numPagos * self.valor
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
    def __init__(self, iess, comisi, antigued):
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
    def __init__(self, emplea, fec, sobretiem, comisi, antigued, iess, presta):
        self.__id = Nomina.aumentoId
        self.empleado = emplea
        self.fecha = fec
        self.sueldo = emplea.sueldo
        self.sobretiempo = sobretiem
        self.comision = comisi
        self.antiguedad = antigued
        self.totIng = self.sueldo + self.antiguedad + self.sobretiempo.horasRecargo + self.sobretiempo.horasExtraordinarias
        self.iess = self.sueldo * iess
        self.iess = round(self.iess, 2)
        self.prestamo = presta
        self.totDes = self.comision + self.iess + self.prestamo.valor
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


nombre = input("Nombre del empleado: ")
sueldo = float(input("Sueldo del empleado: "))
fechaIngreso = input("Fecha de ingreso del empleado: ")

empleadoTipo = int(input("Empleado [1]administrativo, [2]obrero: "))
if empleadoTipo == 1:
    comision = int(input("El empleado está sujeto a comisiones [1]si, [2]no: "))
    if comision == 1:
        empleado = Administrativo(nombre, sueldo, fechaIngreso, True)
    else:
        empleado = Administrativo(nombre, sueldo, fechaIngreso, False)
else:
    sindicato = int(input("El empleado pertenece a un sindicato [1]si, [2]no: "))
    contratoColectivo = int(input("El empleado pertenece a algún contrato colectivo [1]si, [2]no: "))
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

direccion = input("Direccion de la empresa: ")
telefono = input("Telefono de la empresa: ")
razonSocial = input("Razón Social de la empresa: ")
ruc = input("Ruc de la empresa: ")

realizaPrestamo = int(input("El empleado realizó un prestamo [1]si, [2]no: "))
if realizaPrestamo == 1:
    #Realizo prestamo
    fechaPrestamo = input("Fecha del prestamo: ")
    valorPrestamo = float(input("Cuota a cancelar: "))
    numeroPagos = int(input("Numero de pagos restantes: "))
    cuota = float(input("Cuota establecida: "))
    if (numeroPagos * valorPrestamo) != 0:
        estadoPres = True
    else:
        estadoPres = False
    prestamos = Prestamos(fechaPrestamo, valorPrestamo, numeroPagos, cuota, empleado, estadoPres)
else:
    #No realizo prestamo
    prestamos = Prestamos("", 0, 0, 0, empleado, False)

realizaSobretiempo = int(input("El empleado realizó sobretiempo [1]si, [2]no: "))
if realizaSobretiempo == 1:
    #Realizo sobretiempo
    horasRecargo = float(input("Horas recargo: "))
    horasExtraordinarias = float(input("Horas Extraordinarias: "))
    fechaSobretiempo = input("Fecha Sobretiempo: ")
    if horasRecargo != 0 or horasExtraordinarias != 0:
        estadoSobret = True
    else:
        estadoSobret = False
    sobretiempo = Sobretiempo(horasRecargo, horasExtraordinarias, empleado, fechaSobretiempo, estadoSobret)
else:
    #No realizo sobretiempo
    sobretiempo = Sobretiempo(0, 0, empleado, "", False)

porcentajeIess = float(input("Porcentaje a cobrar del sueldo para el iess: "))
realizoComision = isinstance(empleado, Administrativo)
if realizoComision:
    #True
    cobrarComision = float(input("Comision a recargar: "))
else:
    #False > Obrero
    cobrarComision = 0
antiguedad = float(input("Cargo por antiguedad: "))

fechaNomina = input("Fecha de emisión de la nomina: ")

empresa = Empresa(Departamento(empleado, descripcionDepartamento), empleado, direccion, telefono, razonSocial, ruc)
deducciones = Deducciones(porcentajeIess, cobrarComision, antiguedad)
nomina = Nomina(empleado, fechaNomina, sobretiempo, deducciones.comision, deducciones.antiguedad, deducciones.iess, prestamos)


print("")
empresa.mostrarEmpresa()
print("")
empleado.mostrarEmpleado()
print("")
if isinstance(empleado, Administrativo):
    empleado.mostrarAdministrativo()
else:
    empleado.mostrarObrero()
print("")
empresa.departamento.mostrarDepartamento()
print("")
prestamos.mostrarPrestamos()
print("")
sobretiempo.mostrarSobretiempo()
print("")
deducciones.mostrarDeducciones()
print("")
nomina.mostrarNomina()
