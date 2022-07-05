from Carrito import Carrito
from Producto import Producto
if __name__ == '__main__':
    cart = Carrito()
    prod1 = Producto("Pizza", precio=10, stock=10)
    prod2 = Producto("Hamburguesa", precio=5, stock=10)

    
    cart.agregar(prod1,11)
    cart.agregar(prod2,3)
    print(cart)
  

