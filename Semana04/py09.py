#print('Imported my_module...')

#test = 'Test String'
# def find_index(to_search, target):
#	'''Find the index of a value in a sequence'''
#	for i, value in enumerate(to_search):
#		if value == target:
#			return i

#	return -1
#import sys
#sys.path.append('/home/pedro/Área de Trabalho/SEMB2/SEII-PedroJacobFavoreto/Semana04')


#from my_module import find_index, test


#courses = ['History', 'Math', 'Physics', 'CompSci']

#index = find_index(courses, 'Math')
#print(index)
#print(test)

#print(sys.path)

import random
import math
import datetime
import calendar
import os

courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choice(courses)
rads = math.radians(90)
today = datetime.date.today()

print(random_course)
print(math.sin(rads))
print(today)
print(calendar.isleap(2017))
print(os.getcwd())
print(os.__file__)



