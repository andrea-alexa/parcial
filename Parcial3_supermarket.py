#Estas son las variables que vamos a necesitar 
#cada variable almacena datos para ejecutar el codigo y se componen de diccionarios{} y listas []

usuario1 = {"nombre": "Juan", "contrasena": "1234", "edad": "25", "nivel": "admin", "id": "1"}
usuario2 = {"nombre": "Pedro", "contrasena": "2468", "edad": "30", "nivel": "vendedor", "id": "2"}
usuario3 = {"nombre": "Maria", "contrasena": "1357", "edad": "40", "nivel": "cliente", "id": "3"}
usuario4 = {"nombre": "Julian", "contrasena": "1324", "edad": "24", "nivel": "admin", "id": "4"}
usuarios_activos = [usuario1, usuario2, usuario3,usuario4]

areas = ["Electrónica", "Ropa"]
categorias = ["Computadoras", "Televisores", "Camisas", "Pantalones", "Vestidos"]
productos = {
    "Computadoras": [
        {
            "Nombre": "Laptop",
            "Proveedor": "HP",
            "Fecha de caducidad": "N/A",
            "Fecha de entrada": "2023-05-01",
            "Detalles": "8GB RAM, 256GB SSD",
            "Precio": 1000,
            "Unidades": 10
        },
        {
            "Nombre": "PC de escritorio",
            "Proveedor": "Dell",
            "Fecha de caducidad": "N/A",
            "Fecha de entrada": "2023-05-05",
            "Detalles": "16GB RAM, 1TB HDD",
            "Precio": 1500,
            "Unidades": 5
        }
    ],
    "Televisores": [
        {
            "Nombre": "Smart TV",
            "Proveedor": "Samsung",
            "Fecha de caducidad": "N/A",
            "Fecha de entrada": "2023-04-20",
            "Detalles": "55 pulgadas, 4K",
            "Precio": 800,
            "Unidades": 8
        },
        {
            "Nombre": "Televisor LED",
            "Proveedor": "LG",
            "Fecha de caducidad": "N/A",
            "Fecha de entrada": "2023-05-10",
            "Detalles": "32 pulgadas, HD",
            "Precio": 300,
            "Unidades": 12
        }
    ],
    "Camisas": [
        {
            "Nombre": "Camisa de manga corta",
            "Proveedor": "Zara",
            "Fecha de caducidad": "N/A",
            "Fecha de entrada": "2023-04-25",
            "Detalles": "Color blanco, talla M",
            "Precio": 30,
            "Unidades": 20
        },
        {
            "Nombre": "Camisa de manga larga",
            "Proveedor": "H&M",
            "Fecha de caducidad": "N/A",
            "Fecha de entrada": "2023-05-08",
            "Detalles": "Color azul, talla L",
            "Precio": 25,
            "Unidades": 15
        }
    ],
    "Pantalones": [
        {
            "Nombre": "Pantalón vaquero",
            "Proveedor": "Levi's",
            "Fecha de caducidad": "N/A",
            "Fecha de entrada": "2023-04-30",
            "Detalles": "Color negro, talla 32",
            "Precio": 50,
            "Unidades": 10
        },
        {
            "Nombre": "Pantalón de vestir",
            "Proveedor": "Hugo Boss",
            "Fecha de caducidad": "N/A",
            "Fecha de entrada": "2023-05-12",
            "Detalles": "Color gris, talla 34",
            "Precio": 80,
            "Unidades": 8
        }
    ],
    "Vestidos": [
        {"Nombre": "Vestido de noche",
            "Proveedor": "Forever 21",
            "Fecha de caducidad": "N/A",
            "Fecha de entrada": "2023-04-28",
            "Detalles": "Color negro, talla S",
            "Precio": 70,
            "Unidades": 5
        },
        {
            "Nombre": "Vestido casual",
            "Proveedor": "Zara",
            "Fecha de caducidad": "N/A",
            "Fecha de entrada": "2023-05-15",
            "Detalles": "Color rojo, talla M",
            "Precio": 60,
            "Unidades": 7
        }
    ]
}
#inicio del programa
print("========================================================")
print("============Supermercado Los Precios Altos =============")
print("========================================================\n")

