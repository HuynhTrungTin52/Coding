main :: IO()
main = do
 putStr "Nhap list:"
 input<-getLine
 let lists = read input :: [Int]
 putStr "Nhap n:"
 input<-getLine
 let n = read input :: Int
 
 print (countOccur n 0 lists)
isMember n [] =False 
isMember n (x:xs)
 | n==x =True 
 | otherwise =  isMember n xs

countOccur n count [] = count
countOccur n count (x:xs)
 | n `isMember` (x:xs) = countOccur n (count+1) xs 
 | otherwise = countOccur n count xs