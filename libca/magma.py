# --------------------------------------------------
# MIT License
# Copyright (c) 2025 Maks Osipenko
# --------------------------------------------------


import secrets
from .alpha import RU32, NODE

def unwrapp(key:str)->list[bytes]:
    sub_keys = list()
    bytes32 = bytes.fromhex(key)
    for index in range(0, len(bytes32), 4):
        sub_key = bytes32[index:index+4]
        sub_keys.append(sub_key)
    return sub_keys*3+sub_keys[::-1]

def fill8(block:bytes)->bytes:
    padding = bytearray()
    for _ in range(8-len(block)):
        padding.append(secrets.randbelow(256))
    return bytes(bytearray(block)+padding)

def split8(text:str)->list[bytes]:
    blocks = list()
    bytes = text.encode("utf-8")
    for index in range(0, len(bytes), 8):
        block = bytes[index:index+8]
        blocks.append(fill8(block))
    return blocks

def apply_box(bit4:int, box_index:int)->int: return NODE[box_index][bit4]

def distribut(sum4:bytes)->bytes:
    bytes4 = bytearray()
    for index in range(len(sum4)):
        byte = sum4[index]
        high_nibble = byte >> 4
        low_nibble = byte & 0x0F
        new_high_nibble = apply_box(high_nibble, index*2)
        new_low_nibble = apply_box(low_nibble, index*2+1)
        new_byte = (new_high_nibble << 4) | new_low_nibble
        bytes4.append(new_byte)
    return bytes(bytes4)

def func(block4:bytes, iter_key:bytes)->bytes:
    block4_int = int.from_bytes(block4, byteorder="big")
    iter_key_int = int.from_bytes(iter_key, byteorder="big")
    sum4 = ((block4_int+iter_key_int)%(2**32)).to_bytes(4, byteorder="big")
    dis_int = int.from_bytes(distribut(sum4), byteorder="big")
    shift = ((dis_int << 11) | (dis_int >> (32-11))) & 0xFFFFFFFF
    return shift.to_bytes(4, byteorder="big")

def XOR(lb:bytes, rb:bytes)->bytes: return bytes([l^r for l, r in zip(lb, rb)])

def magma(text:str, key:str)->str:
    ciphertext = bytearray()
    iter_keys = unwrapp(key)
    blocks = split8(text)
    for block in blocks:
        l_block, r_block = block[:4], block[4:]
        for index in range(31):
            _block = r_block
            r_block = XOR(l_block, func(r_block, iter_keys[index]))
            l_block = _block
        ciphertext.extend(XOR(l_block, func(r_block, iter_keys[31]))+r_block)
    return bytes(ciphertext).hex()