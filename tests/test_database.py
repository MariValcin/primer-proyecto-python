import csv
import copy
import config
import helpers
import unittest
import database as db

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Clientes.lista = [
            db.Cliente("05M", "Garlo", "Desmarra"),
            db.Cliente("20A", "JeanP", "Cass"),
            db.Cliente("23E", "Sebastian", "Ramirez")

        ]

    def test_buscar_cliente(self):
        cliente_existente = db.Clientes.buscar("05M")
        cliente_inexistente = db.Clientes.buscar("06M")
        self.assertIsNotNone(cliente_existente)
        self.assertIsNone(cliente_inexistente)


    def test_crear_cliente(self):
        nuevo_cliente = db.Clientes.crear("30J", "Victor", "Ramirez")
        self.assertEqual(len(db.Clientes.lista), 4)
        self.assertEqual(nuevo_cliente.dni, "30J")
        self.assertEqual(nuevo_cliente.nombre, "Victor")
        self.assertEqual(nuevo_cliente.apellido, "Ramirez")

    def test_modificar_cliente(self):
        cliente_a_modificar = copy.copy(db.Clientes.buscar("20A"))
        cliente_modificado = db.Clientes.modificar("20A", "JP", "Cass")
        self.assertEqual(cliente_a_modificar.nombre, "JeanP")
        self.assertEqual(cliente_modificado.nombre, "JP")

    def test_borrar_cliente(self):
        cliente_borrado = db.Clientes.borrar("23E")
        cliente_rebuscado = db.Clientes.buscar("23E")
        self.assertEqual(cliente_borrado.dni, "23E")
        self.assertIsNone(cliente_rebuscado)    

    def test_dni_valido(self):
        self.assertTrue(helpers.dni_valido("00A", db.Clientes.lista))
        self.assertFalse(helpers.dni_valido("111111S", db.Clientes.lista))
        self.assertFalse(helpers.dni_valido("T33", db.Clientes.lista))
        self.assertFalse(helpers.dni_valido("20A", db.Clientes.lista))
        self.assertFalse(helpers.dni_valido("222", db.Clientes.lista))

    def test_escritura_csv(self):
        db.Clientes.borrar("05M")
        db.Clientes.borrar("20A")
        db.Clientes.modificar("23E", "Dylan", "Ramirez")

        dni, nombre, apellido = None, None, None
        with open(config.DATABASE_PATH,newline="\n") as fichero:
            reader = csv.reader(fichero, delimiter=";")
            dni, nombre, apellido = next(reader)

        self.assertEqual(dni, "23E")
        self.assertEqual(nombre, "Dylan")
        self.assertEqual(apellido, "Ramirez")
        
             