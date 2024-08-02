username=input("Enter username:")
password=input("Enter password:")

pass_len=len(password)
stars="*" * pass_len

print(f"{username}, your password {stars} is {pass_len} letters long ")