squareEvens :: Integral a => [a] -> [a]
squareEvens xs = map (\x -> x * x) (filter (\x -> even x) xs)

sumList :: [Int] -> Int
sumList xs = foldr (+) 0 xs

prodList :: [Int] -> Int
prodList xs = foldr (*) 1 xs

applyTwice :: (a -> a) -> a -> a
applyTwice f x = f (f x)

filterBelow :: Ord a => a -> [a] -> [a]
filterBelow threshold xs = filter (\x -> x > threshold) xs

applyTwoFunctions :: (b -> c) -> (a -> b) -> a -> c
applyTwoFunctions f g x = f (g x)

splitBasedOn :: (a -> Bool) -> [a] -> ([a], [a])
splitBasedOn p [] = ([], [])
splitBasedOn p (x:xs) =
  let (ts, fs) = splitBasedOn p xs
  in if p x
       then (x:ts, fs)
       else (ts, x:fs)

zipWithSum :: [Integer] -> [Integer] -> [Integer]
zipWithSum xs ys = zipWith (+) xs ys