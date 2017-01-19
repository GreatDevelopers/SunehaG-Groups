import os
import xml.etree.ElementTree as ET
import subprocess

class sunehaG():

	def __init__(self,name):
		self.hostName=name

	def addbookmark(self,username,groups):
		xml = subprocess.Popen(["ejabberdctl","private_get",username, \
		self.hostName,"storage","storage:bookmarks"], \
		stdout=subprocess.PIPE).stdout.read()

		print xml
		ET.register_namespace("","storage:bookmarks")
		root = ET.fromstring(xml)
		for group in groups:
			group = group.replace('/','-')
			group = group.replace(' ','-')
			ET.SubElement(root,"conference",attrib={'jid':group+"@conference."+ \
			self.hostName,'autojoin':'true'})

		output=ET.tostring(root)
		print(output)
		subprocess.Popen(["ejabberdctl","private_set",username,self.hostName,output])


	def send_invite(self,username,groups):
		username = username.replace('/','_')
		username = username.replace(' ','_')
		for group in groups:
			group = group.replace('/','-')
			group = group.replace(' ','-')
			print group
			cmd="ejabberdctl set_room_affiliation "+group+" conference."+ \
			self.hostName+" "+username+"@"+self.hostName+" member" 
			os.system(cmd)
			cmd="ejabberdctl send_direct_invitation "+group+" conference."+ \
			self.hostName+" none none "+username+"@"+self.hostName
			os.system(cmd)
		self.addbookmark(username,groups)

	check_group = []
	def create_group(self,groups):
		for group in groups:
			group = group.replace('/','-')
			group = group.replace(' ','-')
			if group not in self.check_group:
				self.check_group.append(group)
				cmd="ejabberdctl create_room "+group+" conference."+ \
				self.hostName+" "+self.hostName
				os.system(cmd)

				cmd="ejabberdctl change_room_option "+group+ \
				" conference."+self.hostName+" allow_subscription true"

				os.system(cmd)
				cmd="ejabberdctl change_room_option "+group+ \
				" conference."+self.hostName+" persistent true"
				os.system(cmd)

				cmd="ejabberdctl change_room_option "+group+ \
				" conference."+self.hostName+" max_users 5000"
				os.system(cmd)

				cmd="ejabberdctl change_room_option "+group+ \
				" conference."+self.hostName+" members_only true"
				os.system(cmd)

				print cmd
				print "check group is working ", group, self.hostName
