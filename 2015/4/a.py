import hashlib
start = "yzbqklnj"
for i in range(0,10000000000):
    result = hashlib.md5((start+str(i)).encode()).hexdigest()
    if result[0:6] == "000000":
        print(i)