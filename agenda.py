import guardado

contactos = {}

def mostrar_comandos():
    ayuda = """
    Agregar | Añadir contacto
    Remover | Eliminar contacto
    Mostrar | Mostrar contacto
    """
    print(ayuda)

def agregar_contacto():
    print("\n")
    nombre = input(" Nombre: ")
    numero = input(" Número: ")
    if (contactos.get(str(nombre)) == None):
        contactos[str(nombre)] = numero
        guardado.guardar(contactos)
    else:
        print(nombre + " ya está en tus contactos")

def remover_contacto():
    print("\n")
    nombre = input(" Nombre: ")
    if not (contactos.get(str(nombre)) == None):
        contactos.pop(str(nombre))
        print(nombre + " ha sido eliminado/a\n")
        guardado.guardar(contactos)
    else:
        print(" "+nombre + " no está en tus contactos")

def mostrar_contacto():
    print("\n")
    nombre = input(" Nombre (deje vacío para mostrar todos): ")
    if(nombre == "" ):
        a = 0
        print("\n---------------------")
        for i in contactos.items():
            a +=1
            print(" " + i[0] + " - " + i[1])
            if a <= (len(contactos.items()) - 1):
                print("------")
        print("---------------------")
    elif not (contactos.get(str(nombre)) == None):
        print("\n " +contactos.get(str(nombre)))
        print("--------")
    else:
        print("no se encontró a " + nombre)

def procesar_comando(comando):
    if comando == "AYUDA":
        mostrar_comandos()
    elif comando == "AGREGAR":
        agregar_contacto()
    elif comando == "REMOVER":
        remover_contacto()
    elif comando == "MOSTRAR":
        mostrar_contacto()
    else: 
        print("Comando -"+ comando +"- no encontrado, ingrese 'ayuda' para obtener una lista de comandos\n")
def ingresar_comando():
    comando = input("\nIngrese su comando: ")
    comando = comando.upper()
    comando = comando.strip()
    return comando

print("\nIngrese 'ayuda' para lista de comandos y 'salir' para terminar")  

comando = ingresar_comando()

contactos = guardado.cargar()

while not (comando.upper() == "SALIR"):
    procesar_comando(comando)
    comando = ingresar_comando()

print("\nPrograma terminado")   