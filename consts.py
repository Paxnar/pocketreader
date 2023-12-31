sizes = {4:
    {
        'SIZE_RAW': 0x80000,
        'SIZE_2BLOCKS': 0x40000,
        'SIZE_PARTY_POKEMON': 0xEC,
        'SIZE_POKEMON': 0x88,
        'DP':
            {
                'SIZE_SMALL': 0xC100,
                'SIZE_BIG': 0x121E0
            },
        'Pt':
            {
                'SIZE_SMALL': 0xCF2C,
                'SIZE_BIG': 0x121E4
            },
        'HGSS':
            {
                'SIZE_SMALL': 0xF628,
                'SIZE_BIG': 0x12310
            },
    },
    5: {
        'SIZE_RAW': 0x80000,
        'SIZE_PARTY_POKEMON': 0xDC,
        'SIZE_POKEMON': 0x88,
        'BW': {
            'SIZE_2BLOCKS': 0x24000,
        },
        'B2W2': {
            'SIZE_2BLOCKS': 0x26000,
        }
    }
}

offsets = {4:
    {
        'HGSS':
        {
            'STARTED_DATE': 0x34,
            'LEAGUE_DATE': 0x3C,
            'TRAINER_NAME': 0x64,
            'TRAINER_ID': 0x74,
            'TRAINER_SID': 0x76,
            'TRAINER_MONEY': 0x78,
            'TRAINER_GENDER': 0x7C,
            'TRAINER_LANGUAGE': 0x7D,
            'TRAINER_JOHTO_BADGES': 0x7E,
            'TRAINER_AVATAR': 0x7F,
            'TRAINER_KANTO_BADGES': 0x83,
            'TRAINER_PLAYTIME': 0x86,
            'PARTY_COUNT': 0x94,
            'PARTY': 0x98,

            'BOX': 0xF700,
            'BOX_NAMES': 0x21708,
            'BOX_WALLPAPERS': 0x219D8
        },
    },
    5:
    {
        'BW':
        {
            'STARTED_DATE': 0x1D934,
            'LEAGUE_DATE': 0x1D93C,
            'TRAINER_NAME': 0x19404,
            'TRAINER_ID': 0x19414,
            'TRAINER_SID': 0x19416,
            'TRAINER_MONEY': 0x21200,
            'TRAINER_GENDER': 0x19421,
            'TRAINER_LANGUAGE': 0x1941E,
            'TRAINER_JOHTO_BADGES': 0x7E,
            'TRAINER_AVATAR': 0x7F,
            'TRAINER_KANTO_BADGES': 0x83,
            'TRAINER_PLAYTIME': 0x86,
            'PARTY_COUNT': 0x18E04,
            'PARTY': 0x18E08,

            'BOX': 0xF700,
            'BOX_NAMES': 0x21708,
            'BOX_WALLPAPERS': 0x219D8
        },
    }
}
