import re
from requests_html import HTMLSession
#TODO: Rethink of a better wayt to search the phone number !
#TODO: Also might be a good idea to looking into the email as well 

# phone_regex = re.compile(r'''(
#     (\d{3}|\(\d{3}\))?      # area code
#     (\s|-|\.)?              # separator
#     (\d{3})                 # first three digits 
#     (\s|-|\.)               # separator
#     (\d{4})                 # last for digits 
#     (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
#     )''', re.VERBOSE)
phone_regex = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4})',re.VERBOSE)#|\d{3}[-\.\s]??\d{4})',re.VERBOSE)
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name 
    (\.[a-zA-Z]{2,4})       # dot-somthing  
    )''', re.VERBOSE)

def scraper(link):
    session = HTMLSession()
    web_html = session.get(link) #user inputed site 
    web_html.html.render()


    web_text = web_html.text
    matches = []
    for groups in phone_regex.findall(web_text):
        # phone_num = '-'.join([groups[1],groups[3],groups[5]])
        # if groups[8] != '':
            # phone_num += ' x' + groups[8]
        matches.append(groups)
    for groups in email_regex.findall(web_text):
        matches.append(groups[0])
    return matches

print(scraper('https://www.indeed.com/jobs?q&l=Nashua%2C%20NH&vjk=bc14adcabbeb16e9'))