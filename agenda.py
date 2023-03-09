contactos = {}

def mostrar_comandos():
    ayuda = """
    Agregar | Añadir contacto
    Remover | Eliminar contacto
    Mostrar | Mostrar contacto
    """
    print(ayuda)

def agregar_contacto():
    nombre = input(" nombre: ")
    numero = input(" número: ")
    if (contactos.get(str(nombre)) == None):
        contactos[str(nombre)] = numero
    else:
        print(nombre + " ya está en tus contactos")

def remover_contacto():
    nombre = input(" nombre: ")
    if not (contactos.get(str(nombre)) == None):
        contactos.pop(str(nombre))
        print(nombre + " ha sido eliminado/a\n")
    else:
        print(" "+nombre + " no está en tus contactos")

def mostrar_contacto():
    nombre = input(" nombre (deje vacío para mostrar todos): ")
    if(nombre == "" ):
        print("\n------")
        for i in contactos.items():
            print(" " + i[0] + " - " + i[1])
            print("----")
        print("------")
    elif not (contactos.get(str(nombre)) == None):
        print("\n " +contactos.get(str(nombre)))
        print("------")
    else:
        print("no se encontró el contacto especificado")

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
        print("Comando no encontrado, ingrese 'ayuda' para obtener una lista de comandos\n")
def ingresar_comando():
    comando = input("\nIngrese su comando: ")
    comando = comando.upper()
    comando = comando.strip()
    return comando

print("\nIngrese 'ayuda' para lista de comandos y 'salir' para terminar")  

comando = ingresar_comando()

while not (comando.upper() == "SALIR"):
    procesar_comando(comando)
    comando = ingresar_comando()

print("\nPrograma terminado")   