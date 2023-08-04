import numpy as np
import sympy as sp
import copy

def change_tensor(arr, inds, layer):
    '''
    This function enters the term arr[ins[0]][inds[1]]... and changes it to the term desired by the user.
    '''
    if type(arr[inds[layer]])==list:
        arr[inds[layer]]=change_tensor(arr[inds[layer]], inds, layer+1)

    else:
        term=sp.sympify(input('\nChoose a number or function for the term {}: '.format(inds)))
        arr[inds[layer]]=term

    return arr

def build_tensor(rank, nb_per_level, fill=0):
    '''
    Temporary copya+paste for the tensor generation
    '''
    l=[fill for i in range(nb_per_level)]
    for i in range(rank):
        l=[copy.deepcopy(l) for j in range(nb_per_level)]

    return l

class Tensor:

    def __init__(self, struct, non_zeros, arr=[], metric=None, coords=sp.symbols('t x y z')):
        '''
       The user has to provide the structure of the tensor in the form of a list o 0s and 1s, 0 indicates a lower index and 1 indicates an upper index, indicating only the amount of coordinates of the tensor and the index structure. Optionally, they can pass a list of lists in a form suitable to the structure provided, which will be verified to make sure it matches the structure provided. 
       There's kind of a but in the creation of the "arr", if the intended tensor is a vector, the list non_zeros needs to have the format [[i],[j], ...], it would be ideal if the used could pass (for instance) [i,j,...] also. 
        '''

        self.struct=struct #list of 0s and 1s
        self.rank=len(struct)
        self.metric=metric
        self.coords=coords

        if arr!=[]:
            self.arr=arr
            #test if the list corresponds to the structure given
            #if it doesn't, set the list to list=[], so the next condition works
            #pass an exception error if the format doesn't correspond to the given structure
            
        if arr==[]: 
            arr=build_tensor(self.rank-1, 4)
            print("arr=", arr, '\n')
            print("Pass the non-zero components of your tensor:\n")
            for inds in non_zeros:
                self.arr=change_tensor(arr, inds, 0)

        #Extensively test the tensor creation to see if it works as intended
        #Use something other than deepcopy for the initial tensor creation
        self.arr=np.array(self.arr)

    def __eq__(T1, T2):
        if T1.struct==T2.struct and np.array_equal(T1.arr,T2.arr) and T1.coords==T2.coords: #How to verify if the metric is equal?
            return True
        else:
            return False

    def __add__(self, T):
        npself=np.array(self.arr)
        npT=np.array(T.arr)

        if self.struct==T.struct and self.coords==T.coords: #verify if metric is the same
            arr_sum=npT+npself
            list_sum=arr_sum.tolist()
            return Tensor(self.struct, [], arr=list_sum, metric=self.metric, coords=self.coords) 

        else:
            raise Exception("Tensors are somehow incompatible!")
            return None

    def __mul__(self, k):
        #if k is a number, product with scalar; if k is another tensor -> too much work for now
        if type(k)==float or type(k)==int:
            arr_prod=k*self.arr
            list_prod=arr_prod.tolist()
            return Tensor(self.struct, [], arr=list_prod, metric=self.metric, coords=self.coords) 
        else:
            print("Tensor contraction not yet implemented")
            #contraction
            return None

    def __rmul__(self,k):
        return self.__mul__(k)

    def __str__(self):
        return str(self.arr)

    def __repr__(self):
        return str(self.arr)

g_mink=Tensor([0,0], [], [[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], metric=[])

if __name__=="__main__":
    '''
    This is a testing area, every bit of code written here will only be run if you directly run the tensor.py code.
    '''
    

