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

def scraper(link):
    session = HTMLSession()
    web_html = session.get(link)
    web_text = web_html.text

    phone_matches = phone_regex.findall(web_text)
     
    # removing all the the blank items
    new_phone_matches = []
    for found_phones in phone_matches:
        for phone in found_phones:
            if len(phone) < 11:
                del phone
            else:
                new_phone_matches.append(phone)
  
    email_matches = email_regex.findall(web_text)
    new_email_matches = []
    for found_emails in email_matches:
        for email in found_emails:
            if len(email) >= 6:
                new_email_matches.append(email)
            else:
                del email

    # removes duplicates  
    new_email_matches = list(dict.fromkeys(new_email_matches))
    new_phone_matches = list(dict.fromkeys(new_phone_matches))
    return new_phone_matches, new_email_matches