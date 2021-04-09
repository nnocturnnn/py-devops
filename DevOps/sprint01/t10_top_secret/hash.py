from hashlib import md5,sha1


def md5_hash(string):
    print("Original string: "+ string)
    print("md5 hash generated is")
    print(md5(string.encode('utf-8')).hexdigest())

def sha1_hash(string):
    print("Original string: "+ string)
    print("sha1 hash generated is")
    print(sha1(string.encode('utf-8')).hexdigest())
