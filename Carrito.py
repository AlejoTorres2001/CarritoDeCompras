class Carrito():
    def __init__(self):
        self.productos = []
        self.total = 0
        self.cantidad_total = 0

    def agregar(self, producto, cantidad=1):
        if producto.stock == 0:  # Si el producto no tiene stock
            print(f'No hay stock de producto {producto.nombre}')
            return
        if producto.stock < cantidad:  # Si la cantidad de productos que se quiere agregar es mayor a la cantidad de stock
            print(f'No hay suficiente stock de producto {producto.nombre}')
            return
        #! Y si no quiero permitir que existan mas unidades en el carrito de un producto que el stock?
        self.productos.append([producto, cantidad])
        self.total += producto.precio*cantidad
        self.cantidad_total += cantidad

    def quitar(self, producto):
        for prod in self.productos:
            if prod[0].nombre == producto.nombre:
                if prod[1] - 1 == 0:
                    self.productos.remove(prod)
                    self.cantidad_total -= 1
                    self.total -= prod[0].precio
                else:
                    prod[1] -= 1
                    self.cantidad_total -= 1
                return
        print(f'No se encontro el producto a eliminar: {producto.nombre}')

    def __str__(self):
        prods = ""
        for prod in self.productos:
            prods += f"Nombre:{prod[0].nombre} Precio: {str(prod[0].precio)} Cantidad: {str(prod[1]) } \n"
        return "Carrito: \n" + prods + " Total A Pagar: " + str(self.total) + " Cantidad de productos: " + str(self.cantidad_total)
