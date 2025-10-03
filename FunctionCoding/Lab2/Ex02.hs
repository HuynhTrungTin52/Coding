main :: IO()
main = do
 putStr "Nhap A:"
 input<-getLine
 let a = read input :: Int
 putStrLn ""
 putStr "Nhap B:"
 input<-getLine
 let b = read input :: Int 
 putStr "A+B="
 print(a+b)