import re


# FILESYSTEM OK -/ used space (9%) inode (3%) | fs=9% inode=3%
def string_parser(txt: str) -> str:
    space_regex = 'space\s?\((?P<space>\d+\%)\)\s?'
    inode_regex = 'inode\s?\((?P<inode>\d+\%)\)\s?'
    fs_regex = '\|\s?fs=(?P<fs>\d+\%)'

    regex = re.compile(f'{space_regex}{inode_regex}{fs_regex}')
    match = regex.search(txt)

    if match is None:
        return None

    result = {
        'space': match.group('space'),
        'inode': match.group('inode'),
        'fs': match.group('fs')
    }

    return result
