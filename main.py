import bytereaders
import consts
import gamechecker


class SAV:
    def __init__(self, path):
        self.data = open(path, 'rb').read()
        self.version = gamechecker.gameversionchecker(self.data)
        self.current_block = self.get_current_block()
        self.block_offset = consts.sizes[4]['SIZE_2BLOCKS'] * self.current_block
        self.started_date = bytereaders.read32(self.data, self.block_offset + consts.offsets[4]['HGSS']['STARTED_DATE'])


    def get_current_block(self):
        if self.version == 'HGSS':
            block1_time = bytereaders.read16(self.data, consts.offsets[4]['HGSS']['TRAINER_PLAYTIME']) * 3600 + \
                          bytereaders.read8(self.data, consts.offsets[4]['HGSS']['TRAINER_PLAYTIME'] + 2) * 60 + \
                          bytereaders.read8(self.data, consts.offsets[4]['HGSS']['TRAINER_PLAYTIME'] + 4)
            block2_time = bytereaders.read16(self.data, consts.sizes[4]['SIZE_2BLOCKS'] +
                                             consts.offsets[4]['HGSS']['TRAINER_PLAYTIME']) * 3600 + \
                          bytereaders.read8(self.data, consts.sizes[4]['SIZE_2BLOCKS'] +
                                            consts.offsets[4]['HGSS']['TRAINER_PLAYTIME'] + 2) * 60 + \
                          bytereaders.read8(self.data, consts.sizes[4]['SIZE_2BLOCKS'] +
                                            consts.offsets[4]['HGSS']['TRAINER_PLAYTIME'] + 4)
            if block1_time > block2_time:
                self.playtime = block1_time
                return 0
            self.playtime = block2_time
            return 1


print(SAV('HG.sav').started_date)
