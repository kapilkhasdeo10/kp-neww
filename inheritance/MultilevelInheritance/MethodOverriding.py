class Level1:
    var = 100
    def fun(self):
        return 101
    
class Level2:
    var = 200
    def fun(self):
        return 201
    
class Level1(Level2):
    pass

obj = Level1()
print(obj.var, obj.fun())