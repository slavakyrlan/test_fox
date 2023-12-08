import json
import unittest

from main import Entity, Employee


class TestStringMethods(unittest.TestCase):
    @staticmethod
    def fixture():
        with open('data.json') as json_file:
            return json.load(json_file)

    def test_data(self):
        data = self.fixture()
        self.assertEqual(len(data), 2)

        cat = Entity(**data[0])
        employee = Employee(**data[1])

        self.assertEqual(str(cat), 'Сущность: Сугроб')
        self.assertEqual(str(employee), 'Петя работает в Foxford')

    def test_difference(self):
        employee1 = Employee("Петя", 'горе')
        employee2 = Employee("Вася", 'долина')
        self.assertNotEqual(str(employee1), str(employee2))
