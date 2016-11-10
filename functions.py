import os
import xml.etree.ElementTree as ET
import subprocess

hostName="guru.gndec.ac.in"

def addbookmark(username,groups):
    xml = subprocess.Popen(["ejabberdctl","private_get",username,hostName,"storage","storage:bookmarks"], stdout=subprocess.PIPE).stdout.read()
    print xml
    ET.register_namespace("","storage:bookmarks")
    root = ET.fromstring(xml)
    for group in groups:
        group = group.replace('/','_')
        group = group.replace(' ','_')
        ET.SubElement(root,"conference",attrib={'jid':group+"@conference."+hostName,'autojoin':'true'})
    output=ET.tostring(root)
    print(output)
    subprocess.Popen(["ejabberdctl","private_set",username,hostName,output])


def send_invite(username,groups):
    for group in groups:
        group = group.replace('/','_')
        group = group.replace(' ','_')
        print group
        cmd="ejabberdctl set_room_affiliation "+group+" conference."+hostName+" "+username+"@"+hostName+" member"
        os.system(cmd)
        cmd="ejabberdctl send_direct_invitation "+group+" conference."+hostName+" none none "+username+"@"+hostName
        os.system(cmd)
    addbookmark(username,groups)

check_group = []
def create_group(groups):
    for group in groups:
        group = group.replace('/','_')
        group = group.replace(' ','_')
        if group not in check_group:
            check_group.append(group)
            cmd="ejabberdctl create_room "+group+" conference."+hostName+" "+hostName
            os.system(cmd)
            cmd="ejabberdctl change_room_option "+group+" conference."+hostName+" allow_subscription true"
            os.system(cmd)
            cmd="ejabberdctl change_room_option "+group+" conference."+hostName+" persistent true"
            os.system(cmd)
            cmd="ejabberdctl change_room_option "+group+" conference."+hostName+" max_users 5000"
            os.system(cmd)
            cmd="ejabberdctl change_room_option "+group+" conference."+hostName+" members_only true"
            os.system(cmd)
            print "check group is working ", group
