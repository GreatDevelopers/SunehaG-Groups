import mysql.connector
import os

cnx = mysql.connector.connect(user='root', password='**', database='sunehag_test')
course_code = []
branch = []
student = []


# course code
cursor1 = cnx.cursor()
query1 = ("select course_code from course_code;")
cursor1.execute(query1)

for i in cursor1:
    course_code.append(int(i[0]))

course_code = list(set(course_code))
print("course code: %s" %course_code)

dic_course_code = {}

# branch code
cursor3 = cnx.cursor()
query3 = ("select branch_code from branch_code;")
cursor3.execute(query3)

list_branch_code = []
for i in cursor3:
    list_branch_code.append(i[0])

print("branch code: %s" %list_branch_code)

dic_branch_code = {}

# semester
cursor5 = cnx.cursor()
query5 = ("select semester from student_data;")
cursor5.execute(query5)

semester = []
for i in cursor5:
    semester.append(i[0])

semester = list(set(semester))
print("semester: %s"%semester)

dic_semester = {}

# ssection
cursor7 = cnx.cursor()
query7 = ("select ssection from student_data;")
cursor7.execute(query7)

ssection = []
for i in cursor7:
    ssection.append(i[0])

ssection = list(set(ssection))
print("ssection: %s"%ssection)

dic_ssection = {}


# sgroup
cursor9 = cnx.cursor()
query9 = ("select sgroup from student_data;")
cursor9.execute(query9)

sgroup = []
dic_sgroup = {}
for i in cursor9:
    sgroup.append(i[0])

sgroup = list(set(sgroup))
print("sgroup: %s" %sgroup)

for i in course_code:
    cursor2 = cnx.cursor()
    query2 = ("select college_roll_no from student_data where course_code="+str(i)+";")
    cursor2.execute(query2)
    list_course_code = []
    for j in cursor2:
        list_course_code.append(int(j[0]))
    #if len(list_course_code) != 0:
    dic_course_code[int(i)]=list_course_code
    cursor2.close ()
    for j in list_branch_code:
        cursor4 = cnx.cursor()
        query4 = ("select college_roll_no from student_data where course_code \
            ="+str(i)+" and branch_code = "+str(j)+";")
        #print query4
        cursor4.execute(query4)
        branch_key = []
        branch_item = []
        branch_key.append(int(i))
        branch_key.append(int(j))
        #print branch_key
        #print branch_key
        for z in cursor4:
            branch_item.append(int(z[0]))
        #if len(branch_item) != 0:
        dic_branch_code[str(i)+"_"+str(j)] = branch_item
        #print branch_item
        cursor4.close()
        for z in semester:
            cursor6 = cnx.cursor()
            query6 = ("select college_roll_no from student_data where course_code \
                = "+str(i)+" and branch_code = "+str(j)+" and semester = "+str(z)+";")
            cursor6.execute(query6)
            semester_item = []
            for x in cursor6:
                semester_item.append(int(x[0]))
            #if len(semester_item) != 0:
            dic_semester[str(i)+"_"+str(j)+"_"+str(z)] = semester_item
            cursor6.close()
            for x in ssection:
                cursor8 = cnx.cursor()
                query8 = ("select college_roll_no from student_data where course_code \
                     = "+str(i)+" and branch_code = "+str(j)+" and semester = "+str(z)+\
                        " and ssection = '"+str(x)+"';")
                #print query8
                cursor8.execute(query8)
                ssection_item = []
                for y in cursor8:
                    ssection_item.append(int(y[0]))
                #if len(ssection_item) != 0:
                dic_ssection[str(i)+"_"+str(j)+"_"+str(z)+"_"+str(x)] = ssection_item
                cursor8.close()
                for y in sgroup:
                    sgroup_item = []
                    cursor10 = cnx.cursor()
                    query10 = ("select college_roll_no from student_data where \
                        course_code = "+str(i)+" and branch_code = "+str(j)+" and semester = "\
                            +str(z)+" and ssection = '"+str(x)+"' and sgroup = '"+str(y)+"';")
                    cursor10.execute(query10)
                    for k in cursor10:
                        sgroup_item.append(int(k[0]))
                    #if len(sgroup_item) != 0:
                    dic_sgroup[str(i)+"_"+str(j)+"_"+str(z)+"_"+str(x)+"_"+str(y)] = sgroup_item
                    cursor10.close()


print dic_course_code
print dic_branch_code
print dic_semester
print dic_ssection
print dic_sgroup


cursor11 = cnx.cursor()
query11 = ("select course_name from course_code;")
cursor11.execute(query11)

course_name = []
for i in cursor11:
    course_name.append(str(i[0]))

print course_name

