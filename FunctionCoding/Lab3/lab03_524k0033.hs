conAbsolute :: (Ord a, Num a) => a -> a
conAbsolute n = if n<0 then n*(-1) else n

checkType :: (Ord a, Num a) => a -> String
checkType n =
 if n < 0 then "negative"
 else if n>0 then "positive"
 else "zero"

guardAbsolute :: (Ord a, Num a) => a -> a
guardAbsolute n
 | n<0 = n*(-1)
 | otherwise = n

myNot :: Bool -> Bool
myNot = not

myAnd1 :: Bool -> Bool -> Bool
myAnd1 a b = a && b

myAnd2 a b = if a == False then False else if a == True then if b == True then True else False else False

myHead :: [a] -> a
myHead (x:_) = x

myTail :: [a] -> [a]
myTail (_:xs) = xs

safetailA :: [a] -> [a]
safetailA xs =
 if null xs then [] else tail xs  
safetailB :: [a] -> [a]
safetailB xs 
 | null xs = []
 | otherwise = tail xs
safetailC :: [a] -> [a]
safetailC []=[]
safetailC (x:xs) = xs

odd :: (Num a, Enum a) => a -> [a]
odd n = toOdd[0..n-1]
 where 
 toOdd xs = [x*2+1 | x<-xs]

zipWithSum :: [Integer] -> [Integer] -> [Integer]
zipWithSum = zipWith (+)

mergeSort :: Ord a => [a] -> [a]
mergeSort [] = []
mergeSort [x] = [x]
mergeSort xs = merge (mergeSort ys) (mergeSort zs)
  where
    (ys, zs) = splitHalf xs

splitHalf :: [a] -> ([a], [a])
splitHalf xs = splitAt (length xs `div` 2) xs

merge :: Ord a => [a] -> [a] -> [a]
merge [] ys = ys
merge xs [] = xs
merge (x:xs) (y:ys)
  | x <= y    = x : merge xs (y:ys)
  | otherwise = y : merge (x:xs) ys