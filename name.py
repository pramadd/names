students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def names(name):
    for i in students:
        print i['first_name'],i['last_name']

names(students)
 

 #part1
 #--------------------------------------------------


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def Names(data, title): 
	print title
	for i in range(len(data)): 
		full_name = data[i]['first_name'] + " " + data[i]['last_name']
		print (i + 1), " - ", full_name, " - ", (len(full_name) - 1)

students = users['Students']
instructors = users['Instructors']

Names(students, 'Students')
Names(instructors, 'Instructors')
