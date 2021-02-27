import sqlite3

class Person:
    def setId(self, id):
        self.__id = id
    
    def getId(self):
        return self.__id

    def setName(self, name):
        self.__name = name
    
    def getName(self):
        return self.__name

    def setAddress(self, address):
        self.__address =  address
    
    def getAddress(self):
        return self.__address
    
    def setPhone(self, phone):
        self.__phone = phone
    
    def getPhone(self):
        return self.__phone


def allPeople(connection) -> list:
    result = []
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM person")
    for line in cursor.fetchall():
        person = Person()
        person.setId(line[0])
        person.setName(line[1])
        person.setAddress(line[2])
        person.setPhone(line[3])
        result.append(person)
    return result

def createPerson(person, connection):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO person (name, address, phone) VALUES (?,?,?)", (person.getName(), person.getAddress(), person.getPhone()))
    connection.commit()

def readPersonByName(name, connection) -> list:
    result = []
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM person WHERE name LIKE  ? ", ('%'+name+'%',))
    for line in cursor.fetchall():
        person = Person()
        person.setId(line[0])
        person.setName(line[1])
        person.setAddress(line[2])
        person.setPhone(line[3])
        result.append(person)
    return result

def readPersonById(id, connection) -> Person:
    result = []
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM person WHERE id = ? ", (str(id)))
    line = cursor.fetchone() 
    person = Person()
    person.setId(line[0])
    person.setName(line[1])
    person.setAddress(line[2])
    person.setPhone(line[3])
    return person

def updatePerson(person, connection):
    cursor = connection.cursor()
    cursor.execute("UPDATE person SET name=?, address=?, phone=? WHERE id=?", (person.getName(), person.getAddress(), person.getPhone(), person.getId()) )
    connection.commit()

def deletePerson(id, connection):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM person WHERE id=?", (str(id),) )
    connection.commit()

