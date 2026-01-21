
def implied(p,q):
    return not p or q
def bicon(p,q):
    return (p and q) or (not p and not q)
def drawTable():
	propositions = [
     			 (True,True,True),
                 (True,True,False),
                 (True,False,True),
                 (True,False,False),
                 (True,True,True),
                 (False,True,False),
                 (False,False,True),
                 (False,False,False),
                 ]
	# print((True and True))
	print("p	| q	|r	|p<->q	|(p->r)<->(q->r)|")
	print("--------------------------------------------")
	for p, q,r in propositions:
		# implication = not p or q
		print(f"{p}	|{q}	|{r}	|{bicon(p,q)}	|	{bicon(implied(p,r),implied(q,r))}	|")
  
drawTable()