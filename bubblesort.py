array = [10,19,13,20,4,7,1,24,11,17,23,6,15,21,8,18,2,16,25,9,12,3,5,14,22]

s_offset = 0
not_ordered_count = 1

while True:

    #run until the list is ordered
    if not_ordered_count == 0:
        break

    offset = s_offset
    not_ordered_count = 0

    # run until the end of the array is reached
    while offset <= len(array) - 2:

        #set starting offset for next pass
        if offset == 0:
            s_offset = 1
        elif offset == 1:
            s_offset = 0

        # if first number is greater than the second number, then switch the two numbers
        if array[offset] > array[offset + 1]:
            array[offset],array[offset + 1] = array[offset + 1],array[offset]

            not_ordered_count = not_ordered_count + 1

        #move to next pair
        offset = offset + 2

print(array)
