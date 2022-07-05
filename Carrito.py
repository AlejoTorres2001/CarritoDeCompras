class Carrito():
    def __init__(self):
        self.productos = []
        self.total = 0
        self.cantidad_total = 0
        self.stock = 0
        
    def agregar(self, producto,cantidad=1):
        self.productos.append([producto,cantidad])
        self.total += producto.precio*cantidad
        self.cantidad_total += cantidad
#        self.cantidad = cantidad
#        self.stock = producto.stock # De esta manera cuando uno esta sin stock me tira todos sin stock
        for prod in self.productos:
          self.stock = prod[0].stock  # Si defino self.stock como el stock de cada prod no funciona la condicion o va igual que la anterior 
          self.cantidad = cantidad    
    def quitar(self, producto):
        for prod in self.productos:
            if prod[0].nombre == producto.nombre:
                if prod[1] -1 == 0:
                    self.productos.remove(prod)
                    self.cantidad_total -= 1  
                    self.total -= prod[0].precio  
                    
                else:                                                   
                    prod[1] -= 1
                    self.cantidad_total -= 1
            
    def __str__(self):
        prods=""
        for prod in self.productos:        
            prods+=f"Nombre:{prod[0].nombre} Precio: {str(prod[0].precio)} Cantidad: {str(prod[1]) } \n"
            if self.stock <= self.cantidad:
              return "Carrito: \n" + prods + " Total A Pagar: " + str(self.total) + " Cantidad de productos: " + str(self.cantidad_total)
            else:
              print("No hay suficiente stock de:" ,prod[0].nombre)