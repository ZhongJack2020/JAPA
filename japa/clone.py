# -*- coding: utf-8 -*-


import copy

def clone_antibody(antibody, clone_multiplier, num_antigens, affinity_rank):
    num_clones = int(round(clone_multiplier * num_antigens / float(affinity_rank)))
    
    return [copy.deepcopy(antibody) for i in range(num_clones)]
