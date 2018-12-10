# This is an implementation of a binary search
# lst       -> a list of elements ordered
# item      -> an element to search
# returns   -> an index in lst if item is found, None if not.
def binary_search(lst, item):
    # Auxiliary variables to compute the middle index:
    low_idx = 0
    high_idx = len(lst) - 1
    
    # low == high when checking the last possibility:
    while low_idx <= high_idx:
        # Compute the middle element.
        # In the book the author uses the following formula for
        # finding the middle index:
        # mid = (high_idx + low_idx) / 2
        # At the article titled:
        # " Extra, Extra - Read All About It: Nearly All Binary
        # Searches and Mergesorts are Broken" by the author Joshua
        # Bloch, and probably a lot of other sources it's advised to
        # not use the formula above to find the middle index. Instead
        # it is advisable to use:
        # mid = low_idx + ((high_idx - low_idx) / 2)
        # for finding the middle index. Exactly what is argued to happen
        # is that the formula fails for large values of the variables
        # low_idx and hight_idx, it can produce an overflow and by the
        # modular nature in the arithmetic of ints it produces a
        # negative result and an array-index-out-of-bounds-like error.
        # But, in python the integer data type, according to the
        # documentation is of unlimited precision, so the overflow error
        # doesn't need to happen (I need to check this assertion).
        # Nonetheless I'm going to use the last formula because I think
        # that it's more intuitive and carries more meaning according
        # to its purpose:
        mid = low_idx + (high_idx - low_idx) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        if guess > item:
            high_idx = mid - 1
        else:
            low_idx = mid + 1
    
    return None
   
   
# Testing: 
if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 9]
    
    print(binary_search(my_list, 3))
    print(binary_search(my_list, -1))
    
