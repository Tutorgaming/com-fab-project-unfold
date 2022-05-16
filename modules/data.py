#!/usr/bin/env python3
############################################################
# Data Structure                                           #
############################################################

#################################
# Face Data                     #
#################################
class Face(object):
    """
    Face Represent Triangle inside the mesh
    """
    def __init__(self):
        self.sides = []
        self.next = []
        self.next_edge = []
        self.coplanar = []
        self.used = False
