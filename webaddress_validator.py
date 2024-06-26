# I am creating a simple web validator program
# This module is meant to introduce the re (python regex module)
import re

def web_address_validator(web_address:str) -> bool:
    pattern = re.compile("^[w]{3}.[^#@.*%&!]+.[a-zA-Z]{3}$")
    if pattern.search(web_address) != None:
        return True
    else:
        return False

def main() -> None:
    address = 'www.google.com'
    while address != '.q':
        address = input("Enter address to check, .q to QUIT: ")
        if address == '.q':
            break
        if web_address_validator(address):
            print(f'ACCESS GRANTED!')
        else:
           print(f'ACCESS DENIED!')

# ---------------------------
if __name__=='__main__':
    main()

