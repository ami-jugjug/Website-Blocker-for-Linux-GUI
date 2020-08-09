# This file contains the logical code or the back end codes.

class Block():
    # host_address=r'/etc/hosts'
    # host_address = 'hosts'
    redirect='127.0.0.1'
    host_temp="/etc/hosts"
    def __init__(self):
        self.website_list=[]
        with open(self.host_temp) as file:
            content = file.readlines()
        for c in content:
            if '127.0.0.1' in c :
                if 'localhost' in c:
                    pass
                else:
                    self.website_list.append(c[10:])
    
    def block_website(self,item):
        self.website_list.append(item)
        with open(self.host_temp,'r+') as file:
            content = file.read()
            for website in self.website_list:
                if website in content:
                    pass
                else:
                    file.write(self.redirect+" "+website+"\n")

    def unblock_website(self,item):
        self.website_list.remove(item)
        with open(self.host_temp,'r') as file:
            content = file.readlines()
        with open(self.host_temp,'w') as file:
            file.seek(0)
            for c in content:
                if (item in c):
                    pass
                else:
                    file.write(c)

    def display_website(self):
        with open(file='hosts') as file:
            content = file.readlines()
            print(content,end = "\n\n")
            file.seek(0)
            for line in content:
                if any(website in line for website in website_list):
                    s = str(line)
                    print(s[10:])

    
    