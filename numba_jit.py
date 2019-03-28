from numba import jit
import math

@jit(nopython=True, parallel=True)
def find(v_max, v_min):
	G = []
	for v in range(2 * v_min + 1, 2 * v_max + 1, 2):
		print('v: ', v)
		n = 4 * v
		vs = round(1 + math.sqrt(n) + 0.5)
		vs2 = round(1 + math.sqrt(v * 2) + 0.5)
		k = 0
		for y in range(1, vs2, 2):
			y2 = 2 * y * y
			for x in range(1, vs, 2):
				x2 = x * x + y2
				for z in range(1, vs, 2):
					if x2 + z * z == n:
						k += 1
		G.append(k)
	return (G)
		
v_max = 100001 
v_min = 99995
f = open('g.txt', 'w')
G = find(v_max, v_min)
for element in G:
	f.write(str(element) + ',')
print(G)
