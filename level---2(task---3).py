def check_password(password):
    length = len(password)
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else:
            has_special = True

    
    if length < 6:
        print("Weak password ")
    elif has_upper and has_lower and has_digit and has_special:
        print("Strong password ")
    else:
        print("Medium password ")

pwd = input("Enter your password: ")
check_password(pwd)