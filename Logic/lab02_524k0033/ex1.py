p=True
q=False
r=True
def evaluate(p,q,r):
	implication= not p or q
	
	express2= not p and q
	
	express3=p and (q and r)
	
	express4=p and (not q or r)
    
	res = {
		"p->q": implication,
		"~p A q": express2,
		"p A (q A r)": express3,
		"p A (~q V r)":express4
	}
	return res


print(evaluate(True,True,True))


# print(f"1)p->q:{implication}")
# print(f"2)~p A q:{express2}")
# print(f"3)p A (q A r):{express3}")
# print(f"4)p A (~q V r):{express4}")
