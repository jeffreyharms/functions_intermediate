from asyncio.windows_events import NULL


x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# change the 10 in x to 15
# print(x[1])
# new_place = x[1]
# print(new_place)
# new_place[0] = 15
# print(new_place)
# x[1] = new_place
# print(x)
x[1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
print(students[0])
students[0]['last_name'] = 'Bryant'
print(students[0])

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
print(z)
z[0]['y'] = 30
print(z)

cohort = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(element):
    print(cohort)
    for undergrad in range(0, len(element)):
        print("first_name - ", cohort[undergrad]['first_name'])
        print("last_name - ", cohort[undergrad]['last_name'])
        undergrad += 1
        
iterateDictionary(cohort)



# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(element):
    print(len(element['locations']))
    print(" LOCATIONS")
    for n in range(0, len(element['locations'])):
        print(element['locations'][n])
    print(len(element['instructors']))
    print(" INSTRUCTORS")
    for b in range(0, len(element['instructors'])):
        print(element['instructors'][b])

printInfo(dojo)
