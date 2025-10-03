main :: IO()
main = do
 putStr "Nhap list:"
 input<-getLine
 let lists = read input :: [Int]
 print (findMisSmal 1 lists)
 
isMember :: Eq t => t -> [t] -> Bool
isMember n [] =False 
isMember n (x:xs)
 | n==x =True 
 | otherwise =  isMember n xs


findMisSmal :: (Eq t, Num t) => t -> [t] -> t
findMisSmal small [] = small
findMisSmal small (x:xs)
 | isMember small (x:xs) = findMisSmal (small+1) xs
 | otherwise = small 