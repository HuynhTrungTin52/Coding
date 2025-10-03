tongChuSo n 
	| n<0 =tongChuSo(-n)
	| n < 10 = n 
	| otherwise = (n `mod` 10) + tongChuSo(n `div` 10)