#Esta funcion está asignada para el nivel de usuario "cliente" y le permite comprar un o varios productos -->
#de una categoría
def comprar_productos():
    #definimos estas listas y variable para agregarle valores luego
    compras = []
    total_pagar = 0

    print("=== Comprar productos ===")

    print("Áreas disponibles:")
    for i, area in enumerate(areas, start=1):# enumerate nos permite ennumerar las areas empezando desde el 1
                                             # para eso usamos "start" para que empiece desde el 1 y no 0
        print(f"{i}. {area}") #aquí i se convierte en la ennumeracion y se imprime el area

    area_opcion = int(input("Seleccione un área: "))
    area_seleccionada = areas[area_opcion - 1] #el numero seleccionado nos permite acceder a la lista de areas
    #y como los indices comienzan en 0 le restamos 1 para tener el indice correcto en la lista de areas


    print(f"Categorías de {area_seleccionada}:")# aquí mostramos las categorias respectivas al area
    categorias_area = [categoria for categoria in categorias if categoria in productos.keys()]
# categoria representa cada elemento en la lista categorias y luego .keys() confirma si la categoria se encuentra
# en el diccionario productos
    for i, categoria in enumerate(categorias_area, start=1):
        print(f"{i}. {categoria}")

    categoria_opcion = int(input("Seleccione una categoría: "))
    categoria_seleccionada = categorias_area[categoria_opcion - 1]

    
    print(f"Productos de {categoria_seleccionada}:")
    productos_categoria = productos[categoria_seleccionada]
    for i, producto in enumerate(productos_categoria, start=1):
        print("---------------")
        print(f"Producto {i}:")
        for clave, valor in producto.items(): #acá se busca en el diccionario de producto el nombre y precio y lo hace iterable
            print(f"{clave}: {valor}")# donce clave son "nombre", "precio", etc. y valor son el valor que tiene "nombre", "precio", etc

    while True:
        producto_opcion = input("Seleccione un producto (número) o 's' para finalizar la compra: ")
        if producto_opcion == 's':
            break
        producto_seleccionado = productos_categoria[int(producto_opcion) - 1] #esto permite que a la hora de seleccionar un producto
                                                                             # de la lista productos_categoria se haga coorectamente empezando desde 1
        compras.append(producto_seleccionado)#agregamos los productos seleccionados
        total_pagar += producto_seleccionado['Precio']# y busacamos el precio en la lista y se lo añadimos a la cantidad que debe pagar

    
    print("=== Detalles de compra ===")
    if len(compras) > 0:
        for i, producto in enumerate(compras, start=1):
            print("---------------")
            print(f"Producto {i}:")
            for clave, valor in producto.items():#acá se busca en la biblioteca de producto el nombre y precio y lo hace iterable
                print(f"{clave}: {valor}")# donce clave son "nombre", "precio", etc. y valor son el valor que tiene "nombre", "precio", etc
        print("---------------")
    else:
        print("No se han seleccionado productos.")

    print(f"Total a pagar: ${total_pagar}")
#===================================================================================================
#Esta funcion es para el nivel de usuario "vendedor" y basicamente cumple la misma funcion que la de comprar->
# un producto
def vender_productos():
    compras = []
    total_pagar = 0

    print("=== vender productos ===")

    print("Áreas disponibles:")
    for i, area in enumerate(areas, start=1):# enumerate nos permite ennumerar las areas empezando desde el 1
                                             # para eso usamos "start" para que empiece desde el 1 y no 0
        print(f"{i}. {area}")#aquí i se convierte en la ennumeracion y se imprime el area                

    area_opcion = int(input("Seleccione un área: "))
    area_seleccionada = areas[area_opcion - 1]#el numero seleccionado nos permite acceder a la lista de areas
