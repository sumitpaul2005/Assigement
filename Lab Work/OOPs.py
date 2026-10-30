class A:
    def fact(self,n):
        fa = 1
        for i in range(1,n+1):
            fa *= i

        print("Factorial : ",fa)

class B:
    def prime(self,n):
        p = 0
        for i in range(1,n+1):
            if n%i == 0:
                p += 1
        if p == 2:
            print("Prime number")
        else:
            print("Not Prime number")

class C:
    def sorting(self):
        l = list(map(int,input("Enter the number : ").split()))
        s = l.sort()
        print("Sorting : ",s)

class D(C,B,A):
    def inp(self):
        menu = """
            Press 1 : Factorial
            Press 2 : Prime number
            Press 3 : Sorting
            Press 4 : Exit
        """
        c = int(input("Enter your choice : "))
        return c

        

while True:
    o = D()
    c = o.inp()
    if c == 1:
        n = int(input("Enter the value : "))
        o.fact(n)
        
    elif c == 2:
        n = int(input("Enter the value : "))
        o.prime(n)

    elif c == 3:
        o.sorting()
        
    elif c == 4:
        print("Thank you!!!")
        break

    else:
        print("You enter worng ")
        break