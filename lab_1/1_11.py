"""Напишите генератор frange как аналог range() с дробным шагом."""
def frange(xx,y,z):
    while xx<=y:
        yield round(xx, 1)
        #one += step
        xx+=z
       # print(xx)
        #return(xx)
        
    


#frange(1,5,0.1)
for x in frange(1,5,0.1):
    print(x, end="   ")

