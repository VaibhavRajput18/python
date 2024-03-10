# import re
# pattern   = r'\d'
# text = "HI,This is vaibhav"
# val=re.match(pattern,text)
# print(val)

#=========================================

# import re
# pattern = r'\d'
# text = "Hello 2, 1, 3 World"
# match = re.search(pattern,text)
# if match:
#     print("Found",match.group())
# else:
#     print("Not Found")

#============================================

# import re
# pattern = r'\d'
# text = "Hello 202, 101, 303 World"
# match = re.search(pattern,text)
# print(match)
# if match:
#     print("Found",match.group())
# else:
#     print("Not Found")

#====================================

# import re
# pattern = r'[a-z]+uch'
# text = "lions spend much rions of their time resting. "
# match = re.search(pattern,text)
# print(match)
# if match:
#     print("Found",match.group())
# else:
#     print("Not Found")

#=========================================

# import re
# pattern = r'[A-Z]+ions'
# text = "Lions spend much rions of their Time resting. "
# match = re.findall(pattern,text)
# print(match)

#==========================================

# import re
# pattern = r'[a-zA-z]+ions'
# text = "Lions spend much rions of their time resting. "
# match = re.findall(pattern,text)
# print(match)

#===========================================

# import re
# pattern = r'[a-zA-z0-9]+ions'
# text = "Lions spend much rions of their time resting.123 "
# match = re.findall(pattern,text)
# print(match)

#============================================

# import re
# pattern = r'[A-Za-z]+ions'
# text = "Lions spend much rions of their time resting."
# match = re.findall(pattern,text)
# for i in match:
#     print(i)

#=============================================

#email validation:
# import re
# def valid_email(email):
#    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#    if re.match(pattern, email):
#         return True
#    else:
#         return False
   
# email = str(input("enter your email :"))
# if valid_email(email):
#     print(f"{email} is a valid email address.")
# else:
#     print(f"{email} is not a valid email address.")

#========================================================

#date validation:
# import re

# def is_valid_date(date_str, format='%Y-%m-%d'):
#     date_pattern = r'\d{4}-\d{2}-\d{2}'
#     return bool(re.match(date_pattern, date_str))

# date_to_validate = "2023-10-12"
# if is_valid_date(date_to_validate):
#     print(f"{date_to_validate} is a valid date.")
# else:
#     print(f"{date_to_validate} is not a valid date.")

#===================================================

#access website

# import re, urllib
# import urllib.request
# site = "https://www.rcpit.ac.in/"
# u = urllib.request.urlopen(site)
# text=u.read()
# title = re.findall("<title>.*</title>",str(text),re.I)
# print(title[0])

