
# List of all possible truth values for p and q
def drawTable():
	propositions = [(True, True), (True, False), (False, True), (False, False)]
	# print((True and True))
	print("p	| q	|p v ~p |p ^ ~p |(p ^ q) v (~p v (p ^ ~q))|(p ^ ~q) ^ (~p v q)  |")
	print("--------------------------------------------")
	for p, q in propositions:
		# implication = not p or q
		print(f"{p}	|{q}	|{p or not p}	|{p and not p}	|{(p and q) or (not p or(p and not q))}			  | 	{(p and not q) and (not p and q)}		|")
  
drawTable()