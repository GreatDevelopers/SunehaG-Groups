import os
from functions import *
from sqlalchemy import * # don't use * in production
# if you are using Mysql look for commented code

#engine = create_engine('mysql://root:a@localhost/suneha_test')
engine = create_engine('mysql://<username>:<password>@<host>/<database name>')

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

#course_code
connection = engine.connect()
course_query = text('select course_code, course_name from course_code')

#branch_code
branch_query = text('select branch_code, branch_name, course_code from branch_code')

#student_data
student_query = text('select course_code, branch_code, ssection, sgroup, batch, college_roll_no from student_info where branch_code=21 and batch=2014')

#student_data[0]: course_code
#branch_code[2]: course_code
#student_data[1]: branch_code
#branch_code[0]: branch_code
#course_code[1]: course_name
#course_code[0]: course_code
#branch_code[1]: branch_name
#student_data[4]: batch_year
#student_data[2]: ssection
#student_data[5]: college_roll_no
#student_data[3]: sgroup

create_group(['GNDEC'])
for student_data in connection.execute(student_query):
   for branch_code in connection.execute(branch_query):
       if str(student_data[0]) in str(branch_code[2]) and str(student_data[1]) in str(branch_code[0]):
           for course_code in connection.execute(course_query):
               if str(student_data[0]) in str(course_code[0]):
                    course = str(course_shortform[course_code[1]])
                    branch = str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])
                    passing_year = str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])+str(student_data[4])[-2:]
                    section = str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])+str(student_data[4])[-2:]+"_"+str(student_data[2]).replace('/','')
                    group = str(course_shortform[course_code[1]])+"_"+str(branch_shortform[branch_code[1]])+str(student_data[4])[-2:]+"_"+str(student_data[2]).replace('/','')+"_"+str(student_data[3])
                    print course, branch, passing_year, section, group
                    create_group([course, branch, passing_year, section, group])
                    send_invite(str(student_data[5]),[course, branch, passing_year, section, group])
   send_invite(str(student_data[5]), ['GNDEC'])
   print student_data[5]
