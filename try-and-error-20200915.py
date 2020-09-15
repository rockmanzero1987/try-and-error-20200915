# AB×CD×E=2040
# F×G×H×I=3024

import sys

numbers = []

for num in range(1, 10):
	numbers.append(num)

for a in range(1, 10):
	for b in range(1, 10):
		for c in range(1, 10):
			for d in range(1, 10):
				for e in range(1, 10):
					for f in range(1, 10):
						for g in range(1, 10):
							for h in range(1, 10):
								for i in range(1, 10):
									if (10 * a + b) * (10 * c + d) * e == 2040 and f * g * h * i == 3024:
										numbers = [a, b, c, d, e, f, g, h, i]
										if numbers.count(1) == 1 and numbers.count(2) == 1 and numbers.count(3) == 1 and numbers.count(4) == 1 and numbers.count(5) == 1 and numbers.count(6) == 1 and numbers.count(7) == 1 and numbers.count(8) == 1 and numbers.count(9) == 1:
											print(10 * a + b, ' * ', 10 * c + d, ' * ', e, ' = ', (10 * a + b) * (10 * c + d) * e)
											print(f, ' * ', g, ' * ', h, ' * ', i, ' = ', f * g * h * i)
											sys.exit('Done!')
