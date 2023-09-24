def find_min_max(numbers):
    min=1000
    max=-1000
    for i in range (len(numbers)):
        if max < numbers[i]: 
            max = numbers[i]
            if min > numbers[i]: 
                min = numbers[i]
                return min,max

