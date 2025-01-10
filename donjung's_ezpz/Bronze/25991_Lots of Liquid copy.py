n = int(input())

side_lengths = list(map(float, input().split()))

def solve_container_problem(n, side_lengths):
	total_volume = sum(side ** 3 for side in side_lengths)
	container_side = total_volume ** (1/3)
	return container_side

print(solve_container_problem(n, side_lengths))