import re
import sololearn

def validate_email():
    options = ("com|edu|net")
    pattern = f"[a-zA-Z0-9]+@[a-zA-Z]+\.({options})"
    user_input = input("please enter your email: ")
    if re.search(pattern, user_input):
        print("valid!!")
    else:
        print("invalid")


def validate_phone_number(phone_number):
    area_code = "\(?\d{3}\)?[-.]?" #3 didgits, possibly encapsulated in "()" and ending with a "." or "-"
    pattern = area_code + "\d{3}[-.]\d{4}"
    if re.match(pattern, phone_number):
        print("valid phone number")
    else:
        print("invalid number")

# validate_phone_number("917-555-1234")
# validate_phone_number("646.555.1234")
# validate_phone_number("(212)-867-5509")
# validate_phone_number("(212)867-5509")
sololearn.concatenate("I","love", "Python", "!")