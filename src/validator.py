class Validator(object):

    def __init__(self):
        self.isValid = False
    
    def validate(self, number):
        try:
            if number is None:
                return self.isValid
            if isinstance(number, str) and number.find(' ') >= 0:
                number = number.replace(' ', '')
            self.isValid =  number.isdigit() and len(number) == 13
            if self.isValid:
                index = 1
                evens = ""
                numArray = list(number)
                total = 0
                while index < 13:
                    if index % 2 == 0:
                        evens = evens + numArray[index - 1]
                    else:
                        total = total + int(numArray[index - 1])
                    index = index + 1
                evenTotalArrSum = sum(int(val) for val in list(str(int(evens) * 2)))
                evenOdd = total + evenTotalArrSum
                self.isValid = int(numArray[12]) == 10 - int(list(str(evenOdd))[1])
                
            return self.isValid
        except Exception:
            self.isValid = False
            return self.isValid
