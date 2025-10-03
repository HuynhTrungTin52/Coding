main :: IO()
main = do
 putStrLn "Nhap N:"
 input<-getLine
 let n = read input :: Int 
 print(oddOrEven n)
oddOrEven :: Int -> [Char] 
oddOrEven n 
 | even n  = ['E','v','e','n']
 | otherwise = ['O','d','d']