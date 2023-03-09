import json
import os

def guardar(contactos):
    f = open("contacts.json", "w")
    f.write(json.dumps(contactos))
    f.close

def cargar():
    if os.path.exists("contacts.json"):
        f = open("contacts.json", "r") 
        return json.loads(f.read()) 
    else:
        return None