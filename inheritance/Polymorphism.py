class One:
    def Do_it(self):
        print("Do_it from One")
        
        
    def Doanything(self):
        self.Do_it()
            
class Two(One):
    def Do_it(self):
        print("Do_it from Two")
        
one = One()
two = Two()
one.Doanything()
two.Doanything()