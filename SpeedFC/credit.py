# Autor : Gabriel Tadeo
# Luhn algorithm reference: https://en.wikipedia.org/wiki/Luhn_algorithm


class Luhn:
    def __init__(self):
        self.creditCard = ""
    
    # Note: Input will be entirely numeric
    def readCard(self):
        self.creditCard = input("Number: ")
    
    # Luhn algorithm
    def isValid(self):
        counter = 0
        size = len(self.creditCard)
        one_two = 0

        creditCard = self.creditCard[::-1]
        for i in range(0, size):

            c = ord(creditCard[i]) - ord('0')
            c = c * ( one_two + 1)
            c =  c // 10  + c % 10
            counter += c
            one_two = (one_two + 1) % 2

        #print(counter, end = ' ')
        
        if counter % 10 == 0:
            return True
        else:
            return False
    
    # Get card mame
    def isValidCard(self):

        # AMEX or MASTERCARD or VISA
        if self.isValid():
            
            if(len(self.creditCard) < 2):
                return 
            

            if len(self.creditCard) == 15 and self.creditCard[0:2] in ("34", "37"):
                return "AMEX"
            elif len(self.creditCard) == 16 and self.creditCard[0:2] in ("51","52","53","54","55"):
                return "MASTERCARD"
            elif len(self.creditCard) in (13,16)  and self.creditCard[0] == '4':
                return "VISA"
            else:
                return
        else:
            return "INVALID"




# Main 
obj = Luhn()
obj.readCard()
print(obj.isValidCard())

#### Note: None output represents that the creditCard is valid but doesn`t below to VISA, AMEX or MASTERCARD
