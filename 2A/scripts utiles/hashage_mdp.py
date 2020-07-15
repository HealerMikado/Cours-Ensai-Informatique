import uuid
import hashlib
 
def hash_password(password, idep):
    # uuid is used to generate a random number
    salt = idep
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest()
    
print(hash_password("mon_super_password", "remi"))