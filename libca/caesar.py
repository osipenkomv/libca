# --------------------------------------------------
# MIT License
# Copyright (c) 2025 Maks Osipenko
# --------------------------------------------------


from .alpha import RU32

def caesar(text:str, key:int)->str:
    ciphertext = str()
    for letter in text:
        ciphertext += RU32[(RU32.index(letter)+key)%32]
    return ciphertext