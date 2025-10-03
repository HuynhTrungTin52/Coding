main :: IO()
main = do
 putStr "Nhap list:"
 input<-getLine
 let lists = read input :: [Int]
 putStr "Nhap n:"
 input<-getLine
 let n = read input :: Int
 
 print (countOccur n lists)
 
countOccur :: (Num a, Eq t) => t -> [t] -> a
countOccur _ [] = 0
countOccur n (x:xs)
 | n==x = 1+countOccur n xs
 | otherwise = countOccur n xs