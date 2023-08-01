def readlittleendian(data: list, amount: int = 1):
    byteslist = data[:amount]
    ret = 0
    for i in range(amount):
        ret += byteslist[i] << 8 * i
    return ret


def read8(data: list):
    return readlittleendian(data)


def read16(data: list):
    return readlittleendian(data, 2)


def read32(data: list):
    return readlittleendian(data, 4)
