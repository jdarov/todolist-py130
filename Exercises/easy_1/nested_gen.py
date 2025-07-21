lists = [[1,2,3], [4,5]]

flat_list = list(element for number_list in lists for element in number_list)

print(flat_list)