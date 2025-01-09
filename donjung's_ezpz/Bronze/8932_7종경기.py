def track(A, B, C, P):
	return int(A * (B - P) ** C)

def field(A, B, C, P):
	return int(A * (P - B) ** C)

for _ in range(int(input())):
	listi = list(map(int, input().split()))
	score = (track(9.23076, 26.7, 1.835, listi[0]) \
	+ field(1.84523, 75, 1.348, listi[1]) \
	+ field(56.0211, 1.5, 1.05, listi[2]) \
	+ track(4.99087, 42.5, 1.81, listi[3]) \
	+ field(0.188807, 210, 1.41, listi[4]) \
	+ field(15.9803, 3.8, 1.04, listi[5]) \
	+ track(0.11193, 254, 1.88, listi[6]))
	print(score)
