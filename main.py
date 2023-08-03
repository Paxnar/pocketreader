import bytereaders
import consts
import gamechecker
import characters
import datetime
import enums


class PKM:
    def __init__(self, data, offset, gen, version, party=False):
        self.data = data
        self.offset = offset
        self.gen = gen
        self.version = version
        self.party = party
        if self.gen in [4, 5]:
            self.pkm_raw = list(self.data[offset:offset + ((236 if self.gen == 4 else 220) if self.party else 136)])

            self.pkm_unenc = self.pkm_raw[:0x8]
            self.PID = bytereaders.read32(self.pkm_unenc, 0)
            self.checksum = bytereaders.read16(self.pkm_unenc, 0x6)

            self.pkm_enc = self.pkm_raw[0x8:0x88]
            self.shuffled_blocks = self.shuffle()
            self.decrypt_enc()

            self.ID = bytereaders.read16(self.pkm_enc, 0x8 - 8 + self.shuffled_blocks[0])
            self.species = enums.pkm[self.ID]
            self.trainer_id = bytereaders.read16(self.pkm_enc, 0xC - 8 + self.shuffled_blocks[0])
            self.trainer_sid = bytereaders.read16(self.pkm_enc, 0xE - 8 + self.shuffled_blocks[0])
            self.trainer_name = characters.get_player_name(self.pkm_enc,
                                                           0x68 - 8 - 96 + self.shuffled_blocks[3], self.gen)
            self.exp = bytereaders.read16(self.pkm_enc, 0x10 - 8 + self.shuffled_blocks[0])
            self.friendship = bytereaders.read8(self.pkm_enc, 0x14 - 8 + self.shuffled_blocks[0])
            self.ability = enums.abilities[bytereaders.read8(self.pkm_enc,
                                                             0x15 - 8 + self.shuffled_blocks[0])].capitalize()
            self.language = enums.languages[bytereaders.read8(self.pkm_enc,
                                                              0x17 - 8 + self.shuffled_blocks[0])]
            self.EVs = {
                ['HP', 'Attack', 'Defense', 'Speed', 'Sp. Attack', 'Sp. Defense'][i]:
                    bytereaders.read8(self.pkm_enc,
                                      0x18 - 8 + i + self.shuffled_blocks[0]) for i in range(6)}

            self.pkm_batl = self.pkm_raw[0x88:]

    def shuffle(self):
        if self.gen in [4, 5]:
            orderTable = {
                # A offset -> index 0; B offset -> index 1; C offset -> index 2; D offset -> index 3
                0: [0, 32, 64, 96],  # ABCD
                1: [0, 32, 96, 64],  # ABDC
                2: [0, 64, 32, 96],  # ACBD
                3: [0, 96, 32, 64],  # ACDB
                4: [0, 64, 96, 32],  # ADBC
                5: [0, 96, 64, 32],  # ADCB
                6: [32, 0, 64, 96],  # BACD
                7: [32, 0, 96, 64],  # BADC
                8: [64, 0, 32, 96],  # BCAD
                9: [96, 0, 32, 64],  # BCDA
                10: [64, 0, 96, 32],  # BDAC
                11: [96, 0, 64, 32],  # BDCA
                12: [32, 64, 0, 96],  # CABD
                13: [32, 96, 0, 64],  # CADB
                14: [64, 32, 0, 96],  # CBAD
                15: [96, 32, 0, 64],  # CBDA
                16: [64, 96, 0, 32],  # CDAB
                17: [96, 64, 0, 32],  # CDBA
                18: [32, 64, 96, 0],  # DABC
                19: [32, 96, 64, 0],  # DACB
                20: [64, 32, 96, 0],  # DBAC
                21: [96, 32, 64, 0],  # DBCA
                22: [64, 96, 64, 0],  # DCAB
                23: [96, 64, 32, 0]  # DCBA
            }

            return orderTable[((self.PID & 0x3e000) >> 0xd) % 24]

    def decrypt_enc(self):
        if self.gen in [4, 5]:
            seed = self.checksum
            for i in range(0, 128, 2):
                seed = (0x41C64E6D * seed) + 0x00006073
                self.pkm_enc[i] ^= (seed >> 16) & 0xff
                self.pkm_enc[i + 1] ^= (seed >> 24) & 0xff

    def __repr__(self):
        return f'PID: {hex(self.PID)[2:]}, Species: {self.species} ({self.ID}), Trainer: {self.trainer_name} ' \
               f'({self.trainer_id}, {self.trainer_sid}) EVs: {"".join([f"{i}: {self.EVs[i]}, " for i in self.EVs])}'


