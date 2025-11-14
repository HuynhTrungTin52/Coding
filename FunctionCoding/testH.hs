-- ex01
and :: [Bool] -> Bool
and [] = True
and (x:xs) =
  if x == False
    then False
    else and xs

concat :: [[a]] -> [a]
concat [] = []
concat (xs:xss) = xs ++ concat xss

replicate :: Int -> a -> [a]
replicate n x =
  if n <= 0
    then []
    else x : replicate (n - 1) x

(!!) :: [a] -> Int -> a
(x:_) !! 0 = x
(_:xs) !! n = xs !! (n - 1)
[] !! _ = error "Index out of bounds"

elem :: Eq a => a -> [a] -> Bool
elem _ [] = False
elem y (x:xs) =
  if y == x
    then True
    else elem y xs

subsets :: [a] -> [[a]]
subsets [] = [[]]
subsets (x:xs) =
  let smaller = subsets xs
  in smaller ++ map (\s -> x : s) smaller

pascal :: Int -> Int -> Int
pascal n k =
  if k == 0
    then 1
    else if n == k
      then 1
      else pascal (n - 1) (k - 1) + pascal (n - 1) k

sSearch :: [Int] -> Int -> Bool
sSearch [] _ = False
sSearch (x:xs) n =
  if x == n
    then True
    else if x > n
      then False
      else sSearch xs n


-- ex02
merge :: Ord a => [a] -> [a] -> [a]
merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys) =
  if x <= y
    then x : merge xs (y:ys)
    else y : merge (x:xs) ys