def ipok(ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte)>255:
            return False
    return True
