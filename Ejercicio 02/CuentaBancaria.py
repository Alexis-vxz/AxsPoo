class CuentaBancaria: 
    def __init__(self,titular,numeroCuenta,saldo): 
        self.titular = titular 
        self.numeroCuenta = numeroCuenta 
        self.saldo = saldo 
         
    def depositar(self,cantidad): 
        self.saldo = self.saldo + cantidad 
        return cantidad 
    def retirar(self,cantidad): 
       if cantidad <= self.saldo: 
        self.saldo = self.saldo - cantidad 
       else:
          print("El saldo de tu cuenta es insuficiente para realizar el retiro, deposita mas dinero")
    def consultarSaldo(self): 
        return self.saldo 
    def mostarInformacion(self): 
        return f"{self.titular} tienes {self.saldo}" 
     
     
cuenta1 = CuentaBancaria("Juan Perez", "0987654321", 1500.00) 
print(cuenta1.mostarInformacion()) 
 
cuenta1.depositar(3200.00) 
print(cuenta1.mostarInformacion()) 
 
cuenta1.retirar(500.00) 
print(cuenta1.mostarInformacion()) 
 
cuenta1.retirar(5000.00) 
print(cuenta1.mostarInformacion()) 
 
cuenta2 = CuentaBancaria("Maria Lopez", "0123456", 600.50) 
print(cuenta2.mostarInformacion()) 
 
cuenta2.depositar(600.00) 
print(cuenta2.mostarInformacion()) 
 
cuenta2.retirar(300.00)

print(cuenta2.mostarInformacion()) 
cuenta2.retirar(2000.00) 
print(cuenta2.mostarInformacion())