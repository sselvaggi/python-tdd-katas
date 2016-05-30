class RomanNumberHelper:

    def __init__(self):
        self.symbols = [['I','V'],['X','L'],['C','D'],['M','?']]
        self.digits = range(0,9)

    def symbol_by_digit_and_exp(self, digit, exp):
        #validate  0 < digit < 10
        if(digit == 1):
            return self.symbols[exp][0]
        elif(digit == 2):
            return self.symbols[exp][0]+self.symbols[exp][0]
        elif(digit == 3):
            return self.symbols[exp][0]+self.symbols[exp][0]+self.symbols[exp][0]
        elif(digit == 4):
            return self.symbols[exp][0]+self.symbols[exp][1]
        elif(digit == 5):
            return self.symbols[exp][1]
        elif(digit == 6):
            return self.symbols[exp][1]+self.symbols[exp][0]
        elif(digit == 7):
            return self.symbols[exp][1]+self.symbols[exp][0]+self.symbols[exp][0]
        elif(digit == 8):
            return self.symbols[exp][1]+self.symbols[exp][0]+self.symbols[exp][0]+self.symbols[exp][0]
        elif(digit == 9):
            return self.symbols[exp][0]+self.symbols[exp+1][0]
    def to_roman(self, integer):
        result = ''
        for exp in range(self.get_max_decimal_exponent(integer),0):
            digit = self.get_digit_by_exp(integer,exp)
            result += self.symbol_by_digit_and_exp(digit,exp)
        return result 
    
    def get_max_decimal_exponent(self, integer):
        exp = 0
        while((10**exp) < integer):
            exp+=1
        return exp

    # integer=1  exp=0 return 1
    # integer=2  exp=0 return 2
    # integer=10 exp=0 return 0
    # integer=10 exp=1 return 1
    # integer=20 exp=1 return 2
    # integer=10 exp=2 return 0
    def get_digit_by_exp(self, integer,exp):
        digit = 0
        max_exp = self.get_max_decimal_exponent(integer)
        mod = integer % (10**(exp+1))
        for i in range(0, 10):
            if (i*(10**exp) <= mod):
                digit = i
        return digit