STELLAR_TYPES = {
    0: 'Main Sequence, M<0.7 Msun',
    1: 'Main Sequence, M>0.7 Msun',
    2: 'Herztsprung Gap',
    3: 'First Giant Branch',
    4: 'Core Helium Burning',
    5: 'Early Asymptotic Giant Branch',
    6: 'Thermally Pulsing Asymptotic Giant Branch',
    7: 'Helium MS',
    8: 'Helium Herztsprung Gap',
    9: 'Helium Giant Branch',
    10: 'Helium White Dwarf',
    11: 'C-O White Dwarf',
    12: 'O-N White Dwarf',
    13: 'Neutron Star',
    14: 'Black Hole',
    15: 'Massless Remnant',
    16: 'Chemically Homogenously Evolving'
}


def is_compact_object(type) -> bool:
    return (type == 13) or (type == 14)


def is_white_dwarf(type) -> bool:
    return (type == 10) or (type == 11) or (type == 12)


def is_main_sequence(type) -> bool:
    return 0 <= type <= 9
