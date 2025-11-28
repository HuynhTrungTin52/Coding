import Data.List (sort)

-- 1
greeting :: IO ()
greeting = do
  putStrLn "Enter your name:"
  name <- getLine
  putStrLn ("Hello, " ++ name ++ "!")


-- 2
sumTwoNumbers :: IO ()
sumTwoNumbers = do
  putStrLn "Enter first integer:"
  input1 <- getLine
  let num1 = read input1 :: Int
  
  putStrLn "Enter second integer:"
  input2 <- getLine
  let num2 = read input2 :: Int
  
  let total = num1 + num2
  putStrLn ("The sum of " ++ show num1 ++ " and " ++ show num2 ++ " is " ++ show total ++ ".")


-- 3
sumList :: IO ()
sumList = do
  putStrLn "Enter a list of integers (separated by spaces):"
  input <- getLine
  let numbers = map read (words input) :: [Int]
  let total = sum numbers
  putStrLn ("The sum is " ++ show total ++ ".")


-- 4
findMinMax :: IO ()
findMinMax = do
  putStrLn "Enter a list of integers (separated by spaces):"
  input <- getLine
  let numbers = map read (words input) :: [Int]
  let largest = maximum numbers
  let smallest = minimum numbers
  putStrLn ("The largest number is " ++ show largest ++ ", and the smallest number is " ++ show smallest ++ ".")


-- 5
multiplicationTable :: IO ()
multiplicationTable = do
  putStrLn "Enter an integer:"
  input <- getLine
  let num = read input :: Int
  mapM_ (\i -> putStrLn (show num ++ " x " ++ show i ++ " = " ++ show (num * i))) [1..10]


-- 6
sortList :: IO ()
sortList = do
  putStrLn "Enter a list of integers (separated by spaces):"
  input <- getLine
  let numbers = map read (words input) :: [Int]
  let ascending = sort numbers
  let descending = reverse ascending
  putStrLn ("Ascending: " ++ unwords (map show ascending))
  putStrLn ("Descending: " ++ unwords (map show descending))


-- 7
evaluateExpression :: IO ()
evaluateExpression = do
  putStrLn "Enter a mathematical expression (e.g., 3 + 4 * 2):"
  input <- getLine
  let result = calculate input
  putStrLn (show result ++ ".")


calculate :: String -> Double
calculate expr = evalAddSub (words expr)

evalAddSub :: [String] -> Double
evalAddSub tokens = foldl applyOp num rest
  where
    (num, rest) = evalMulDiv tokens
    applyOp acc (op:xs) = 
      let (nextNum, remaining) = evalMulDiv xs
      in case op of
           "+" -> acc + nextNum
           "-" -> acc - nextNum
           _   -> acc
    applyOp acc _ = acc

evalMulDiv :: [String] -> (Double, [String])
evalMulDiv (x:xs) = foldl' applyOp (read x, xs) xs
  where
    foldl' _ acc [] = acc
    foldl' f acc (y:ys)
      | y `elem` ["*", "/"] = 
          let (num, rest) = acc
              nextNum = read (head ys) :: Double
              newNum = case y of
                        "*" -> num * nextNum
                        "/" -> num / nextNum
                        _   -> num
          in foldl' f (newNum, tail ys) (tail ys)
      | otherwise = acc
evalMulDiv [] = (0, [])

--Test
main :: IO ()
main = do
  putStrLn "Choose an exercise (1-7)"
  putStrLn "1. Greeting"
  putStrLn "2. Sum of Two Integers"
  putStrLn "3. Sum of List"
  putStrLn "4. Find Min and Max"
  putStrLn "5. Multiplication Table"
  putStrLn "6. Sort List"
  putStrLn "7. Expression Calculator"
  putStr "\nYour choice: "
  
  choice <- getLine
  putStrLn ""
  
  case choice of
    "1" -> greeting >> main
    "2" -> sumTwoNumbers >> main
    "3" -> sumList >> main
    "4" -> findMinMax >> main
    "5" -> multiplicationTable >> main
    "6" -> sortList >> main
    "7" -> evaluateExpression >> main
    _   -> putStrLn "Invalid choice!" >> main