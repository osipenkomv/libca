# --------------------------------------------------
# MIT License
# Copyright (c) 2025 Maks Osipenko
# --------------------------------------------------


from .alpha import RU32

def polybius(text:str)->list[tuple[int, int]]:
    ciphertext = list()
    for letter in text:
        designation = (RU32.index(letter)//6+1, RU32.index(letter)%6+1)
        ciphertext.append(designation)
    return ciphertext
