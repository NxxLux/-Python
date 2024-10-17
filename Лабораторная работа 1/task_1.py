numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

total_sum = sum(numbers[:4] + numbers[5:])
count_with_none = len(numbers)
average = round(total_sum / (count_with_none), 2)
numbers[4] = average

print("Измененный список:", numbers)
