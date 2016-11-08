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
        'Production Engineering':'PE',\
        'Environmental Science Engineering':'ESE', 'Industrial Engineering':'IE',\
        'Power Engineering':'PowE', \
        'Structural Engineering':'SE',\
        'VLSI Design':'VLSID',\
        'Energy Engineering':'EngE', 'Geo Technical Engineering ':'GEO',\
        'Soil Mechanics and Foundation Engineering':'SMFE'}

metadata = MetaData(engine)
table1 = Table('course_code', metadata, autoload=True)
table2 = Table('branch_code', metadata, autoload=Trues
table3 = Table('student_data', metadata, autoload=True)

#course_code
var1 = table1.select(table1.c.course_code)

#branch_code
var2 = table2.select(table2.c.course_code)

#student_data
var3 = table3.select(table3.c.course_code)

#list-comphrehension

#[(create_group([str(course_shortform[course_code[1]]),(str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])), (str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])+"_"+str(student_data[5])), (str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])+"_"+str(student_data[5])+"_"+str(student_data[9])), (str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])+"_"+str(student_data[5])+"_"+str(student_data[9])+"_"+str(student_data[10]))]), send_invite(str(student_data[7]),[(str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])), (str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])+"_"+str(student_data[5])), (str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])+"_"+str(student_data[5])+"_"+str(student_data[9])), (str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])+"_"+str(student_data[5])+"_"+str(student_data[9])+"_"+str(student_data[10]))])) for student_data in var3.execute() for branch_code in var2.execute() if str(student_data[1]) in str(branch_code[2]) and str(student_data[2]) in str(branch_code[0]) for course_code in var1.execute() if str(student_data[1]) in course_code[0]]


#student_data[1]: course_code
#branch_code[2]: course_code
#student_data[2]: branch_code
#branch_code[0]: branch_code
#course_code[1]: course_name
#course_code[0]: course_code
#branch_code[1]: branch_name
#student_data[5]: batch_year
#student_data[9]: ssection
#student_data[7]: college_roll_no
#student_data[10]: sgroup

for student_data in var3.execute():
   for branch_code in var2.execute():
        if str(student_data[1]) in str(branch_code[2]) and str(student_data[2]) in str(branch_code[0]):
            for course_code in var1.execute():
                if str(student_data[1]) in course_code[0]:
                    course = str(course_shortform[course_code[1]])
                    branch = str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])
                    passing_year = str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])+"_"+str(student_data[5])
                    section = str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])+"_"+str(student_data[5])+"_"+str(student_data[9])
                    group = str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])+"_"+str(student_data[5])+"_"+str(student_data[9])+"_"+str(student_data[10])
                    create_group([course, branch, passing_year, section, group])
                    send_invite(str(student_data[7]),[course, branch, passing_year, section, group])
                    print student_data[7]
