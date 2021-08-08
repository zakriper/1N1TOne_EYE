from bs4 import BeautifulSoup
from Yahoo import Yahoo_search
from Color import  bcolors
import pyfiglet
from domain import req_domain
from GooGle_Bot import Google_search
import urllib3
urllib3.disable_warnings()



text = "1N1TOne Club "
print(pyfiglet.figlet_format(text))
print(bcolors.green + "1N1TOne_EYE is simple OSINT Tool To search For Emails And Social Media Accounts And Accounts related To The Target Chosen\n")
print(bcolors.cyan + "contact us on : \nWebsite : https://in1tone.wordpress.com/\nInstagrame : @1n1tone\nFacebook : https://www.facebook.com/1N1TOne/")
print("\n")


domain = input(str(bcolors.lightblue +'Enter Target Domain For Ex ( Exemple.com ) : '))
if len(domain) <= 3:
    print("nothing to search")
    quit()
print("\n")

print(bcolors.blue + "============================================== GooGle Search ==============================================")
print(bcolors.orange + "searching in google\n")
r = Google_search(domain)
google_emails = []
google_face = []
google_insta = []

try:
    emails = Google_search.get_emails(r)
    socila_media = Google_search.get_pages(r)
except:
    pass
try:
    if len(Google_search.email_list) == 0:
        print(bcolors.red + "Ops Sorry No Email Found \n")
    elif len(Google_search.email_list) !=0:
        for e in Google_search.email_list:
            if e not in google_emails:
                google_emails.append(e)

    if len(Google_search.instagram) == 0:
        print(bcolors.red + "No Instagram account Found \n")
    elif len(Google_search.instagram) !=0 :
        for I in Google_search.instagram:
            if I not in google_insta:
                google_insta.append(I)

    if len(Google_search.facebook) == 0:
        print(bcolors.red + "No Facebook Page Found \n")
    elif len(Google_search.facebook) !=0:
        for F in Google_search.facebook:
            if F not in google_face:
                google_face.append(F)
except:
    pass
try:

    for i in google_emails:
        print(bcolors.orange + "This Email Found On GooGle may related To your Target : "  + i + "\n")

    for i in google_face:
        if i != "tr" and i != "p" and i != "pages":
            print(bcolors.blue +  'This Facebook account Found On GooGle may related To your Target : ' + "https://www.facebook.com/"+ i)

    for i in google_insta:
        if i != "tr" and i != "p" and i != "pages":
            print(bcolors.green + 'This Instagrame account Found On GooGle may related To your Target : ' + "https://www.instagram.com/" + i)
except:
    pass

print("\n\n")

print(bcolors.blue + "============================================== Yahoo Search ==============================================")
print(bcolors.blue + "searching on Yahoo")
r = Yahoo_search(domain)
yahoo_emails = []
yahoo_face = []
yahoo_insta = []

try:
    
    Yahoo_emails = Yahoo_search.get_emails(r)
    socila_media = Yahoo_search.get_pages(r)
    
except:
    pass
try:

    if len(Yahoo_search.email_list) == 0:
        print(bcolors.red + "Ops Sorry No Email Found \n")
    elif len(Yahoo_search.email_list) !=0:
        for e in Yahoo_search.email_list:
            if e not in yahoo_emails:
                yahoo_emails.append(e)

    if len(Yahoo_search.instagram) == 0:
        print(bcolors.red + "No Instagram account Found \n")
    elif len(Yahoo_search.instagram) !=0:
        for I in Yahoo_search.instagram:
            if I not in yahoo_insta:
                yahoo_insta.append(I)

    if len(Yahoo_search.facebook) == 0:
        print(bcolors.red + "No Facebook Page Found \n")
    elif len(Yahoo_search.facebook) != 0:
        for F in Yahoo_search.facebook:
            if F not in yahoo_face:
                yahoo_face.append(F)
except:
    pass

try:

    for i in yahoo_emails:
        print(bcolors.orange  + 'This Email Found On Yahoo may related To your Target : '+ i + '\n')

    for i in yahoo_face:
        if i != "tr" and i != "p" and i != "pages":
            print(bcolors.blue +  'This Facebook account Found On Yahoo may related To your Target : ' + "https://www.facebook.com/"+ i + '\n')

    for i in yahoo_insta:
        if i != "tr" and i != "p" and i != "pages":
            print(bcolors.green + 'This Instagram account Found On Yahoo may related To your Target : ' + "https://www.instagram.com/" + i + '\n')
except:
    pass
print("\n\n")

print(bcolors.blue + "============================================== Website Search ==============================================")

pages = ("" , "contact" , 'about' , )

web_emails = []
web_face = []
web_insta = []
print(bcolors.green + 'searching on website ')

for page in  pages :
    
    try:
        r = req_domain(domain , page)
        email = req_domain.Get_emails(r)
        social_media = req_domain.get_pages(r)
    except:
        pass

    if len(req_domain.email_list) == 0:
        print(bcolors.red + "Ops Sorry No Email Found \n")

    elif len(req_domain.email_list) !=0:
        for e in req_domain.email_list:
            if e not in web_emails:
                web_emails.append(e)
    if len(req_domain.instagram) == 0:
        print(bcolors.red + "No Instagram account Found \n")

    elif len(req_domain.instagram) !=0:
        for insta_page in req_domain.instagram:
            if insta_page not in web_insta:
                web_insta.append(insta_page)

    if len(req_domain.facebook) == 0:
        print(bcolors.red + "No Facebook Page Found \n")
    elif len(req_domain.facebook) != 0:
        for face_page in req_domain.facebook:
            if face_page not in web_face:
                web_face.append(face_page)

for i in web_emails:
    if "https" not in i and '@' in i and '.' in i and '/' not in i:
    	print(bcolors.orange  + 'Email Fund On website : '+ i + "\n")

for i in web_face:
    if i != "tr" and i != "p" and i != "pages":
        print(bcolors.blue  + 'Facebook Page Found On website : ' + "https://www.facebook.com/"+ i + "\n")
for i in web_insta:
    if i != "tr" and i != "p" and i != "pages":
        print(bcolors.green  +'Instagram account Found On website : ' + "https://www.instagram.com/" + i + "\n")

print(bcolors.blue +"==============================================***1N1TOne Club***==============================================")
