import requests
from bs4 import BeautifulSoup
from Color import bcolors
import re
import urllib3
urllib3.disable_warnings()

def cleann(clear):
    clean = re.sub('<em>','',clear)
    clean = re.sub('<b>','',clear)
    clean = re.sub('</b>','', clear)
    clean = re.sub('</em>','', clear)
    clean = re.sub('<strong>','', clear)
    clean = re.sub('</strong>','', clear)
    clean = re.sub('<wbr>','', clear)
    clean = re.sub('</wbr>','', clear)
    return clean


class Yahoo_search:
    
    email_list = []
    facebook = []
    instagram = []

    def __init__(self , Target):
        
        self.Target = Target
        self.r = requests.get("https://search.yahoo.com/search?p=%40{}&fr=yfp-t&ei=UTF-8&fp=1'".format(Target))
        self.soup = BeautifulSoup(self.r.content , 'html.parser')
        self.html2 = self.soup.prettify()
        self.result = self.soup.text
        self.html = cleann(self.result)
    
    def get_emails(self):
        self.rgx = re.compile(r'[a-zA-Z0-9./-_+#]+'+'@+'+r'{}'.format(self.Target) , re.VERBOSE)
        self.tmp_email = re.findall(self.rgx ,self.html)
        for i in self.tmp_email:
            if i.split('@')[0] not in ('"',"'"):
                self.email_list.append(i)
     
    def get_pages(self):

        self.face_rgx = re.compile(r'(?:https?:)?\/\/(?:www\.)?(?:facebook|fb)\.com\/(?P<profile>(?![A-z]+\.php)(?!marketplace|gaming|watch|me|messages|help|search|groups)[A-z0-9_\-\.]+)\/?' ,  re.VERBOSE)
        self.Fac_page = re.findall(self.face_rgx , self.html2)
        if len(self.Fac_page) != 0:
            for i in self.Fac_page:
                self.facebook.append(i)
                
        self.insta_rgx = re.compile(r'(?:https?:)?\/\/(?:www\.)?(?:instagram\.com|instagr\.am)\/(?P<username>[A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)' ,  re.VERBOSE)
        self.insta_page = re.findall(self.insta_rgx , self.html2)
        if len(self.insta_page) != 0:
            for i in self.insta_page:  
                self.instagram.append(i)