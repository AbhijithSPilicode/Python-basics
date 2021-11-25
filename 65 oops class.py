Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 18:46:30) [MSC v.1929 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#OOPS
class car:
    name=" "
    color=" "
    make=2020
    def details(self):
        print(self.name)
        print(self.color)

        
audi=car()
audi.name
' '
audi.name="audi A8"
audi.name
'audi A8'
audi.color="blue"
audi.color
'blue'

audi.details()
audi A8
blue
bmw=car()
bmw.name="B2"
bmw.color="silver"
bmw.details()
B2
silver
