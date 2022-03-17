class Producto():
  def __init__(self,nombre, precio, stock):
    self.nombre = nombre
    self.precio = precio
    self.stock = stock
  def __str__(self):
    return "Nombre: " + self.nombre + " Precio: " + str(self.precio) + " Stock: " + str(self.stock)
  