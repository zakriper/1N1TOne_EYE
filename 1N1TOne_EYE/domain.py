import requests
import re
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings()

class req_domain:
    
    email_list = []
    facebook = []
    instagram = []
    
    def __init__(self ,Target ,pages):

        self.pages = pages
        self.Target = Target
        header = {
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
        }

        self.r = requests.get('https://www.{}/{}'.format(self.Target , self.pages) , headers=header , verify=False , timeout= 10)
        if self.r.status_code == 200 or self.r.status_code == 300:
            self.soup = BeautifulSoup(self.r.content , "html.parser")
            self.html = self.soup.prettify()

    def Get_emails(self):
        
        self.rgx = re.compile(r'[a-zA-Z0-9./-_+#]+'+'@+'+r'[a-zA-Z0-9./-_+#]+' , re.VERBOSE)
        self.tmp_email = re.findall(self.rgx ,self.html)

        if len(self.tmp_email) !=0:
            for i in self.tmp_email:
                if  i.split('@')[0] not in ('"',"'"):
                    self.email_list.append(i)
            
    


    def get_pages(self):

        self.face_rgx = re.compile(r'(?:https?:)?\/\/(?:www\.)?(?:facebook|fb)\.com\/(?P<profile>(?![A-z]+\.php)(?!marketplace|gaming|watch|me|messages|help|search|groups)[A-z0-9_\-\.]+)\/?' ,  re.VERBOSE)
        self.Fac_page = re.findall(self.face_rgx , self.html)

        if len(self.Fac_page) != 0:
            for i in self.Fac_page:
                self.facebook.append(i)

        self.insta_rgx = re.compile(r'(?:https?:)?\/\/(?:www\.)?(?:instagram\.com|instagr\.am)\/(?P<username>[A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)' ,  re.VERBOSE)
        self.insta_page = re.findall(self.insta_rgx , self.html)

        if len(self.insta_page) != 0:
            for i in self.Fac_page:
                self.instagram.append(i)