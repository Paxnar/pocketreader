class IdkWhatVersionException(Exception):
    def __str__(self):
        return 'This savefile has no version that I implemented or it\'s not a proper savefile'
