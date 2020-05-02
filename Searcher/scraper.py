import re
from requests_html import HTMLSession

class Scraper:
    def __init__(self, link):
        self.link = link
        session = HTMLSession()
        self.web_text = session.get(self.link).text

    def numbers(self):
        """ Returns a group of Phone numbers found """
        phone_regex = re.compile(r'''((\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})(\s*(ext|x|ext.)\s*(\d{2,5}))?)''', re.VERBOSE)
        phone_matches = phone_regex.findall(self.web_text)

        new_phone_matches = []
        for found_phones in phone_matches:
            for phone in found_phones:
                if len(phone) < 11:
                    del phone
                else:
                    new_phone_matches.append(phone)
        new_phone_matches = list(dict.fromkeys(new_phone_matches))
        return new_phone_matches

    def emails(self):
        """ Returns a group of emails found """
        email_regex = re.compile(r'''([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''', re.VERBOSE)
        email_matches = email_regex.findall(self.web_text)

        new_email_matches = []
        for found_emails in email_matches:
            for email in found_emails:
                if len(email) >= 6:
                    new_email_matches.append(email)
                else:
                    del email
        new_email_matches = list(dict.fromkeys(new_email_matches))
        return new_email_matches