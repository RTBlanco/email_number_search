import re
from requests_html import HTMLSession


phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      # area code
    (\s|-|\.)?              # separator
    (\d{3})                 # first three digits 
    (\s|-|\.)               # separator
    (\d{4})                 # last for digits 
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # extension
    )''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # domain name 
    (\.[a-zA-Z]{2,4})       # dot-somthing  
    )''', re.VERBOSE)


session = HTMLSession()
web_html = session.get('https://www.transparent.com/')
web_html.html.render()


web_text = 'ronnytoribio1@hotmail.com ronnytoribio2@outlook.com rtblanco66@gmail.com ' #web_html.text
matches = []
for groups in phone_regex.findall(web_text):
    phone_num = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(web_text):
    matches.append(groups[0])

