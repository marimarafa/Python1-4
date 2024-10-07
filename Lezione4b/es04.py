def majority_element(nums : list[int]) -> int:
    """
    Data una lista di nums di n elementi,restituire l'elemento che 
    compare più di n/2 volte
    """
    
    for n in nums:
        if nums.count(n) > len(nums)/2 :
            return n 
        else:
            return None
        
lista = majority_element([4,3,3,4,4])
print(lista)


