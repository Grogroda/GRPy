import numpy as np
import simpy as sp

class Tensor:

    def __init__(self, struct, lista=[]):
        '''
       The user has to provide the structure of the tensor in the form of a list o 0s and 1s, 0 indicates a lower index and 1 indicates an upper index, indicating only the amount of coordinates of the tensor and the index structure. Optionally, they can pass a list of lists in a form suitable to the structure provided, which will be verified to make sure it matches the structure provided. 
        '''

        self.struct=struct

        if lista!=[]:
            self.lista=lista
            #test if the list corresponds to the structure given
            
        if lista==[]: 
            #write a process for the user to fill a list following the structure given
