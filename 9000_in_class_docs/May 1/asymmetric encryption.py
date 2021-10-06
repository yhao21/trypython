"""
when you encrypt the content, you use public key,

Tom send something to yujie

yujie generate private and public key,
Yujie, give public key to Tom, tom encrypt the machine with public key, and send back to Yujie
then, Yujie use private key to decrypt the machine.

by using asymmetric encrypt, the program will generate two key, private key and public key
private key is much longer. and public key is part of the private key.




asymmetric work very slow when encrypt byte type data.
so,
use symmetric to encrypt the machine,
then you use the asymmetric method to encrypt the key of the machine.



if you have a nice machine and you want to sell to others,
you use asymmetric encryption , each of one copy of product(machine) have a unique code. that is encrypted.




you need RSA private key and public key
"""
"""
so, when you want to encrypt a machine and send to others,
you use symmetric encryption to encrypt the machine, while it will also generate a key.

and then, you use asymmetric encryption to encrypt the key.


doing so because asymmetric encryption run every slow with byte type. if your machine file is too large,
it will take you to much time to finish the encryption work. 


"""