class SAV:
    def __init__(self, path):
        self.file_name = path
        self.data = open(path, 'rb').read()
        self.version = gamechecker.gameversionchecker(self.data)
        self.gen = self.get_generation(self.version)
        self.consts_offsets = consts.offsets[self.gen][self.version]
        if self.gen == 4:
            self.current_block = self.get_current_block()
            self.block_offset = consts.sizes[4]['SIZE_2BLOCKS'] * self.current_block
            self.started_date = bytereaders.read32(self.data,
                                                   self.block_offset + self.consts_offsets['STARTED_DATE'])
            self.league_date = bytereaders.read32(self.data,
                                                  self.block_offset + self.consts_offsets['LEAGUE_DATE'])
            self.player_name = characters.get_player_name(self.data,
                                                          self.block_offset + self.consts_offsets['TRAINER_NAME'],
                                                          self.gen)
            self.gender = bytereaders.read8(self.data,
                                            self.block_offset + self.consts_offsets['TRAINER_GENDER'])
            self.player_id = bytereaders.read16(self.data,
                                                self.block_offset + self.consts_offsets['TRAINER_ID'])
            self.player_sid = bytereaders.read16(self.data,
                                                 self.block_offset + self.consts_offsets['TRAINER_SID'])
            self.party_size = bytereaders.read32(self.data,
                                                 self.block_offset + self.consts_offsets['PARTY_COUNT'])
            self.party_pokemon = [PKM(self.data,
                                      self.block_offset + self.consts_offsets['PARTY'] + 236 * i,
                                      4, self.version, True) for i in range(self.party_size)]
        if self.gen == 5:
            self.started_date = bytereaders.read32(self.data,
                                                   self.consts_offsets['STARTED_DATE'])
            self.league_date = bytereaders.read32(self.data,
                                                  self.consts_offsets['LEAGUE_DATE'])
            self.player_name = characters.get_player_name(self.data,
                                                          self.consts_offsets['TRAINER_NAME'],
                                                          self.gen)
            self.gender = bytereaders.read8(self.data,
                                            self.consts_offsets['TRAINER_GENDER'])
            self.player_id = bytereaders.read16(self.data,
                                                self.consts_offsets['TRAINER_ID'])
            self.player_sid = bytereaders.read16(self.data,
                                                 self.consts_offsets['TRAINER_SID'])
            self.party_size = bytereaders.read32(self.data,
                                                 self.consts_offsets['PARTY_COUNT'])
            self.party_pokemon = [PKM(self.data,
                                      self.consts_offsets['PARTY'] + consts.sizes[5]['SIZE_PARTY_POKEMON'] * i,
                                      5, self.version, True) for i in range(self.party_size)]

    def get_generation(self, version):
        gens = {
            1:
                ['RB', 'G', 'Y'],
            2:
                ['GS', 'C'],
            3:
                ['RS', 'E', 'FRLF'],
            4:
                ['DP', 'Pt', 'HGSS'],
            5:
                ['BW', 'B2W2']
        }

        for gen in range(1, 10):
            if version in gens[gen]:
                return gen

    def get_current_block(self):
        if self.gen == 4:
            block1_savecount = bytereaders.read32(self.data, consts.sizes[4][self.version]['SIZE_SMALL'] - 16)
            block2_savecount = bytereaders.read32(self.data, consts.sizes[4][self.version]['SIZE_SMALL'] + 0x40000 - 16)
            return block1_savecount < block2_savecount

    def __repr__(self):
        nl = '\n'
        return f"{self.file_name}: This is a {self.gen}" \
               f"{'st' if self.gen == 1 else 'nd' if self.gen == 2 else 'rd' if self.gen == 3 else 'th'} generation " \
               f"{self.version} file of {self.player_name}, who started {'her' if self.gender else 'his'} journey on " \
               f"{datetime.datetime.fromtimestamp(946674000 + self.started_date)}\n" \
               f"{self.player_name}'s trainer ID is {self.player_id} and {'her' if self.gender else 'his'} SID " \
               f"is {self.player_sid}\n" \
               f"{self.player_name} has {self.party_size} pokemon in {'her' if self.gender else 'his'} party, them " \
               f"being:\n" \
            f"{nl.join([str(i + 1) + ' '+ self.party_pokemon[i].__repr__() for i in range(len(self.party_pokemon))])}"


savefile = SAV('white.sav')
print(savefile)
