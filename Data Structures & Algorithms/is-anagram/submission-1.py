class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        conteo = {}
        for letra in s:
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1
        for letras in t:
            if letras in conteo:
                conteo[letras] -= 1
                if conteo[letras] <0:
                    return False
            else:
                return False
        return True