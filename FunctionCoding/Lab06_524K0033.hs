squareEvens :: Integral b => [b] -> [b]
squareEvens xs = map (^2) (filter even xs)


sumList :: [Int] -> Int
sumList = foldr (+) 0

prodList :: [Int] -> Int
prodList = foldr (*) 1

applyTwice :: (e -> e) -> e -> e
applyTwice f x = f (f x)

filterBelow :: Ord a => a -> [a] -> [a]
filterBelow threshold = filter (> threshold)

applyTwoFunctions :: (t1 -> t2) -> (t3 -> t1) -> t3 -> t2
applyTwoFunctions f g x = f ( g x)

splitBasedOn :: (a -> Bool) -> [a] -> ([a], [a])
splitBasedOn _ [] = ([], [])
splitBasedOn p (x:xs)
  | p x       = (x : trues, falses) 
  | otherwise = (trues, x : falses) 
  where
    (trues, falses) = splitBasedOn p xs 


zipWithSum :: [Integer] -> [Integer] -> [Integer]
zipWithSum = zipWith (+)