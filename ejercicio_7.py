class Producto:
    def __init__(slef, referencia, nombre, pvp):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp

    def __str__(self):
        return (self.referencia+""+self.nombre+""+self.pvp)


class Alimento(Producto):
    tipo = "alimento"

    def __str__(self):
        return(self.referencia+""+self.tipo+""+self.nombre+""+self.pvp)

class Electrodomestico(Producto):
    tipo = "electrodomestico"
    garantia = ""

    def __str__(self):
        return(self.referencia+""+self.tipo+""+self.nombre+""+self.pvp+""+self.garantia+" años de garantia")


class Moda(Producto):
    tipo = "moda"
    talla = ""

    def __str__(self):
        return(self.referencia+""+self.tipo+""+self.nombre+""+self.pvp+""+self.talla)

manzana = Alimento ("1223", "manzana roja", "$23")       
fresa = Alimento ("1224", "fresa", "$32")
estufa = Electrodomestico("1323", "estufa", "$5600")
estufa.garantia = ("4")
nevera = Electrodomestico("1343", "nevera", "$5900")
estufa.garantia = ("4")
camisa = Moda("1454", "camisa vestir", "$350")
camisa.talla = "G"
pantalon = Moda("1464", "pantalon vestir", "$460")
camisa.talla = "G"

alimentos = [manzana, fresa]
electrodemestico = [estufa, nevera]
modas = [camisa, pantalon]

def listar(categoria):
    for Producto in categoria:
        print(Producto, '\n')


def vender(categoria):
    print('eliga el producto para comprar (introduzca su referencia)')
    teclado = input()
    for producto in categoria:
        if producto.referencia == teclado:
            print('El producto ' +producto.nombre+ 'se ha vendido')
            categoria.remove(producto)
            break

    else:
        print('el producto no existe')


vender(alimentos)
listar(alimentos)
    

