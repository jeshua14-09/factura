#taller factura electronica
class Cliente:
  def _init_(self):
    self.nombre=""
    self.telefono=""
   
  def datos_tienda(self):
    print ("Datos de la tienda")
    self.nombre= (input("escriba el nombre de la tienda:"))
    self.telefono= (input("escribe el telefono de la tienda:"))
    self.nit=(input("ingrese el nit de la tienda"))
    self.direccion= (input("ingrese la direccion de la tienda"))
  
  def solicitar_datos_del_cliente(self):
    print("Datos del cliente")
    self.nombre= (input("Escriba el nombre del cliente:"))
    self.telefono =(input("escriba el telefono del cliente:"))
    self.cedula=(input("Escriba la cedula del cliente:"))
  

  def productos (self):
    self.nombre= input("Escribe nombre del producto:")
    self.precio = int(input("Escribe el precio:"))
    self.cantidad= int(input("Escribe la cantidad del producto:"))
    
    self.total=self.precio * self.cantidad 
    self.iva=self.total*19

  def mostrar_total (self):
    print("Subotal: ",self.total)
    print("Total + iva: ",self.iva)
    print("Gracias por tu compra")
factura=Cliente()
factura.datos_tienda()
factura.solicitar_datos_del_cliente()
factura.productos()
factura.mostrar_total()