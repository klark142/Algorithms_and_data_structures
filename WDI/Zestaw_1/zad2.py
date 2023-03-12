# suma = 10000
# best = (2020, 0)

# for i in range(2022):
# 	y = 2021
# 	x = i
# 	while x > 0 and y > x:
# 		x, y = y-x, x
# 	if x + y < suma:
# 		suma = x + y
# 		best = (x, y)

# print(suma, best)


for sum in range(2, 2023):
	for a in range(1, sum):
		b = sum - a
		start_a = a
		start_b = b
		while a < 2022:
			temp = a
			a = b
			b = temp + b
			if a == 2022:
				print(start_a, start_b)
				exit()