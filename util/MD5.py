import hashlib
def md5(key):

    input_name = hashlib.md5()

    input_name.update(key.encode("utf-8"))

    print(key,"  ---->  ",input_name.hexdigest())

    return input_name.hexdigest()