
filename = 'emails.txt'
contents = ''
with open(filename) as file_object:
    contents = file_object.read().lstrip("['").rstrip("']\n").split("', '")

duplicates = set([x for x in contents if contents.count(x) > 1])
removed_duplicates = list(set(contents) - duplicates)

filename = 'duplicate-free-email-list.txt'
with open(filename,'w') as file_object:
    file_object.write("['" + ("', '".join(removed_duplicates)) +  "']")
