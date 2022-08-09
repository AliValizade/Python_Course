class Fraction:
    def __init__(self, s, m):
        self.soorat = s
        self.makhraj = m

    def sum(self, guest):
        result = Fraction(None, None)
        result.soorat = self.soorat * guest.makhraj + self.makhraj * guest.soorat
        result.makhraj = self.makhraj * guest.makhraj
        return result
    def sub(self, guest):
        result = Fraction(None, None)
        result.soorat = self.soorat * guest.makhraj - self.makhraj * guest.soorat
        result.makhraj = self.makhraj * guest.makhraj
        return result
    def multiply(self, guest):
        result = Fraction(None, None)
        result.soorat = self.soorat * guest.soorat
        result.makhraj = self.makhraj * guest.makhraj
        return result
    def division(self, guest):
        result = Fraction(None, None)
        result.soorat = self.soorat * guest.makhraj
        result.makhraj = self.makhraj * guest.soorat
        return result
    def show_fraction(self):
        print(self.soorat, '/', self.makhraj)

f1 = Fraction(3, 5)
print('f1 = ', end=' ')
f1.show_fraction()
f2 = Fraction(5, 7)
print('f2 = ', end=' ')
f2.show_fraction()
sum_f = f1.sum(f2)
print('Sum of fraction: ', end=' ')
sum_f.show_fraction()
sub_f = f1.sub(f2)
print('Sub of fraction: ', end=' ')
sub_f.show_fraction()
mul_f = f1.multiply(f2)
print('Multiply of fraction: ', end=' ')
mul_f.show_fraction()
div_f = f1.division(f2)
print('Division of fraction: ', end=' ')
div_f.show_fraction()



        
