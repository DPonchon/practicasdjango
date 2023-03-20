class Persona:
    def __init__(self, nombre, edad, dni):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad
    
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, nuevo_dni):
        self._dni = nuevo_dni
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        self.titular = titular

    def get_cantidad(self):
        return self.cantidad

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad

    def mostrar(self):
        print(f"Titular:", self.titular.nombre)
        print(f"Cantidad:", self.cantidad)

persona1 = Persona("Light Shagami", 26, "45687598")
cuenta1 = Cuenta(persona1, 3200.0)
cuenta1.mostrar()  

cuenta1.ingresar(800.0)
cuenta1.mostrar()  

cuenta1.retirar(1500.0)
cuenta1.mostrar()    

class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def es_titular_valido(self):
        edad = self.titular.edad
        return edad >= 18 and edad < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        

    def mostrar(self):
        print(f"Cuenta Joven")
        print(f"Titular:", self.titular.nombre)
        print(f"Cantidad:", self.cantidad)
        print(f"Bonificación:", self.bonificacion, "%")

persona2 = Persona("Lawliet Ryusaki", 25, "46187496")
cuenta_joven1 = CuentaJoven(persona2, 1000.0, 10)
cuenta_joven1.mostrar() 

persona3 = Persona("Misa Amane", 16, "51248746" )
cuenta_joven2 = CuentaJoven(persona3, 500.0, 5)
cuenta_joven2.retirar(100.0)  
cuenta_joven2.mostrar()  

