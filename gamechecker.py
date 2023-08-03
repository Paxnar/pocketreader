import consts
import bytereaders
import errors


def CRC16_CCITT(data):
    top = 0xFF
    bot = 0xFF
    for b in data:
        x = b ^ top
        x ^= (x >> 4)
        top = (bot ^ (x >> 3) ^ (x << 4)) & 0xFF
        bot = (x ^ (x << 5)) & 0xFF
    return (top << 8) | bot


def isgen4sav(data):
    if len(data) != consts.sizes[4]['SIZE_RAW']:
        return False

    def validSequence(data, offset: int):
        size = bytereaders.read32(data, offset + consts.sizes[4]['SIZE_2BLOCKS'] - 0xC)
        # print(size)
        if size != offset:
            return False
        sdk = bytereaders.read32(data, offset - 0x8)
        DATE_INT = 0x20060623
        DATE_KO = 0x20070903
        return sdk == DATE_INT or sdk == DATE_KO

    if validSequence(data, consts.sizes[4]['DP']['SIZE_SMALL']):
        return "DP"
    if validSequence(data, consts.sizes[4]['Pt']['SIZE_SMALL']):
        return "Pt"
    if validSequence(data, consts.sizes[4]['HGSS']['SIZE_SMALL']):
        return 'HGSS'

    return False


def isgen5sav(data):
    if len(data) != consts.sizes[5]['SIZE_RAW']:
        return False

    def validFooter(data, block_size: int, length):
        footer = data[block_size - 0x100: block_size - 0x100 + length + 0x10]
        stored = bytereaders.read16(footer[-2:])
        actual = CRC16_CCITT(footer[:length])
        return stored == actual

    if validFooter(data, consts.sizes[5]['BW']['SIZE_2BLOCKS'], 0x8C):
        return "BW"
    if validFooter(data, consts.sizes[5]['B2W2']['SIZE_2BLOCKS'], 0x94):
        return "B2W2"

    return False


def gameversionchecker(data):
    if ret := isgen4sav(data):
        return ret
    if ret := isgen5sav(data):
        return ret
    raise errors.IdkWhatVersionException
