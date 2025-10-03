l=0
f[] = []
f (x:xs) = (l+1) f xs
getLength ns = l+1