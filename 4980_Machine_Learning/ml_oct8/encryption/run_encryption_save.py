from cryptography.fernet import Fernet
import pickle
import base64


password = b'PasswordPasswordPasswordPassword'
key = base64.urlsafe_b64encode(password)
print(key)
#### key:
#### b'UGFzc3dvcmRQYXNzd29yZFBhc3N3b3JkUGFzc3dvcmQ='
f = Fernet(key)

'serialized obj first, then encrypt it'

original_obj = 'This is a secret message!!'

serialized_obj = pickle.dumps(original_obj)


### f contain a key, we encrypt the key, rather the obj directly.
encrypted_obj = f.encrypt(serialized_obj)


print(encrypted_obj)
##b'gAAAAABfxo2NFxPAHEftlQ507NzByYLMyNXexmOIkQCTb4uTIqIEvwyJIWc9s0DQF_N9sXMRNql8p-
##gE7EbsngOHeLLm_uSxXWPFHweaOY4lCy4xLYgAaeCR9yTSVNyN_W62diAs4DTh'




