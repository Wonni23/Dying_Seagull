R = int(input())

Sang = input()

N = int(input())

Friend = [input() for i in range(N)]

score = 0
possible_max = 0

for j in range(R):
	rsp = [0, 0, 0]
	char = Sang[j]
	for i in range(N):
		char2 = Friend[i][j]
		if char2 == 'S':
			rsp[1] += 1
			if char == char2:
				score += 1
			elif char == 'R':
				score += 2
		elif char2 == 'R':
			rsp[0] += 1
			if char == char2:
				score += 1
			elif char == 'P':
				score += 2
		else:
			rsp[2] += 1
			if char == char2:
				score += 1
			elif char == 'S':
				score += 2
	# rsp 계산
	possible_max += max(2 * rsp[1] + 1 * rsp[0],
	2 * rsp[2] + 1 * rsp[1],
	2 * rsp[0] + 1 * rsp[2])

print(score)
print(possible_max)

# [묵, 찌, 빠]

#[PPRRS,
#RRSSP]

#Friend[0] = PPRRS
#Friend[1] = RRSSP
# print(Friend)