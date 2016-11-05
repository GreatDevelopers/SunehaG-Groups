import xml.etree.ElementTree as ET
import subprocess

hostName="guru.gndec.ac.in"

def addbookmark(username,group):
    xml = subprocess.Popen(["ejabberdctl","private_get",username,hostName,"storage","storage:bookmarks"], stdout=subprocess.PIPE).stdout.read()
    print xml
    ET.register_namespace("","storage:bookmarks")
    root = ET.fromstring(xml)
    ET.SubElement(root,"conference",attrib={'jid':group,'autojoin':'true'})
    output=ET.tostring(root)
    print(output)
    subprocess.Popen(["ejabberdctl","private_set",username,hostName,output])


def send_invite(username,group):
    group = group.replace('/','_')
#    cmd="ejabberdctl send_direct_invitation "+group+" conference."+hostName+" none none "+username+"@"+hostName
#    os.system(cmd)
    #addbookmark(username,group+"@conference."+hostName)

check_group = []
def create_group(group):
    group = group.replace('/','_')
    if group not in check_group:
        check_group.append(group)
        #cmd="ejabberdctl create_room "+group+" conference."+hostName+" "+hostName
        #os.system(cmd)
        #cmd="ejabberdctl change_room_option "+group+" conference."+hostName+" allow_subscription true"
        #os.system(cmd)
        #cmd="ejabberdctl change_room_option "+group+" conference."+hostName+" persistent true"
        #os.system(cmd)
        #cmd="ejabberdctl change_room_option "+group+" conference."+hostName+" max_users 5000"
        #os.system(cmd)
        print "check group is working ", group
    print check_group
