def evens(limiter = 10):
    n = 0
    while True:
        n+=2
        if n > limiter:
            return
        yield n

def odds():
    n = 1
    while True:
        n+=2
        yield n        
    
for i in evens():
    print(i)
        