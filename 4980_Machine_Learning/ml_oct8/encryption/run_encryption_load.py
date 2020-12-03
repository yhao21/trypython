from cryptography.fernet import Fernet
import pickle
import base64





password = b'PasswordPasswordPasswordPassword'
key = base64.urlsafe_b64encode(password)
f = Fernet(key)


encrypted_obj = b'gAAAAABfxo2NFxPAHEftlQ507NzByYLMyNXexmOIkQCTb4uTIqIEvwyJIWc9s0DQF_N9sXMRNql8p-gE7EbsngOHeLLm_uSxXWPFHweaOY4lCy4xLYgAaeCR9yTSVNyN_W62diAs4DTh'

decrypted_obj = f.decrypt(encrypted_obj)
print(decrypted_obj)
### b'\x80\x04\x95\x1e\x00\x00\x00\x00\x00\x00\x00\x8c\x1aThis is a secret message!!\x94.'

deserialized_obj = pickle.loads(decrypted_obj)
print(deserialized_obj)
### This is a secret message!!
