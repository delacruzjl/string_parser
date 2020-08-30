import re
# FILESYSTEM OK -/ used space (9%) inode (3%) | fs=9% inode=3%
def string_parser(txt: str) -> str:
    regex = 'space\s?\((?P<space>\d+\%)\)\s?inode\s?\((?P<inode>\d+\%)\)\s?\|\s?fs=(?P<fs>\d+\%)'
    match = re.search(regex, txt)

    if match is None:
        return None

    result = {
        'space': match.group('space'),
        'inode': match.group('inode'),
        'fs': match.group('fs')
    }

    return result


