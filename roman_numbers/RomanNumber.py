class RomanNumberHelper:

    def __init__(self):
        self.symbols = [['I','V'],['X','L'],['C','D'],['M','?']]
        self.digits = range(0,9)

    def to_roman(self, integer):
        result = ''
        exp = 0
        digit = 0
        while (10**exp <= integer):
            digit = integer % (10**(exp+1))
            integer -= digit
            if(digit == 1 * (10**exp)):
                result = self.symbols[exp][0] + result
            elif(digit == 2 * (10**exp)):
                result = self.symbols[exp][0]+self.symbols[exp][0] + result
            elif(digit == 3 * (10**exp)):
                result = self.symbols[exp][0]+self.symbols[exp][0]+self.symbols[exp][0] + result
            elif(digit == 4 * (10**exp)):
                result = self.symbols[exp][0]+self.symbols[exp][1] + result
            elif(digit == 5 * (10**exp)):
                result = self.symbols[exp][1] + result
            elif(digit == 6 * (10**exp)):
                result = self.symbols[exp][1]+self.symbols[exp][0] + result
            elif(digit == 7 * (10**exp)):
                result = self.symbols[exp][1]+self.symbols[exp][0]+self.symbols[exp][0] + result
            elif(digit == 8 * (10**exp)):
                result = self.symbols[exp][1]+self.symbols[exp][0]+self.symbols[exp][0]+self.symbols[exp][0] + result
            elif(digit == 9 * (10**exp)):
                result = self.symbols[exp][0]+self.symbols[exp+1][0] + result
            exp = exp+1
        return result