main :: IO()
main = do
 putStr "Nhap string:"
 input<-getLine
 let str = read input :: String
 print(isPalin str)
isPalin :: String -> Bool 
isPalin str = reverse str == str 