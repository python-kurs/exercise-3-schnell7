#linux
import utils

with open("./data/cars.txt", "r") as file:
    lines = file.readlines()

count = utils.count_type(lines)
single = list(set(lines))

with open("./solutions/count2.csv", "w") as file:
    file.write('Type;count\n' )
    if len(count) == len(single):
        for i in range(len(count)):
            #file.write(str(res[i]) + ";" + single[i])
            file.writelines(single[i][:-2] + ";" + str(count[i]) +"\n")
