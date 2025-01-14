name_one = input("Enter name [Men]: ").lower()
name_two = input("Enter name [Women]: ").lower()

concatenates_name = name_one + name_two 

t = concatenates_name.count('t')
r = concatenates_name.count('r')
u = concatenates_name.count('u')
e = concatenates_name.count('e')

l = concatenates_name.count('l')
o = concatenates_name.count('o')
v = concatenates_name.count('v')
e = concatenates_name.count('e')

true = (t*10)+(r*10)+(u*10)+(e*10)
love = (l+o+v+e)

true_love = true+love

print (true_love)