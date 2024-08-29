array = [100, -100]
max_val = array[0]  # setting max value to the first value in the array
min_val = array[0]  # setting min value to the first value in the array

for i in array:  # iterating through the array
    if i > max_val:  # if the current value in the array is bigger than the max value, this current value then becomes the max value as expected
        max_val = i
    elif i < min_val:
        min_val = i
    else:  # if the current value is equal to the max or min value, as for the first value in the array, then continue iterating through the array
        continue

min_max = [min_val, max_val]
print(min_max)
