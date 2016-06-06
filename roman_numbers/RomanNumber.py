class RomanNumberHelper:

    def __init__(self):
        self.symbols = [['I','V'],['X','L'],['C','D'],['M','?']]
        self.digits = range(0,9)

    def get_roman_char_by_digit(self,digit,exp):
        if(digit == 1 * (10**exp)):
            return self.symbols[exp][0]
        elif(digit == 2 * (10**exp)):
            return self.symbols[exp][0]+self.symbols[exp][0]
        elif(digit == 3 * (10**exp)):
            return self.symbols[exp][0]+self.symbols[exp][0]+self.symbols[exp][0]
        elif(digit == 4 * (10**exp)):
            return self.symbols[exp][0]+self.symbols[exp][1]
        elif(digit == 5 * (10**exp)):
            return self.symbols[exp][1]
        elif(digit == 6 * (10**exp)):
            return self.symbols[exp][1]+self.symbols[exp][0]
        elif(digit == 7 * (10**exp)):
            return self.symbols[exp][1]+self.symbols[exp][0]+self.symbols[exp][0]
        elif(digit == 8 * (10**exp)):
            return self.symbols[exp][1]+self.symbols[exp][0]+self.symbols[exp][0]+self.symbols[exp][0]
        elif(digit == 9 * (10**exp)):
            return self.symbols[exp][0]+self.symbols[exp+1][0]
        else:
            return ''

    def to_roman(self, integer):
        result = ''
        exp = 0
        digit = 0
        while (10**exp <= integer):
            digit = integer % (10**(exp+1))
            result = self.get_roman_char_by_digit(digit, exp) + result
            integer -= digit
            
            exp = exp+1
        return result