import random, string

suffix = [
    "@yahoo.com",
    "@gmail.com",
    "@hotmail.com",
    "@aol.com",
    "@msn.com",
    "@apple.com"
]

emails = []
for i in range(50):
    emails.append(''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(5,10)) ) + suffix[random.randint(0,len(suffix)-1)] )

# insert duplicates
for i in range(10):
    emails.insert(random.randint(0,len(emails)-1) , emails[i])

filename = 'emails.txt'
with open(filename,'w') as file_object:
    file_object.write("['" + ("', '".join(emails)) +  "']")
