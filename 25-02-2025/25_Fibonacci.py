#def fibonacci(term, next_term):
    

term=0
next_term=1
n=0
while n<10:
    print(term)
    t=next_term
    next_term=next_term+term
    term=t
    
    n+=1
