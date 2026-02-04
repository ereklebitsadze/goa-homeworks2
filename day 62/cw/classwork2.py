numbers = list(range(1, 101))

every_10th = [numbers[i] for i in range(len(numbers)) if (i+1) % 10 == 0]

print(every_10th)
