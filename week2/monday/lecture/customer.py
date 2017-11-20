class Address:
    def __init__(self):
        self.street = ''
        self.state = ''
        self.zipCode = ''

class Customer(object):
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.address = []

customer = Customer()
customer.firstName = 'John'
customer.lastName = 'Doe'

address1 = Address()
address1.street = "1200 Richmond Ave"
address1.state = 'TX'
address.zipCode = '77042'

customer.address.append(address1)

class Job:
    def __init__(self):
        self.title = ''
        self.location = ''
        self.department = ''

class Employee(object):
    def __init__(self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name
        self.job = Job()

employee = Employee('John','Doe')
employee.job.title = 'Mechanic'
employee.job.location = 'Houston'
employee.job.department = 'IT'

print(employee.firstName + ' ' + employee.lastName)
print(employee.job.title + ' ' + employee.job.location + ' ' + employee.job.department)
