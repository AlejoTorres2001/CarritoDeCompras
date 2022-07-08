from Carrito import Carrito
from Producto import Producto
if __name__ == '__main__':
    cart = Carrito()
    #!Probemos con un solo articulo
    prod1 = Producto("Pizza", precio=10, stock=3)
    #prod2 = Producto("Hamburguesa", precio=5, stock=10)
    #! Tratamos de agregar mas que el stock permitido
    cart.agregar(prod1, 4)
    # cart.agregar(prod2)
    print(cart)
    cart.quitar(prod1)
    print(cart)
