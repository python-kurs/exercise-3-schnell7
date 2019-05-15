# Exercise 3
from pathlib import Path
import utils
# import functions from utils here

data_dir = Path("H:\git\exercise-3-schnell7\data")
output_dir = Path("solution")
#%%
# 1. Contstruct the path to the text file in the data directory using the `pathlib` module [2P]
#data_dir = Path("H:\git\exercise-3-schnell7\data")
data_dir = "H:\git\exercise-3-schnell7\data"
#????????????
#%%
# 2. Read the text file [2P]
with open(data_dir +"\cars.txt", "r") as file:
    lines = file.readlines()
    
print(lines)
#%%
# 3. Count the occurences of each item in the text file [2P]
count = utils.count_type()
#%%
# 4. Using `pathlib` check if a directory with name `solution` exists and if not create it [2P]


# 5. Write the counts to the file `counts.csv` in the `solution` directory in the format (first line is the header): [2P]
#    item, count
#    item_name_1, item_count_1
#    item_name_2, item_count_2
#    ...
    
single = list(set(lines))
#%%

with open(data_dir + "\solotions.csv", "w") as file:
    file.write('Type;count\n' )
    if len(res) == len(single):
        for i in range(len(res)):
            #file.write(str(res[i]) + ";" + single[i])
            file.writelines(single[i][:-2] + ";" + str(res[i]) +"\n")