import numpy as np
import sympy as sp
import copy

def change_tensor(lista, inds, layer):
    '''
    This function enters the term lista[ins[0]][inds[1]]... and changes it to the term desired by the user.
    '''
    if type(lista[inds[layer]])==list:
        lista[inds[layer]]=change_tensor(lista[inds[layer]], inds, layer+1)

    else:
        term=sp.sympify(input('\nChoose a number or function for the term {}: '.format(inds)))
        lista[inds[layer]]=term

    return lista

def build_tensor(rank, nb_per_level, fill=0):
    '''
    Temporary copya+paste for the tensor generation
    '''
    l=[fill for i in range(nb_per_level)]
    for i in range(rank):
        l=[copy.deepcopy(l) for j in range(nb_per_level)]

    return l

class Tensor:

    def __init__(self, struct, non_zeros, lista=[], metric=None, coords=sp.symbols('t x y z')):
        '''
       The user has to provide the structure of the tensor in the form of a list o 0s and 1s, 0 indicates a lower index and 1 indicates an upper index, indicating only the amount of coordinates of the tensor and the index structure. Optionally, they can pass a list of lists in a form suitable to the structure provided, which will be verified to make sure it matches the structure provided. 
       There's kind of a but in the creation of the "lista", if the intended tensor is a vector, the list non_zeros needs to have the format [[i],[j], ...], it would be ideal if the used could pass (for instance) [i,j,...] also. 
        '''

        self.struct=struct #list of 0s and 1s
        self.rank=len(struct)
        self.metric=metric
        self.coords=coords

        if lista!=[]:
            self.lista=lista
            #test if the list corresponds to the structure given
            #if it doesn't, set the list to list=[], so the next condition works
            #pass an exception error if the format doesn't correspond to the given structure
            
        if lista==[]: 
            lista=build_tensor(self.rank-1, 4)
            print("lista=", lista, '\n')
            print("Pass the non-zero components of your tensor:\n")
            for inds in non_zeros:
                self.lista=change_tensor(lista, inds, 0)

        #Extensively test the tensor creation to see if it works as intended
        #Use something other than deepcopy for the initial tensor creation
        self.lista=np.array(self.lista)

        def __eq__(T1, T2):
            if T1.struct==T2.struct:
                #Not working in any way whatsoever
                return True
            else:
                return False

        def __add__(self, T):
            #check if the structure is compatible, then add with numpy
            
            return None

        def __prod__(self, k):
            #if k is a number, product with scalar; if k is another tensor -> too much work for now
            if type(k)==float or type(k)==int:
                #prod por escalar
                return None
            else:
                #contração
                return None

g_mink=Tensor([0,0], [], [[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], metric=[])

if __name__=="__main__":
    '''
    This is a testing area, every bit of code written here will only be run if you directly run the tensor.py code.
    '''
    

