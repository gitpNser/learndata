import pandas as pd

musicdata = [("The rolling stones","Satisfication"),("Beatles","Let it be"),("Guns N Roses","Don't Cry"),("Metallica","Nothing Else Matters")]

frame = pd.DataFrame(musicdata, index=range(1,5), columns=['singer','Song_name'])

print(frame)