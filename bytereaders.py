def readlittleendian(data, offset, amount: int = 1):
    byteslist = data[offset:amount + offset]
    ret = 0
    for i in range(amount):
        ret += byteslist[i] << 8 * i
    return ret


def read8(data, offset=0):
    return readlittleendian(data, offset)


def read16(data, offset=0):
    return readlittleendian(data, offset, 2)


def read32(data, offset=0):
    return readlittleendian(data, offset, 4)
