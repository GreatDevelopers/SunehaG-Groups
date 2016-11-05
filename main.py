from functions import *
from sqlalchemy import * # don't use * in production
# if you are using Mysql look for commented code

engine = create_engine('mysql://root:a@localhost/suneha_test')

course_shortform = {'B.Tech.':'BT', 'M.Tech.':'MT', 'MBA':'MBA', 'MCA':'MCA'}

#space FIXME
branch_shortform = {'Civil Engineering':'CE', 'Computer Science and Engineering':'CSE', \
        'Electrical Engineering':'EE', 'Electronics and Communication Engineering':'ECE',\
        'Information Technology':'IT', 'Masters in Business Administration':'MBA',\
        'Masters in Computer Application':'MCA', 'Mechanical Engineering':'ME',\
        'Production Engineering':'PE', 'Electrical Engineering':'EE',\
        'Electronics and Communication Engineering':'ECE',\
        'Environmental Science Engineering':'ESE', 'Industrial Engineering':'IE',\
        'Information Technology':'IT', 'Power Engineering':'PE', \
        'Production Engineering':'PE', 'Structural Engineering':'SE',\
        'VLSI Design':'VLSID', 'Computer Science and Engineering':'CSE',\
        'Energy Engineering':'EngE', 'Geo Technical Engineering ':'GEO',\
        'Soil Mechanics and Foundation Engineering':'SMFE'}

metadata = MetaData(engine)
table1 = Table('course_code', metadata, autoload=True)
table2 = Table('branch_code', metadata, autoload=True)
table3 = Table('student_data', metadata, autoload=True)

#course_code
var1 = table1.select(table1.c.course_code)
m1 = [i for i in var1.execute()]
print m1

#branch_code
var2 = table2.select(table2.c.course_code)
m2 = [i for i in var2.execute()]
print m2

#student_data
var3 = table3.select(table3.c.course_code)
m3 = [i for i in var3.execute()]
print m3

#print [(student_data[7], course_code[1], branch_code[1], student_data[5], student_data[9], student_data[10]) for student_data in m3 for branch_code in m2 if str(student_data[1]) in str(branch_code[2]) and str(student_data[2]) in str(branch_code[0]) for course_code in m1 if str(student_data[1]) in course_code[0]]

for student_data in m3:
   for branch_code in m2:
        if str(student_data[1]) in str(branch_code[2]) and str(student_data[2]) in str(branch_code[0]):
            for course_code in m1:
                if str(student_data[1]) in course_code[0]:
                    course = str(course_shortform[course_code[1]])
                    branch = str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])
                    passing_year = str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])+"_"+str(student_data[5])
                    section = str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])+"_"+str(student_data[5])+"_"+str(student_data[9])
                    group = str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])+"_"+str(student_data[5])+"_"+str(student_data[9])+"_"+str(student_data[10])
                    create_group(branch)
