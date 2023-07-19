import numpy as np
import simpy as sp
import copy

def change_tensor(lista):
    for i in range(len(lista)):
        if type(lista[i])==list:
            change_tensor(lista[i])

        else:
            lista[i]=sp.sympify(input('Choose a component (in order): '))

def build_tensor(rank, nb_per_level, fill=0):
    '''
    Temporary copya+paste for the tensor generation
    '''
    l=[fill for i in range(nb_per_level)]
    for i in range(rank):
        l=[copy.deepcopy(l) for j in range(nb_per_level)]

    return l

class Tensor:

    def __init__(self, struct, lista=[], coords=sp.symbols('t x y z')):
        '''
       The user has to provide the structure of the tensor in the form of a list o 0s and 1s, 0 indicates a lower index and 1 indicates an upper index, indicating only the amount of coordinates of the tensor and the index structure. Optionally, they can pass a list of lists in a form suitable to the structure provided, which will be verified to make sure it matches the structure provided. 
        '''

        self.struct=struct #list of 0s and 1s
        self.rank=len(struct)

        if lista!=[]:
            self.lista=lista
            #test if the list corresponds to the structure given
            
        if lista==[]: 
            print("Pass the components of your tensor:")
            self.lista=build_tensor(self.rank, 4)
            change_tensor(self.list)

        #The tensor creation is crappy but works. Fix later:
        #The user manually chooses non-zero components > manually choosing all components
        #Use something other than deepcopy for the initial tensor creation
