import re

def password_strength(password):
    length = len(password)>=8 
    uppercase_letter = re.search(r'[A-Z]',password) is not None
    lowercase_letter = re.search(r'[a-z]',password) is not None
    digits = re.search(r'\d',password) is not None
    special_char = re.search(r'[@_!#$%^&*()<>?/\|}{~:]',password) is not None
    

    if all([length,uppercase_letter,lowercase_letter,digits,special_char]):
        print("strength of pasword is strong")
    else:
        print("strength of password is weak")
    return ""    

password = input("enter your password:")
result = password_strength(password)
print(result)
