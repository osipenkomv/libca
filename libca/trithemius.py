# --------------------------------------------------
# MIT License
# Copyright (c) 2025 Maks Osipenko
# --------------------------------------------------


from .alpha import RU32

def trithemius(text:str)->str:
    ciphertext = str()
    for index in range(len(text)):
        ciphertext += RU32[(RU32.index(text[index])+index+1)%32]
    return ciphertext

def un_trithemius(ciphertext:str)->str:
    text = str()
    for index in range(len(ciphertext)):
        text += RU32[(RU32.index(ciphertext[index])-index-1)%32]
    return text