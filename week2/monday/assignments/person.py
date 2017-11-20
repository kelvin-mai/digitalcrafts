class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greeting_count += 1
    def print_contact_info(self):
        print(self.name + "'s email: " + self.email + ', ' + self.name + "'s phone number: " + self.phone)
    def add_friend(self, friend):
        self.friends.append(friend)
    def num_friends(self):
        return len(self.friends)
    def __repr__(self):
        return self.name + 'object'

sonny = Person('Sonny','sonny@hotmail.com','482-485-4948')
jordan = Person('Jordan','jordan@aol.com','495-586-3456')
sonny.greet(jordan)
jordan.greet(sonny)
# print(sonny.email + ' ' + sonny.phone)
# print(jordan.email + ' ' + jordan.phone)
sonny.print_contact_info()
jordan.print_contact_info()

jordan.add_friend(sonny)
print(jordan.friends[0].name)
print(jordan.num_friends())
print(jordan.greeting_count)
print(jordan)
