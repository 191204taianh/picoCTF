import string

cipher = "268 413 438 313 426 337 272 188 392 338 77 332 139 113 92 239 247 120 419 72 295 190 131"

message = ""

mapping = " " + string.ascii_lowercase + string.digits + "_"

for el in cipher.split(" "):
    modinv = pow(int(el), -1, 41)
    message += mapping[modinv]

print(message)
# 1nv3r53ly_h4rd_dadaacaa