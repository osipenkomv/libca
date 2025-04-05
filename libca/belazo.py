# --------------------------------------------------
# MIT License
# Copyright (c) 2025 Maks Osipenko
# --------------------------------------------------


from .alpha import RU32

def periodic(key:str, target_length:int)->str:
    return key*(target_length//len(key))+key[:target_length-target_length//len(key)]

def belazo(text:str, key:str)->str:
    ciphertext = str()
    for letter, symbol in zip(text, periodic(key, len(text))):
        ciphertext += RU32[(RU32.index(letter)+RU32.index(symbol))%32]
    return ciphertext

def un_belazo(ciphertext:str, key:str)->str:
    text = str()
    for letter, symbol in zip(ciphertext, periodic(key, len(ciphertext))):
        text += RU32[(RU32.index(letter)-RU32.index(symbol))%32]
    return text