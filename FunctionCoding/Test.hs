f [] = []
f (x:xs) = f ys ++ [x] ++ f zs
-- Any variable ends with an s is a list
	where
		ys = [a | a <- xs, a <= x]
		zs = [b | b <- xs, b > x]