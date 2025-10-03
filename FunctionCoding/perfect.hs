factor a = [x | x <- [1..a], a `mod` x == 0]
perfects n = sum(factor n) == 2*n