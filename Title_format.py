def format_name(first_name, last_name):
    name = first_name.title() +" "+ last_name.title()
    return name

fname = input('Enter First name: ')
lname = input('Enter Last name: ')

full_name = format_name(fname, lname)
print(full_name)