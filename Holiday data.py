import pandas as pd

Menu = {"Hotel":["Pala Beach Club Apartmentos","Rimondi Grand Resort & Spa Hotel","Globales Costa Tropical","King Evelthon Beach Hotel & Resort"],
        "Ratings":[1,5,3,4],
        "Nights":[5,7,3,4],
        "Price":[128,521,422,425],}

myframe=pd.DataFrame(Menu)

print(myframe)