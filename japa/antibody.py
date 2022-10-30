# -*- coding: utf-8 -*-

import random


class Antibody:
    def __init__(self, shape = None):
        if shape:
            self.shape = shape
        else:
            self.shape = [random.random() >= .5 for s in range(120)]

        self.affinity = 0
        self.memfinity = 0
