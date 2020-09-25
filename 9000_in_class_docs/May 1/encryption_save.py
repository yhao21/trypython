from cryptography.fernet import Fernet
import pickle
import base64

"""this is the symmetric encrption. one side encrypt, the other side decrypt"""
"""
to be more safe, you should use asymmetric encrypt.
"""



#should be byte type
obj = 'baby shark do do do do'
print('original')
print(obj)

#dumps to make it a obj
serialized_obj = pickle.dumps(obj)
print('serialized')
print(serialized_obj)
"""b'\x80\x04\x95\x1a\x00\x00\x00\x00\x00\x00\x00\x8c\x16baby shark do do do do\x94.'"""



password = b'PasswordPasswordPasswordPassword'
"""
ValueError: Fernet key must be 32 url-safe base64-encoded bytes.
you have to format correctly
"""
##key 1
# key = Fernet.generate_key()
##key 2
key = base64.urlsafe_b64decode(password)

print(key)
"""b'h2b5Rcnb73YXwI0Xvt9GjYj9Ha-s-EFuKZ-T_PF5VLY='"""
f = Fernet(key)
"""
after your friends and you trust this key, then every time you can use this key to encrypt the obj
key = b'h2b5Rcnb73YXwI0Xvt9GjYj9Ha-s-EFuKZ-T_PF5VLY='
f = Fernet(key)
"""



encrypted_object = f.encrypt(serialized_obj)
print('encrypted')
print(encrypted_object)

"""after you encrypted, you have to know the key to decode"""
"""
this is the key
b'h2b5Rcnb73YXwI0Xvt9GjYj9Ha-s-EFuKZ-T_PF5VLY='"""
"""b'gAAAAABerEp2u1Wiwxln7T1hxYLkADVlC2QMwn22p0gn89emp9_WYpqmGTnUEobVI77MUytBaP36AebfTLgD4fsAxK3tKaH-gELwcziseFpeyiXQ13SEpmSREu3IjuaXGqkA8Aq4QSg2'"""
