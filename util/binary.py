
def get_bit(int_type, offset):
    return (int_type & (1 << offset)) >> offset


def set_bit(int_type, offset, value):
    if value:
        return int_type | (1 << offset)
    else:
        return int_type & ~(1 << offset)
