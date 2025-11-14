ex1 :: IO()
ex1 = do
 putStrLn "Nhap N:"
 input<-getLine
 print("Hello " ++ input)

ex2 :: IO()
ex2 = do 
 putStr "Nhap A:"
 input<-getLine
 let a = read input :: Int
 putStrLn ""
 putStr "Nhap B:"
 input<-getLine
 let b = read input :: Int 
 putStr "A+B="
 print(a+b)

ex3 :: IO()
ex3 = do 
 putStr "Nhap chuoi so int:"
 input<-getLine
 let a = map read (words input) :: [Int]
 putStrLn ("Tong cong la " ++ show (sum a))

ex4 :: IO()
ex4 = do
 putStr "Nhap chuoi so int:"
 input<-getLine
 let a = map read (words input) :: [Int]
 putStrLn ("Lon nhat la " ++ show (maximum a)++ ", Nho nhat la "++ show(minimum a))

ex5:: IO()
ex5 = do
 putStr "Nhap A:"
 input<-getLine
 let a = read input :: Int
 putStrLn ""
 printMultiplyTable a

printRow :: (Show a, Num a) => a -> a -> IO ()
printRow n i = putStrLn( show n ++ " x " ++ show i ++ " = " ++ show (n * i))

printMultiplyTable :: (Show a, Num a, Enum a) => a -> IO ()
printMultiplyTable a = mapM_ (printRow a) [1..10]

ex6:: IO()
ex6= do
 putStr "Nhap chuoi so int:"
 input<-getLine
 let a = map read (words input) :: [Int]
 putStrLn ""
 print ("Ascending : " ++ show (mergeSortAsc a))
 print ("Descending : " ++ show (mergeSortDsc a))
 

mergeSortAsc :: Ord a => [a] -> [a]
mergeSortAsc [] = []
mergeSortAsc [x] = [x]
mergeSortAsc xs = mergeAsc (mergeSortAsc ys) (mergeSortAsc zs)
  where
    (ys, zs) = splitHalf xs

splitHalf :: [a] -> ([a], [a])
splitHalf xs = splitAt (length xs `div` 2) xs

mergeAsc :: Ord a => [a] -> [a] -> [a]
mergeAsc [] ys = ys
mergeAsc xs [] = xs
mergeAsc (x:xs) (y:ys)
  | x <= y    = x : mergeAsc xs (y:ys)
  | otherwise = y : mergeAsc (x:xs) ys

mergeSortDsc :: Ord a => [a] -> [a]
mergeSortDsc [] = []
mergeSortDsc [x] = [x]
mergeSortDsc xs = mergeDsc (mergeSortDsc ys) (mergeSortDsc zs)
  where
    (ys, zs) = splitHalf xs


mergeDsc :: Ord a => [a] -> [a] -> [a]
mergeDsc [] ys = ys
mergeDsc xs [] = xs
mergeDsc (x:xs) (y:ys)
  | x >= y    = x : mergeDsc xs (y:ys)
  | otherwise = y : mergeDsc (x:xs) ys


ex7 :: IO()
ex7 = do
  putStr "Nhap chuoi so cong thuc:"
  input <- getLine
  putStrLn ""
  print (evaluate input)

evaluate :: String -> Double
evaluate s = fst (parseExpr s)

skipSpaces :: String -> String
skipSpaces = dropWhile (== ' ')

isDigit :: Char -> Bool
isDigit c = c >= '0' && c <= '9'

parseNumber :: String -> (Double, String)
parseNumber s =
  let t = skipSpaces s
      (numStr, rest) = span (\c -> isDigit c || c == '.') t
  in if null numStr then (0, t) else (read numStr, rest)

parseFactor :: String -> (Double, String)
parseFactor s =
  let t = skipSpaces s
  in case t of
       ('(':rest) ->
         let (v, rest2) = parseExpr rest
             rest3 = skipSpaces rest2
         in if not (null rest3) && head rest3 == ')'
              then (v, tail rest3)
              else (v, rest3)
       ('-':rest) ->
         let (v, rest2) = parseFactor rest
         in (-v, rest2)
       ('+':rest) -> parseFactor rest
       _ -> parseNumber t

parseTerm :: String -> (Double, String)
parseTerm s =
  let (v, rest) = parseFactor s
  in parseTerm' v rest

parseTerm' :: Double -> String -> (Double, String)
parseTerm' acc s =
  let t = skipSpaces s
  in case t of
       ('*':rest) ->
         let (v, rest2) = parseFactor rest
         in parseTerm' (acc * v) rest2
       ('/':rest) ->
         let (v, rest2) = parseFactor rest
         in parseTerm' (acc / v) rest2
       _ -> (acc, s)

parseExpr :: String -> (Double, String)
parseExpr s =
  let (v, rest) = parseTerm s
  in parseExpr' v rest

parseExpr' :: Double -> String -> (Double, String)
parseExpr' acc s =
  let t = skipSpaces s
  in case t of
       ('+':rest) ->
         let (v, rest2) = parseTerm rest
         in parseExpr' (acc + v) rest2
       ('-':rest) ->
         let (v, rest2) = parseTerm rest
         in parseExpr' (acc - v) rest2
       _ -> (acc, s)