#import re and pyperclip
import re, pyperclip

#create a RegX for Phone Numbers
myPhoneNumber = re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d)')  #setting thr number pattern

#Create a RegEX for Email Addresses
myEmail = re.compile(r'[a-zA-Z0-9_.+]+@[a-zA-Z0-9_.+]+')

#Get the Texts off the clipboard
texts = pyperclip.paste()

#Extract Email/Phone number from the texts
ExtractedPhoneNumbers = myPhoneNumber.findall(texts)
ExtractedEmails = myEmail.findall(texts)

print(ExtractedPhoneNumbers)
print(ExtractedEmails)