getLast xs = head (drop aLength xs)
	where 
		aLength = length xs -1
