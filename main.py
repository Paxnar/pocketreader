from bytereaders import read8, read16, read32
import consts


def readfile(path: str):
    return open(path, 'rb').read()


def isgen4sav(data):
    if len(data) != consts.SIZE_G4_RAW:
        return False

    def validSequence(data, offset: int):
        size = read32(data[offset + consts.SIZE_G4_2BLOCKS - 0xC:])
        # print(size)
        if size != offset:
            return False
        sdk = read32(data[offset - 0x8:])
        DATE_INT = 0x20060623
        DATE_KO = 0x20070903
        return sdk == DATE_INT or sdk == DATE_KO

    if validSequence(data, consts.SIZE_G4_SMALL_DP):
        return "DP"
    if validSequence(data, consts.SIZE_G4_SMALL_Pt):
        return "Pt"
    if validSequence(data, consts.SIZE_G4_SMALL_HGSS):
        return 'HGSS'

    return False


file = readfile('HG.sav')
print(isgen4sav(file))

