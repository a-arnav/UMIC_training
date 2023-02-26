class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        if float(self.b) >= 0:
            print(f'{self.a}+{self.b}i')
        else:
            print(f'{self.a}{self.b}i')
    def add(self,complex2):
        return complex(int(self.a)+int(complex2.a),int(self.b)+int(complex2.b))
    def subs(self,complex2):
        return complex(int(self.a)-int(complex2.a),int(self.b)-int(complex2.b))
    def conjugate(self):
        return complex(int(self.a),-int(self.b))
    def modulus(self):
        a=(int(self.a)*int(self.a)+int(self.b)*int(self.b))**0.5
        return a
    def multi(self,complex2):
        return complex(int(self.a)*int(complex2.a)-int(self.b)*int(complex2.b),int(self.b)*int(complex2.a)+int(self.a)*int(complex2.b))
    def inverse(self):
        return complex(int(self.a)/self.modulus(),-1*int(self.b)/self.modulus())
a,b,c,d=input('Input the Complexes(a+ib)(c+id): ').split()
a1=complex(a,b)
a2=complex(c,d)
a1.display()
a2.display()
#a1.add(a2).display()
#a1.subs(a2).display()
#a1.conjugate().display()
#print('%.2f'% a1.modulus())
#a1.multi(a2).display()
#a1.inverse().display()
while True:
    a=input('Select the operation(+,-,*,conj,inv,exit): ')
    if a=='+':
        a1.add(a2).display()
    elif a=='-':
        a1.subs(a2).display()
    elif a=='*':
        a1.multi(a2).display()
    elif a=='conj':
        b=input('First(1) or Second(2): ')
        if b=='1':
            a1.conjugate().display()
        elif b=='2':
            a2.conjugate().display()
        else:
            print('Wrong INPUT')
    elif a=='inv':
        a1.inverse().display()
    elif a=='exit':
        print('-----------BREAK-----------')
        break
    else:
        print('Invalid Input!!')