#y como los indices comienzan en 0 le restamos 1 para tener el indice correcto en la lista de areas

    print(f"Categorías de {area_seleccionada}:")# aquí mostramos las categorias respectivas al area
    categorias_area = [categoria for categoria in categorias if categoria in productos.keys()]
# categoria representa cada elemento en la lista categorias y luego .keys() confirma si la categoria se encuentra
# en el diccionario productos
    for i, categoria in enumerate(categorias_area, start=1):
        print(f"{i}. {categoria}")

    categoria_opcion = int(input("Seleccione una categoría: "))
    categoria_seleccionada = categorias_area[categoria_opcion - 1]

    
    print(f"Productos de {categoria_seleccionada}:")
    productos_categoria = productos[categoria_seleccionada]
    for i, producto in enumerate(productos_categoria, start=1):
        print("---------------")
        print(f"Producto {i}:")
        for clave, valor in producto.items():#acá se busca en la biblioteca de producto el nombre y precio y lo hace iterable
            print(f"{clave}: {valor}")# donde clave es el nombre del producto y valor el precio 

    while True:
        producto_opcion = input("Seleccione un producto (número) o 's' para finalizar la venta: ")
        if producto_opcion == 's':
            break
        producto_seleccionado = productos_categoria[
            int(producto_opcion) - 1]#esto permite que a la hora de seleccionar un producto
                                                                            # de la lista productos_categoria se haga coorectamente empezando desde 1
        compras.append(producto_seleccionado)
        total_pagar += producto_seleccionado['Precio']

    
    print("=== Detalles de venta ===")
    if len(compras) > 0:
        for i, producto in enumerate(compras, start=1):
            print("---------------")
            print(f"Producto {i}:")
            for clave, valor in producto.items():#acá se busca en la biblioteca de producto el nombre y precio y lo hace iterable
                print(f"{clave}: {valor}")# donde clave es el nombre del producto y valor el precio 
        print("---------------")
    else:
        print("No se han seleccionado productos.")

    print(f"Total a pagar: ${total_pagar}")

#===================================================================================================
#esta funcion es para el nivel de usuario "vendedor y "cliente" para que en el caso de el vendedor revise el -->
#inventario y en el caso del "cliente" le mustre los productos disponibles.
def mostrar_productos():
    print("=== Productos disponibles ===")
    for categoria in productos: # aquí itereamos cada categoría en el diccionario productos
        print("Categoría:", categoria) # y luego presentamos una lista de los productod de cada categoría agregando la categoria
                                       # a la que pertenecen
        for i in range(len(productos[categoria])):  # iteramos a través de los índices de la lista de productos asociados a la categoría actual.
            producto = productos[categoria][i]#obtenemos el producto en base a la iteracion de "i"
            print("---------------")
            for clave in producto: #basiamente iteramos en las claves del dicionario producto
                valor = producto[clave]# obtenemos el precio basandose en el producto
                print(clave + ":", valor)   # e imprimimos nombre y precio

#===================================================================================================
#Esta funcion es especificamente para el nivel de usuario "admin" y esta le permite crear o añadir un area ->
# a la lista de las areas
def crear_area():
    print("=== Crear área ===")
    nueva_area = input("Ingrese el nombre del área: ")
    areas.append(nueva_area)# a la lista de las areas le añadimos la nueva
    print("Área creada exitosamente.")
    
#===================================================================================================
#Esta funcion es especificamente para el nivel de usuario "admin" y esta le permite crear o añadir una categoría ->
# a la lista de la categorias	
def crear_categoria():
    print("\n=== Crear categoría ===")
    nueva_categoria = input("Ingrese el nombre de la categoría: ")
    categorias.append(nueva_categoria) # a la lista de la categorias le añadimos la nueva
    print("Categoría creada exitosamente.")
#===================================================================================================
#esta funcion es un añadido a la funcion siguiente que es "crear_producto" y sirve para que el usuario "admin" selecione la categoría->
#a la que quiere añadir el nuevo producto.
def seleccionar_categoria():
    print("\n=== Seleccione una categoría ===")
