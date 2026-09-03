from typing import List

def get_last_three_elements(my_list: List[int]) -> List[int]:
    lenght = len(my_list)
    if lenght == 3:
        return my_list
    else:
        new_l = lenght - 3
        new_list = my_list[new_l:]
        return new_list
# do not modify below this line
print(get_last_three_elements([1, 2, 3]))
print(get_last_three_elements([1, 2, 3, 4, 5]))
print(get_last_three_elements([1, 2, 3, 4, 5, 6, 7, 8, 9]))
