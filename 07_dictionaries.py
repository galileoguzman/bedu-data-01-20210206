'''
How the dictionaries work in Python
'''

student_1 = {
    'name': 'Galileo',
    'age': 31,
    'city': 'Puerto Escondido',
    'state': 'Oaxaca'
}

student_2 = {
    'name': 'Sofia',
    'age': 4,
    'city': 'Zapopan'
}

print(student_2.get('state', 'N/A'))
# print(student_2['state'])

print(student_1)
print(type(student_1))

print(student_1['name'])
print(student_1['age'])

print(f'{student_1["name"]} is {student_1["age"]} years old.')

# galileo = 'galileo'
# print(galileo.upper())
# print(galileo.lower())
# print(galileo.capitalize())