print dic_course_code[1]
for i,j in zip(course_code, course_name):
    z = 0
    ccmd="ejabberdctl create_room "+str(j)+ " conference.lab.gdy.club lab.gdy.club"
    os.system(ccmd)
    ccmd6="ejabberdctl change_room_option "+str(j)+ " conference.lab.gdy.club allow_subscription true"
    os.system(ccmd6)
    for z in dic_course_code[i]:
        cmd="ejabberdctl send_direct_invitation "+str(j)+ " conference.lab.gdy.club none none "+str(z)+"@lab.gdy.club"
        os.system(cmd)


cursor12 = cnx.cursor()
query12 = ("select branch_code, branch_name, course_code from branch_code;")
cursor12.execute(query12)

list_branch = {}
for i in cursor12:
    list_branch[(str(str(i[2]))+"_"+str(i[0]))] = str(i[1])

print "list_branch"
print list_branch


for i in dic_branch_code:
    flag=True
    for j in dic_branch_code[i]:
        if flag==True:
    	    ccmd2="ejabberdctl create_room "+str(list_branch[i]).replace(' ','_')+ " conference.lab.gdy.club lab.gdy.club"
            print ccmd2
            os.system(ccmd2)
            ccmd7="ejabberdctl change_room_option "+str(list_branch[i]).replace(' ','_')+ " conference.lab.gdy.club allow_subscription true"
            os.system(ccmd7)
            flag=False
	cmd1="ejabberdctl send_direct_invitation "+str(list_branch[i]).replace(' ','_') + " conference.lab.gdy.club none none "+str(j)+"@lab.gdy.club"
	os.system(cmd1)

cursor13 = cnx.cursor()
query13 = ("select course_code, branch_code, semester, ssection, sgroup from student_data;")
cursor13.execute(query13)

list_semester = {}
list_ssection = {}
list_sgroup = {}
for i in cursor13:
    #list_semester[str(i[0]+i[1]+i[2])] = str(i[1]+i[2])
    list_semester[str(str(i[0])+"_"+str(i[1])+"_"+str(i[2]))] = list_branch[str(str(i[0])+"_"+str(i[1]))]+"_sem_"+str(i[2])
    list_ssection[str(str(i[0])+"_"+str(i[1])+"_"+str(i[2])+"_"+str(i[3]))] = list_branch[str(str(i[0])+"_"+str(i[1]))]+"_sem_"+str(i[2])+"_section_"+str(i[3])
    list_sgroup[str(str(i[0])+"_"+str(i[1])+"_"+str(i[2])+"_"+str(i[3])+"_"+str(i[4]))] = list_branch[str(str(i[0])+"_"+str(i[1]))]+"_sem_"+str(i[2])+"_section_"+str(i[3])+"_group_"+str(i[4])
#print str(str(i[0])+"_"+str(i[1]))
print list_semester
print list_ssection
print list_sgroup

for i in list_semester:
    flag=True
    for j in dic_semester[i]:
    	if flag==True:
            ccmd3="ejabberdctl create_room "+str(list_semester[i]).replace(' ','_')+ " conference.lab.gdy.club lab.gdy.club"
            os.system(ccmd3)
            print ccmd3
            ccmd8="ejabberdctl change_room_option "+str(list_semester[i]).replace(' ','_')+ " conference.lab.gdy.club allow_subscription true"
            os.system(ccmd8)
            flag=False
	cmd2="ejabberdctl send_direct_invitation "+str(list_semester[i]).replace(' ','_')+" conference.lab.gdy.club none none "+str(j)+"@lab.gdy.club"
	os.system(cmd2)

for i in list_ssection:
    flag=True
    for j in dic_ssection[i]:
        if flag==True:
            ccmd4="ejabberdctl create_room "+str(list_ssection[i]).replace(' ','_')+ " conference.lab.gdy.club lab.gdy.club"
            os.system(ccmd4)
            print ccmd4
            ccmd9="ejabberdctl change_room_option "+str(list_ssection[i]).replace(' ','_')+ " conference.lab.gdy.club allow_subscription true"
            os.system(ccmd9)
            flag=False
        cmd3="ejabberdctl send_direct_invitation "+str(list_ssection[i]).replace(' ','_')+" conference.lab.gdy.club none none "+str(j)+"@lab.gdy.club"
        os.system(cmd3)

for i in list_sgroup:
	flag=True
	for j in dic_sgroup[i]:
            if flag==True:
                ccmd5="ejabberdctl create_room "+str(list_sgroup[i]).replace(' ','_')+ " conference.lab.gdy.club lab.gdy.club"
                os.system(ccmd5)
                ccmd10="ejabberdctl change_room_option "+str(list_sgroup[i]).replace(' ','_')+ " conference.lab.gdy.club allow_subscription true"
                os.system(ccmd10)
                flag=False
                print ccmd5
            cmd4="ejabberdctl send_direct_invitation "+str(list_sgroup[i]).replace(' ','_')+" conference.lab.gdy.club none none "+str(j)+"@lab.gdy.club"
            os.system(cmd4)
