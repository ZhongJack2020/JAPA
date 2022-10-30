import helpers
import japa
import sys
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

digit_names = ["0","1","2","3","4","6","period","9"]
#digit_names = ['0', '1', '2', '3', '4', '6', 'period', '9']
#digit_names = ['left', 'right']

def print_shape(shape):
    x = -1
    for i in range(12):
        row = ''
        for j in range(10):
            x += 1
            if shape[x]:
                row += 'X'
            else:
                row += ' '
        print(row)

affinity_graph = []

for i in range(1):
    affinity_graph += japa.japa(
        antigens             = [helpers.create_antigen(name) for name in digit_names],
        antibodies           = [japa.Antibody() for _ in range(10)],
        generations          = 100,
        num_clone_antibodies = 5,
        num_kill_antibodies  = 1,
        clone_multiplier     = 10
    )

for affinity_rating in affinity_graph:
    affinity_rating['key'] = digit_names[affinity_rating['key']]

with open('output.csv', 'w') as output_csv:
    dict_writer = csv.DictWriter(output_csv, ['generation', 'key', 'affinity'])
    dict_writer.writeheader()
    dict_writer.writerows(affinity_graph)

def AG_plot(path):
    data=pd.read_csv(path)
    dta_keys=sorted(list(set(list(data['key']))))
    n=1
    plt.figure(figsize=(20,10),dpi=200)
    for key in dta_keys:
        dta_access=data[data[data.columns[1]]==key]
        x_axis=np.array(dta_access[data.columns[0]])
        y_axis=np.array(dta_access[data.columns[2]])
        plt.subplot(2,4,n)
        n+=1
        plt.title("digits: '{}.png'".format(key))
        plt.xlabel(data.columns[0])
        plt.ylabel(data.columns[2])
        plt.plot(x_axis,y_axis)
    plt.savefig("./graph.png",facecolor="w")
    plt.show()
    
AG_plot("./output.csv")

sys.exit()
