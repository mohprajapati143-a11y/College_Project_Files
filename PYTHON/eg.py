class Address:
    def __init__(self, street, city, state):
        self.street = street
        self.city = city
        self.state = state

    def details(self):
        return f"{self.street}, {self.city}, {self.state}"


class Employee:
    def __init__(self, num, name, salary, addr):
        self.num = num
        self.name = name
        self.salary = salary
        self.addr = addr

    def details(self):
        print(f"{self.num}, {self.name}, {self.salary}, {self.addr.details()}")


addr = Address('Kphb', 'Hyd', 'TG')
e = Employee(101, 'Amar', 25000, addr)
e.details()
addr = Address('phb', 'Panchayat', 'TG')
e = Employee(102, 'Amul', 35000, addr)
e.details()
