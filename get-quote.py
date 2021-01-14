import random

def primary():
    #print("Keep it logically awesome.")

    lastQ = 13
    
    rand = random.randint(0,lastQ)

    f = open("quotes.txt")
    quotes = f.readlines()
    f.close()

    print(quotes[rand])

if __name__== "__main__":
    primary()
