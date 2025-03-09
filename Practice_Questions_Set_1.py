#%%
def test_func(n):
    print(f"Entering function with n = {n}")
    if n > 1:
        test_func(n - 1)  # Recursive call
    print(f"Exiting function with n = {n}")

test_func(3)


# %%
#Recursion/Call Stack Example
n=5


def sumd(n):
    if(n>1):
        print(f"n: {n}")
        sumd(n-1)
        print(f"after n {n}")

sumd(n)

# %%
# Merge Sort

# Merge Sort Function
def merge_sort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the elements into 2 halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0

        # Copy data to temporary arrays left_half and right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Sample array to sort
array = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", array)

merge_sort(array)
print("Sorted array:", array)

#%%

n = 4

def test(n):
    if n>1:
        print(f"n: {n}")
        test(n-1)
        print(f"n after {n}")

test(n)
# %%

n = 4

def test(n):
    if n>1:
        print(f"n: {n}")
        test(n-1)
    print("out of if",n)

test(n)

# %%
def min_possible_number(num):
    num_str = str(num)
    if num < 0:
        # Negative case: sort in descending order and add negative sign
        sorted_str = ''.join(sorted(num_str[1:], reverse=True))
        return int('-' + sorted_str)
    else:
        # Positive case: sort in ascending order
        sorted_str = ''.join(sorted(num_str))
        # Handle leading zeros
        if sorted_str[0] == '0':
            for i in range(1, len(sorted_str)):
                if sorted_str[i] != '0':
                    sorted_str = sorted_str[i] + sorted_str[:i] + sorted_str[i+1:]
                    break
        return int(sorted_str)

# Test examples
print(min_possible_number(3102))   # Output: 1023
print(min_possible_number(-3087))  # Output: -3210


#%%
def desc_order(num):
    num_string = str(num)

    num_string = sorted(num_string, reverse = True)

    num_string = ''.join(num_string[:])

    return num_string

print(desc_order(54829))


# %%
