import Data.List

main :: IO()
main = do
 putStr "Nhap list:"
 input<-getLine
 let lists = read input :: [Char]
 print (permutations lists)