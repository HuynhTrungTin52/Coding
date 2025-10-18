import hashlib

secret_key = "only_server_knows"
def get_signature(data):
    return hashlib.sha256((data+secret_key).encode()).hexdigest()

def unsign(message):
    print(message)
    data,signature =message.split(".")
    if signature != get_signature(data):
        return False
    else:
        return True

def sign(data):
    signature = get_signature(data)
    return data+"."+signature
 


 
data="joe mama"
signed_data=sign(data)
tampered_data=signed_data.replace("mama","dada")
print(tampered_data)

print(unsign(tampered_data))