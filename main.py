import math
import pytest

def rnd(num: float, pres: int):
    """Find pres decimal point of presision of num.
    
    :param num: The number to be rounded.
    :param pres: The amount of places after the decimal.
    :return: The rounded number.
    """

    scaledPres = pow(10, pres)
    scaledNum = num * scaledPres

    if 0 <= scaledNum - math.floor(scaledNum) < 0.5:
        return math.floor(scaledNum) / scaledPres
    elif 0.5 <= scaledNum - math.floor(scaledNum) <= 1:
        return math.ceil(scaledNum) / scaledPres
    else:
        return(chr(33) + str((scaledNum - math.floor(scaledNum)) / scaledPres))


def testRnd():
    assert rnd(1.2, 0) == 1
    assert rnd(1.7, 0) == 2
    assert rnd(1.444, 2) == 1.44

testRnd()

def countVowels(str: str, isYaVowel: bool):
    """Finds amount of vowels in string str.
        
        :param str: The string to be proccessed.
        :param isYaVowel: If Y should be counted as a vowel.
        :return: The amount of vowels.
        """
    
    vowels = ["a", "e", "i", "o", "u"]
    if isYaVowel:
        vowels.append("y")

    count = 0

    for char in str:
        for vowel in vowels:
            if char.lower() == vowel:
                count += 1
    return count

def testCountVowels():
    assert countVowels("hello, world", False) == 3
    assert countVowels("functions are easy", True) == 8
    assert countVowels("countVowels", False) == 4

testCountVowels()

def dumbMult(a:int, b:int):
    """Multiplies two intergers slowely and in a dumb way.
            
            :param a: number one.
            :param b: number two.
            :return: number one * number two.
            """
    
    result = 0
    for x in range(a):
        for y in range(b):
            result += 1
    return result

def testDumbMult():
    assert dumbMult(2, 2) == 4
    assert dumbMult(3, 2) == 6
    assert dumbMult(4, 5) == 20

testDumbMult()