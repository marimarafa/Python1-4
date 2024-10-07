def intersection(nums1:set, nums2:set) -> list[int]:
    lista_inter = list()
    for e1 in nums1:
            if e1 in nums2 :
                lista_inter.append(e1)
                #lista_inter = list(lista_inter)
    return lista_inter

lista1 = intersection([2,4,5,6,3,5,2],[3,2,4,1,2,4,5])

print(lista1)
   

    
            