import json

class Entity():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f'Сущность: {self.name}'

class Employee():
    def __init__(self,name,place):
        self.name = name
        self.place = place
    def __str__(self):
        return f'{self.name} работает в {self.place}'


if __name__ == '__main__':
    cat = Entity('Сугроб')
    print(cat)

    employee = Employee('Петя', 'Foxford')
    print(employee)

    data = [{"name": cat.name}, {"name": employee.name, "place": employee.place}]

    with open('data.json', 'w') as file:
        json.dump(data, file)