#esta parte sirve para presentar las categorias en una lista Se itera sobre la lista de categorías utilizando la función enumerate 
#con el parámetro start=1 para que los números de opción comiencen desde 1 en lugar de 0.
# de esta manera controlamos las opciones que el usuario escriba

    for i, categoria in enumerate(categorias, start=1):
        print(f"{i}. {categoria}")   # se imprime cada categoría junto con su número de opción utilizando el formato de cadena f-string.
                                    # es como usar comas basicamente
    while True:
         opcion = int(input("Seleccione una opción: "))
#verificamos si lo que ingresó el usuario entra en el rango  valido en la lista "categorias"
         if opcion >= 1 and opcion <= len(categorias):
            return categorias[opcion - 1]#a la opcion que puso el usuario le restamos porque en las listas e empiezan desde 0
         else:
            print("Opción inválida no se ecuentra en el menu de categorias, intente denuevo.")
            
#===================================================================================================
#Esta funciones especificamente para el nivel de usuario "admin" y es la que le permite crear un nuevo producto y añadirlo ->
#a la biblioteca de productos
def crear_producto():
    print("\n=== Crear producto ===")
    nombre = input("Nombre del producto: ")
    proveedor = input("Proveedor: ")
    fecha_caducidad = input("Fecha de caducidad: ")
    fecha_entrada = input("Fecha de entrada: ")
    detalles = input("Detalles: ")
    precio = float(input("Precio: "))
    unidades = int(input("Unidades disponibles: "))

    while True:
#esta funcion permite al usuario ingresar la categoría a la que quiere agregar el producto
#Luego comprobamos si la categoría elegida existe en la biblioteca de productos le agregamos el producto con los datos que solicitamos antes
#además lo ponemos en un bucle por si el usuario se equivoca y no se cierre el programa
        categoria = seleccionar_categoria()
        
        if categoria in productos:
            productos[categoria].append({
                "Nombre": nombre,
                "Proveedor": proveedor,
                "Fecha de caducidad": fecha_caducidad,
                "Fecha de entrada": fecha_entrada,
                "Detalles": detalles,
                "Precio": precio,
                "Unidades": unidades
            })

            print("\nEl producto se ha añadido.\n")
            # Mostrar los productos como una lista ordenada
            print("================================================================")
            print("Lista de productos:")
            print("================================================================\n")
#para eso obtenemos el indice (1->) y el producto correspondiente (Papitas) y luego simplemente imprimimos el precio el cual se busca dentro de
        #productos    
            for indice, producto in enumerate(productos[categoria], start=1):
                print(f"{indice}. {producto['Nombre']} - {producto['Precio']}")
            
            break  # rompemos el bulcle porque ya se cumplio la funcion que necesitabamos
        else:
            print("La categoría seleccionada no existe. Inténtelo de nuevo.")

     
#===================================================================================================  
#esta funcion sirve para todos los nivels de usuario que hay y les pregunta si quieren salir de su menu de opciones para finalizar ->
#o ingresar con otro usuario    
def salirU():
    
    backI = input("Desea volver al inicio de sesion? (si/no) ''si escribe no finalizará el programa!''\n")
    if backI.lower() == "si":
        print("Está bien.")
        login()#preguntamos al usuario si quiere iniciar sesion con otro usuario y si dice si llamamos a la variable login()
    elif backI.lower() == "no":
        print("Fin del programa")     #si dice que no, se cierra el programa

