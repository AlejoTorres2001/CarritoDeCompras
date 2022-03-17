class Carrito():
    def __init__(self):
        self.productos = []
        self.total = 0
        self.cantidad = 0
    def agregar(self, producto):
        self.productos.append(producto)
        self.total += producto.precio
        self.cantidad += 1
    def quitar(self, producto):
        self.productos.remove(producto)
        self.total -= producto.precio
        self.cantidad -= 1
    def __str__(self):
        return "Carrito: " + str(self.productos) + " Total: " + str(self.total) + " Cantidad: " + str(self.cantidad)