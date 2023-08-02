import bytereaders
import consts
import gamechecker
import characters
import datetime


class SAV:
    def __init__(self, path):
        self.data = open(path, 'rb').read()
        self.version = gamechecker.gameversionchecker(self.data)
        self.gen = self.get_generation(self.version)
        if self.gen == 4:
            self.current_block = self.get_current_block()
            self.block_offset = consts.sizes[4]['SIZE_2BLOCKS'] * self.current_block
            self.started_date = bytereaders.read32(self.data,
                                                   self.block_offset + consts.offsets[4][self.version]['STARTED_DATE'])
            self.league_date = bytereaders.read32(self.data,
                                                  self.block_offset + consts.offsets[4][self.version]['LEAGUE_DATE'])
            self.player_name = characters.get_player_name(self.data,
                                                          self.block_offset + consts.offsets[4][self.version][
                                                              'TRAINER_NAME'])
            self.gender = bytereaders.read8(self.data,
                                            self.block_offset + consts.offsets[4][self.version]['TRAINER_GENDER'])

    def get_generation(self, version):
        gens = {
            1:
                ['RB', 'G', 'Y'],
            2:
                ['GS', 'C'],
            3:
                ['RS', 'E', 'FRLF'],
            4:
                ['DP', 'Pt', 'HGSS']
        }

        for gen in range(1, 10):
            if version in gens[gen]:
                return gen

    def get_current_block(self):
        if self.gen == 4:
            block1_savecount = bytereaders.read32(self.data, consts.sizes[4]['HGSS']['SIZE_SMALL'] - 16)
            block2_savecount = bytereaders.read32(self.data, consts.sizes[4]['HGSS']['SIZE_SMALL'] + 0x40000 - 16)
            return block1_savecount < block2_savecount

    def __repr__(self):
        return f"This is a {self.gen}" \
               f"{'st' if self.gen == 1 else 'nd' if self.gen == 2 else 'rd' if self.gen == 3 else 'th'} generation " \
               f"{self.version} file of {self.player_name}, who started {'her' if self.gender else 'his'} journey on " \
               f"{datetime.datetime.fromtimestamp(946684800 + self.started_date)}"


savefile = SAV('HG.sav')
print(savefile)