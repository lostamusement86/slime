
# ######################################################################### #
# Integer operations, such as base conversion, are represented here.        #
# ######################################################################### #

def change_base_16(i, base):
    """
    This will take a string i that represents an integer of base 'base' and
    converts it to a hexadevimal string.

    | :param str i: The integer to convert
    | :param int base: The base of the integer to convert
    | :return:
    """
    return str(hex(int(i, base))).split('x')[-1]