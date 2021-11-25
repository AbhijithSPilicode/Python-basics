x=100 #global
def test():
    y=200 #enclosed
    print(y)
    if True:
        y=2000
        z=300 #local
        print(z)
        print(y)
test()

#
x=12
def test():
    x=1
    print(x) #it will print enclosed 1
    def t():
        x=100  #localvariable
        print(x) #it will print local variable 100
    t()
    
    print(x) #itwillprintlocalvariable1
test()    
print(x) #itwillprintglobalvariable12
