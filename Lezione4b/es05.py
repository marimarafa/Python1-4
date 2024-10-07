def move_zeroes(nums: list[int]):
    """
    Data una lista d' interi, spostare gli seri alla fine della lista mantenendo l'ordine originale dei numeri che non sono zeri
    """
    for n in nums:
        if n == 0:
            nums.remove(n)
            nums.append(n)
    return nums
    
lista = move_zeroes([1,2,3,0,8,0,5,0,34])
print(lista)

