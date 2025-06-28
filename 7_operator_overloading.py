class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        return self.n + num.n      #Even though you can rename self to anything, by Python convention, we usually use:self for the left-hand object other or something like num for the right-hand object

x = Number(10)
y = Number(20)  


print(x+y)