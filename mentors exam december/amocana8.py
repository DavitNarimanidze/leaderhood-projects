def smallest_element(arr, k):
    arr.sort() # ვალაგებთ arr-ს ზრდადობით 

    return arr[k - 1] # k-1 ინდექსზე მდებარეობს k-ე უმცირესი ელემენტი

print(smallest_element(arr = [3, 2, 1, 5, 6, 4], k = 2))
print(smallest_element(arr = [3, 2, 1, 5, 6, 4], k = 4))
print(smallest_element(arr = [7, 10, 4, 3, 20, 15], k = 3))
