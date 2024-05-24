import hashlib

og_key = "yzbqklnj"
num = 1
while True: #creating a loop
    key = og_key + str(num)
    #make into hash
    keya = key.encode()
    keyb = hashlib.md5(keya)
    keyc = keyb.hexdigest()
    #verify
    if keyc.startswith("00000"):
        print(num)
        break
    else:
        num += 1