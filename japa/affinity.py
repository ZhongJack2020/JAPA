# -*- coding: utf-8 -*-

"""
kapa.affinity

Calculates the similarity of an antibody to antigen using the hamming distance

"""

def calculate_affinity(antigen, antibody):
    affinity = 0
    for i in range(len(antigen.shape)):
        if antigen.shape[i] == antibody.shape[i]:
            affinity += 1
    affinity = round(affinity/len(antigen.shape),3)
    # print("antibody{},antigen%{},affinity:{}".format(antibody,antigen,affinity))
    return affinity
