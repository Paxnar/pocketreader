import consts
import bytereaders
import errors


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


def gameversionchecker(data):
    if ret := isgen4sav(data):
        return ret
    raise errors.IdkWhatVersionException
