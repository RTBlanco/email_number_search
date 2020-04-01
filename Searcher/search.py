import re
from requests_html import HTMLSession
#TODO: Rethink of a better wayt to search the phone number !
#TODO: Also might be a good idea to looking into the email as well 

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
    # letting the Javascript render first 
    web_html.html.render()
    web_text = web_html.text

    phone_matches = phone_regex.findall(web_text)
    #TODO: Try a list comprehension 
    # removing all the the blank lists
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

    return new_phone_matches, new_email_matches

phone, email = scraper('https://www.transparent.com')

for number in phone:
    print(number)
for mail in email:
    print(mail)