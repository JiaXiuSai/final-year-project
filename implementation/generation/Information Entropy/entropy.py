# https://github.com/oeschsec/pwmsecurity-usenix2020

import math 

class EntropyCalculator:

    def shannon_entropy(self,data):
        stack = {}

        # calculate probability of each character
        for character in data:
            stack[character] = round(data.count(character) / len(data), 5)
        return self.entropy(stack)

    def entropy_with_freq(self,stack):
        bit_set = [round(prob * math.log2(prob), 5) for prob in stack]
        entropy = -1 * (round(sum(bit_set), 5))
        return entropy

    #Log2(#possible combinations) - naive approach
    def password_entropy(self,passwordlength,charspacesize):
        # pwdlength * LogBase2(size of character space)
        return round(passwordlength*math.log2(charspacesize),5)

    # stack = list of symbols with associated frequency
    def entropy(self,symbol_set):
        bit_set = [round(symbol_set[symbol] * math.log2(symbol_set[symbol]), 5) for symbol in symbol_set]
        entropy = -1 * (round(sum(bit_set), 5))
        return entropy

# code to calculate entropy values with no repeats