#===================================================================================================   
#Aquí es donde se ejecutan todas las funciones antes vistas en donde tenemos las estructuras If correspondientes para cada opcion ->
# y dependiendo del usuario que haya ingresado.                 
def menu_principal(nivel_usuario):
# esta funcion se va a ejecutar dependiendo del nivel de usuario antes definido
    if nivel_usuario == "admin":
        opciones = [
            
            "1-Crear un área",
            "2-Añadir un producto",
            "3-Crear una nueva categoría",
            "4-Salir"
        ]
    elif nivel_usuario == "vendedor":
        opciones = [
            "1-Consultar inventario",
            "2-Registrar una venta",
            "3-Salir"
            
        ]
    elif nivel_usuario == "cliente":
        opciones = [
            "1-Revisar productos",
            "2-Realizar compra",
            "3-Salir"
        ]
    else:
        print("Nivel de usuario no válido")
        return

    # Mostrar el menú dpendiendo del nivel de usuario
    print("================================================================\n")
    print("\nMenú principal:")
    for opcion in opciones:
        print(opcion) # lo hacemos así para que aparezca como lista

       # Pedir la selección al usuario
    seleccion = input("Seleccione una opción: ")
    print("================================================================")

    # Ejecutar la opción seleccionada
    if nivel_usuario == "admin":
        if seleccion == "1":
           crear_area()
           menu_principal(nivel_usuario)

        elif seleccion == "2":
           crear_producto()
           menu_principal(nivel_usuario)
           
        elif seleccion == "3":
           crear_categoria()
           menu_principal(nivel_usuario)
           
        elif seleccion == "4":
           salirU()                
        else:
            print("Opción no válida")
            menu_principal(nivel_usuario)

    elif nivel_usuario == "vendedor":
        if seleccion == "1":
            print("Mostrar inventario")
            mostrar_productos()
            menu_principal(nivel_usuario)
            
        elif seleccion== "2":
            vender_productos()
            menu_principal(nivel_usuario)
            
        elif seleccion == "3":
            salirU()
            
        else:
            print("Opción no válida")
            nivel_usuario == "vendedor"
            menu_principal(nivel_usuario)
   
    elif nivel_usuario == "cliente":
        if seleccion == "1":
            print("Revisar productos")
            mostrar_productos()
            menu_principal(nivel_usuario)
            
        elif seleccion == "2":
            print("Realizar una compra")
            comprar_productos()
            menu_principal(nivel_usuario)
        
        elif seleccion == "3":
            salirU()
            
        else:
            print("Opción no válida")
            nivel_usuario == "cliente"
            menu_principal(nivel_usuario)
             
#esta funcion es para que el usuario ponga los dato que se le pide que inicie sesion con uno de los usuarios activos
#esto será lo primero que se mostrará en la terminal y de aquí depende el "menu_principal" que se le entregará al usuario

def login():
    print("================================================================")
    print("Por favor ingrese sus credenciales")
    print("================================================================\n")
    usua_nom = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")
    edad = input("Escriba su edad: ")
    id= input("Escriba su ID: ")
    
    # Verificar los datos de del usuario
    # definimos estas variables para controlar el usuario y si los datos son corresponden a los agregados
    usuario_valido = False
    nivel_usuario = None
    #recorremos una variable"usuario" en los usuarios preexistentes
    for usuario in usuarios_activos:
         #y si al recorrer la variable se encuentran los datos necesarios usuario_valido = True
        if usuario["nombre"] == usua_nom and usuario["contrasena"] == contraseña and usuario["edad"] == edad and usuario["id"] == id:
            usuario_valido = True
            nivel_usuario = usuario["nivel"]#ahora creamos una variable que busque dentro de la lista de usuarios el nivel de usuario
            break
        
#ponemos un if para condicionar lo que va a pasar si los datos que el usuario escribió son correctos, luego llamamos a la funcion -->
# "def menu_principal(nivel_usuario)" para realizar los procesos que hay dentro de esa funcion.
    if usuario_valido:
        print("\n================================================================")
        print("Inicio de sesión exitoso!")
        menu_principal(nivel_usuario)
    else:
        print("Las credenciales son incorrectas. Por favor intente nuevamente.") #si el usuario se equivoca volvemos a llamar a la funcion para 
        login()                                                                       #que lo intent de nuevo
login() # esto permite que sea lo primero que vea el usuario