def validate_email(email):
    if "@" not in email:
        return "Invalid Email: '@' symbol missing"
    parts = email.split("@")

    if len(parts) != 2:
        return "Invalid Email: Incorrect format"

    username, domain = parts

    if username == "" or domain == "":
        return "Invalid Email: Username or domain missing"

    if "." not in domain:
        return "Invalid Email: Domain name missing"

    return "Valid Email Address"


email_input = input("Enter your email address: ")
result = validate_email(email_input)
print(result)