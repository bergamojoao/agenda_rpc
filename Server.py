from xmlrpc.server import SimpleXMLRPCServer
import sqlite3
import os
from Person import *
import socket

################### INICIALIZAÇÃO DO DATABASE ##################
if not os.path.isfile("database.db"):
    db = sqlite3.connect("database.db")
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE person (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            phone TEXT NOT NULL
    );
    """)
else:
    db = sqlite3.connect("database.db")
################################################################

with SimpleXMLRPCServer(('localhost', 8080), allow_none=True) as server:

    def inserir(nome, endereco, telefone):
        while True:
            try:
                person = Person()
                person.setName(nome)
                person.setAddress(endereco)
                person.setPhone(telefone)
                socket.setdefaulttimeout(5)
                createPerson(person, db)
                socket.setdefaulttimeout(None) 
                return True
            except Exception as ex:
                raise Exception("Erro ao inserir: " + str(ex))
                db.cursor().execute("ROLLBACK;")

    def alterar(id, nome, endereco, telefone):
        while True:
            try:
                person = Person()
                person.setId(id)
                person.setName(nome)
                person.setAddress(endereco)
                person.setPhone(telefone)
                socket.setdefaulttimeout(5)
                updatePerson(person, db)
                socket.setdefaulttimeout(None) 
                return True
            except Exception as ex:
                raise Exception("Erro ao alterar contato: " +str(ex))
                db.cursor().execute("ROLLBACK;")

    def consultar(nome):
        try:
            result_list = readPersonByName(nome, db)
            return result_list
        except Exception as ex:
            raise Exception("Erro ao consultar: " + str(ex))

    def consultar_id(id):
        try:
            result = readPersonById(id, db)
            return result
        except Exception as ex:
            raise Exception("Erro ao consultar por id: " + str(ex))

    def remover(id):
        while True:
            try:
                socket.setdefaulttimeout(5)
                deletePerson(id, db)
                socket.setdefaulttimeout(None) 
                return True
            except Exception as ex:
                raise Exception("Erro ao remover contato: " + str(ex))
                db.cursor().execute("ROLLBACK;")

    server.register_function(inserir)
    server.register_function(alterar)
    server.register_function(consultar)
    server.register_function(consultar_id)
    server.register_function(remover)

    server.serve_forever()

db.close()