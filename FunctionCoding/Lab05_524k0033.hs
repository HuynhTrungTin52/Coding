import Prelude hiding (elem, (!!), replicate)

--1)
and :: [Bool] -> Bool
and = foldr (&&) True

concat :: [[a]] -> [a]
concat = foldr (++) []

replicate :: Int -> a -> [a]
replicate 0 _ = []
replicate n x = x : replicate (n - 1) x

(!!) :: [a] -> Int -> a
(x:_) !! 0 = x
(_:xs) !! n = xs !! (n - 1)
[] !! _ = error "Index out of bounds"

elem :: Eq a => a -> [a] -> Bool
elem _ [] = False
elem y (x:xs) = (y == x) || elem y xs

subsets :: [a] -> [[a]]
subsets [] = [[]]
subsets (x:xs) = subsets xs ++ map (x:) (subsets xs)

pascal :: Int -> Int -> Int
pascal 0 0 = 1
pascal n 0 = 1
pascal n k
 | n == k = 1
 | otherwise = pascal (n - 1) (k - 1) + pascal (n - 1) k

sSearch :: [Int] -> Int -> Bool
sSearch [] _ = False
sSearch (x:xs) n
 | x == n = True
 | x > n = False
 | otherwise = sSearch xs n


--2)
merge :: Ord a => [a] -> [a] -> [a]
merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys)
 | x <= y    = x : merge xs (y:ys)
 | otherwise = y : merge (x:xs) ys