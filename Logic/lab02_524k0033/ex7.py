
def implied(p,q):
    return not p or q
# List of all possible truth values for p and q
def drawTable1():
	propositions = [(True, True), (True, False), (False, True), (False, False)]
	print((True and True))
	print("p	| q	|~(p → q)|p ^ ~q")
	print("--------------------------------------------")
	equivalent=True
	for p, q in propositions:
		express1=not (implied(p,q))
		express2= p and not q
		if express1!=express2:
			equivalent=False
		# implication = not p or q
		print(f"{p}	|{q}	|{express1}|{express2}")
	conclusion = "~(p → q) ≡ p ^ ~q" if equivalent else "~(p → q) !≡ p ^ ~q"
	print("Conclusion:"+conclusion)
 
def drawTable2():
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
	print("p	| q	|r	|p→(q v r)|(p ^ ~q)→r|")
	print("--------------------------------------------")
	equivalent=True
	for p, q,r in propositions:
		# implication = not p or q
		express1= implied(p,(q and r))
		express2= implied((p and not q),r)
		print(f"{p}	|{q}	|{r}	|{express1}		|	{express2}	|")
		if express1!=express2:
			equivalent=False
	conclusion="p→(q v r)≡(p ^ ~q)→r" if equivalent else "p→(q v r)!≡(p ^ ~q)→r"
	print("Conclusion:"+conclusion)
	

  
  
drawTable1()
drawTable2()