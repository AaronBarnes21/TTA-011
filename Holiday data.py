import pandas as pd 

Menu = {"Hotel":["Royal Grand","Muthu Clube Praia Da Oura","Solana Hotel and Spa","Blue Sea",],
        "Prices":[541,611,296,432],
        "Avaliable":['yes','no','yes','yes'],
        "Rating":[4,4,3,3],
        "Most visted city":[1000000,9000000,4500000,5000000]}
        
myframe = pd.DataFrame(Menu)

print(myframe)