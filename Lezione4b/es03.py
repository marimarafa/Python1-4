def convert_to_title(col_number :int) -> str:
    """
    Dato un intero col_number ,restituisce il auo corrispondente titolo di colonna come ad esempio compare in un file excel
    """
    result: str = ""
    while col_number > 0:
        resto:int = (col_number -1) % 26 
        result = chr(resto + ord('A')) + result
        col_number = (col_number -1) // 26
    return result
number = convert_to_title(23)
print(number)




    