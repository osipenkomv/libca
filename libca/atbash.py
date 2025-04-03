# --------------------------------------------------
# MIT License
# Copyright (c) 2025 Maks Osipenko
# --------------------------------------------------


from .alpha import RU32

def atbash(text:str)->str:
    ciphertext = str()
    for letter in text:
        ciphertext += RU32[31-RU32.index(letter)]
    return ciphertext
