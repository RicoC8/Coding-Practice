def search(searchElement, array):
    found = False
    i = 0
    while not found and i <= len(array) - 1:
        if searchElement == array[i]:
            print(f"Element {searchElement} was found at index {i}")
            found = True
        i += 1
            
    if not found:
        print("Element does not exist within this array")

#DECLARE list: ARRAY[0:8] OF INTEGER
list = [1,2,3,4,5,6,7,8,9]

search(2,list)
search(25,list)