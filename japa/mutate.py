# -*- coding: utf-8 -*-


import random

def mutate_antibody(antibody, affinity_rank):
    num_mutations = min(affinity_rank, len(antibody.shape)) # mutations number = affinity rank
    #TODO: improve the mutations strategy
    mutation_keys = random.sample(range(len(antibody.shape)), num_mutations)
    for key in mutation_keys:
        antibody.shape[key] = not antibody.shape[key]
    
    return antibody
