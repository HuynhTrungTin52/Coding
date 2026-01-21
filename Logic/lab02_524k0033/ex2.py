
def implied(p,q):
    return not p or q
# List of all possible truth values for p and q
def drawTable():
	propositions = [(True, True), (True, False), (False, True), (False, False)]
	# print((True and True))
	print("p	| q	|~p	|p AND q|p OR q |p->q	|~p AND q|~p AND q->~q|(p AND q) AND (~p AND q)->q|")
	print("--------------------------------------------")
	for p, q in propositions:
		p_and_q = p and q
		p_or_q = p or q
		not_p_and_q= not p and q
		# implication = not p or q
		print(f"{p}	|{q}	|{not p}	|{p_and_q}	|{p_or_q}	|{implied(p,q)}	|{not_p_and_q}	 |{implied((not p or q), (not q))}	      |		{implied(((p or q) and (not p and q)),q)}")
  
drawTable()