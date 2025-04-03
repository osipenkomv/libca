# --------------------------------------------------
# MIT License
# Copyright (c) 2025 Maks Osipenko
# --------------------------------------------------


from .alpha import RU32

def vigenere(text:str, key:str)->str:
    ciphertext = str()
    for letter, symbol in zip(text, key+text[:-1]):
        ciphertext += RU32[(RU32.index(letter)+RU32.index(symbol))%32]
    return ciphertext