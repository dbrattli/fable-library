def fromBits(lowBits: int, highBits: int, unsigned: bool):
    return lowBits + (highBits << 32)