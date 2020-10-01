import re

mailIds='''It contains several email Ids such as marks@gmail.com <john@xyz.com;> you<>i@search.com postman@home.edu 12233.kdhffh@23893.cdjc.in <location@localhost>; sp,e of them are correct and some of them are invalid lets find out using regEx'''

#Get all email Addresses 
allEmails=re.findall('\S+@\S+',mailIds)
print(allEmails)


#Get only correct email address 
correctFormatEmails = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]',mailIds)
print(correctOnlyEmails)
