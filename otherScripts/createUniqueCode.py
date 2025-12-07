import secrets
import string

def createUniqueCode():
    alph = string.ascii_uppercase + string.digits
    mass = []
    for i in range(17):
        mass.append(secrets.choice(alph))
    return "".join(mass)