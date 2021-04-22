import sys

class Prime_number:
    prime_number_list = []

    def __init__(self):
        self.number_candidate = 2

    def generate(self,r):
        self.range = r

        for i in range(2, self.range):
            self.judge(i)

    def judge(self,nc):
        self.number_candidate = nc

        if (self.number_candidate == 1) or (self.number_candidate == 0):
            return

        for j in range(2, self.number_candidate):
            if self.number_candidate % j == 0:
                return

        self.prime_number_list.append(self.number_candidate)

    def judge_re(self,nc):
        self.number_candidate = nc

        if self.number_candidate == (1 or 0):
            print("no")
            return

        for j in range(2, self.number_candidate):
            if self.number_candidate % j == 0:
                print("no")
                return

        print("yes")

    def print_list(self):
        print(self.prime_number_list)

class Mode_select:
    def __init__(self):
        self.pn = Prime_number()
        print("1:prime number generate")
        print("2:prime number judge")


    def slect(self):
        while True:
            
            s = input("Select mode...")
            self.mode(s)

            
    def mode(self,s):
        if s == "1":
            r = int(input("Number range up to  "))
            self.pn.generate(r)
            self.pn.print_list()
        elif s == "2":
            n = int(input("Is this prime number? "))
            self.pn.judge_re(n)
        elif s == "q":
            sys.exit()
        else:
            return

        
ms = Mode_select()
ms.slect()
