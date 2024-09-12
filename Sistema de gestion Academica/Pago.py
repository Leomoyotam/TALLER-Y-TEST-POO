from utilss import reset_color, green_color, blue_color, purple_color
from utilss import gotoxy, BorrarPantalla, linea
from datetime import datetime
from Profesor import Profesor
from Asignatura import Asignatura
from Estudiante import Estudiante
from Periodo import Periodo
from Pago import Pago
from Nivel import Nivel


class Pago:
    def __init__(self, id, fecha_pago, estudiante,asignatura, profesor, periodo, active=True):
        self.id = id  # Identificador único para el pago.
        self.fecha_pago = fecha_pago  # fecha del pago.
        self.estudiante =  estudiante # Estudiante que realiza el pago.
        self.asignatura = asignatura
        self.profesor = profesor
        self.periodo = periodo
        self.total_pagos=0
        self.detallePago = []  # detalles de los pagos por asignaturas.
        self.active = active
        self.fecha_creacion = datetime.now().strftime('%d-%m-%Y')

    def __str__(self):
       return (f"Pago ID: {self.id}, Fecha pago: {self.fecha_pago}, Estudiante: {self.estudiante}, asignatura {self.asignatura}, Profesor {self.profesor}, periodo {self.periodo} "
                f"Total Pago: {self.total_pagos}, Activo: {self.active}, Fecha de Creación: {self.fecha_creacion}")
       
    def addPago(self, detallePago):
        self.detalle_Pago.append(detallePago)  # añade el detalles de los pagos de cada asignatura por estudiante.
        # suma cada pago por asignatura al total_pagos

            
    def getJson(self):
        return {
            "Pago ID": self.id,
            "Fecha pago": self.fecha_pago,
            "Estudiante": self.estudiante,
            "Asignatura": self.asignatura,
            "profesor":self.profesor,
            "periodo": self.periodo,
            "Total Pago": self.total_pagos,
            "detalle_pago": [detalle.getJson() for detalle in self.detallePago],
            "active": self.active,
            "fecha_creacion": self.fecha_creacion
        }

    def mostrar_detalle_notas(self):
        linea(80, green_color)
        print(f"( {purple_color}Universisdad Estatal de Milagro{green_color} )".center(80))
        linea(80, green_color)
        
        print(blue_color + f"Pago ID: {self.id} Fecha: {self.fecha_creacion}")
        print(f" Periodo: {self.periodo.periodo}, Profesor: {self.profesor.nombre} {self.profesor.apellido}, Asignatura: {self.asignatura.descripcion}")
        
        linea(80, green_color)
        print(f"{purple_color} Detalle de pago".center(80))
        linea(80, green_color)
        print(f"{'Dni':<9}{'Estudiante':<33}{'Pago horas':<10}{'pago aranceles':<10}{'total':<10}{'Observación':<15}")
        linea(80, green_color)
        
        for detalle in self.detalle_notas:
            recuperacion = detalle.recuperacion if detalle.recuperacion is not None else "N/A"
            print(f"{detalle.estudiante.dni:<9}{detalle.estudiante.nombre} {detalle.estudiante.apellido:<30}{detalle.nota1:<10}{detalle.nota2:<10}{recuperacion:<15}{detalle.promedio:<10.2f}{detalle.observacion:<15}")
        
        linea(80, green_color)


class DetallePago:
    def __init__(self, id,asignatura,pago ):
        self.id = id  # Identificador único para el detalle del pago.
        self.asignatura = asignatura  # asignatura que se paga.
        self.pago= pago # costo de la asignatura.


    def __init__(self, id, estudiante, pago_horas, pago_aranceles, observacion=None):
        self.id = id  # Asignando el parámetro a self.id
        self.estudiante = estudiante  # Asignando el parámetro a self.estudiante
        self.pago_horas = pago_horas 
        self.pago_aranceles = pago_aranceles
        self.total = self.calcular_promedio()
        self.observacion = observacion or self.generar_observacion()
        
    def calcular_promedio(self):
        pago = [self.pago_horas, self.pago_aranceles]
        pago.append(self.total)
        return sum(pago)

    def generar_observacion(self):
        return "Pago Aprobado"
    
    def __str__(self):
        return (f"Detalle pago ID: {self.id}, Estudiante: {self.estudiante}, pago horas: {self.pago_horas}, "
                f"pago aranceles: {self.pago_aranceles}, total: {self.total}, Observación: {self.observacion}")
    
    def getJson(self):
        return {
            "id": self.id,
            "estudiante": self.estudiante,
            "pago horas": self.pago_horas,
            "pago aranceles": self.pago_aranceles,
            "total": self.total,
            "observacion": self.observacion
        }

