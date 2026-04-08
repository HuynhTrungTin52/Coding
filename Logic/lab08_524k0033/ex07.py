def towerOfHanoi(A, B, C, h=None):

	if h is None:
		h = len(A[1])
	
	if h <= 0:
		return
	
	if h > 1:
		towerOfHanoi(A, C, B, h - 1)
	
	disk = A[1].pop()
	C[1].append(disk)
	print(f"Move disk {disk} from {A[0]} to {C[0]}")
	
	if h > 1:
		towerOfHanoi(B, A, C, h - 1)

A = [['A'], [1, 2, 3]]
B = [['B'], []]
C = [['C'], []]
towerOfHanoi(A, B, C)