# Algoritmo selection sort tomado directamente del libro y aplicado a la
# organizacion de un array de enteros de forma ascendente.

# Encuentra el indice del elemento mas pequeño en un array:
def find_smallest(arr):
	smallest = arr[0]
	smallest_idx = 0
	
	for idx in range(1, len(arr)):
		if arr[idx] < smallest:
			smallest = arr[idx]
			smallest_idx = idx
			
	return smallest_idx
	
def selection_sort(arr):
	new_arr = []
	for rep in range(len(arr)):
		# Encontrar el elemento mas pequeño y luego disminuir el tamaño
		# del array:
		smallest_idx = find_smallest(arr)
		new_arr.append(arr.pop(smallest_idx))
	
	return new_arr
	
if __name__ == '__main__':
	print(selection_sort([5, 3, 6, 2, 10]))
