from cryptography.fernet import Fernet
import pickle
import base64

##key 1
# key = b'h2b5Rcnb73YXwI0Xvt9GjYj9Ha-s-EFuKZ-T_PF5VLY='

##key 2
password = b'password'
key = base64.urlsafe_b64decode(password)
f = Fernet(key)

encrypted_obj = b'gAAAAABerErIWd11sdD9X4E9-QNWewpC--LQNMVRQAx_279zWBudW2miq5LOUl49F7ut6rB9Xiw86v0mujZz7vupqSaVs58dc2mfS6hCL5kWLLkrl9v8eg2QJIVAOvbFNJm_DUB2QUeW'

decrypted_obj = f.decrypt(encrypted_obj)
print(decrypted_obj)
"""b'\x80\x04\x95\x1a\x00\x00\x00\x00\x00\x00\x00\x8c\x16baby shark do do do do\x94.'"""

deserialized_obj = pickle.loads(decrypted_obj)
print(deserialized_obj)
"""baby shark do do do do"""

"""
zoom n*n 加密其实是假的，zoom先读取你的信息然后再加密，再发送
"""