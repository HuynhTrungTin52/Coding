import System.Random
naturalNumbers :: [Integer]
naturalNumbers = [1..]

--1)
take5N :: [Integer]
take5N= take 5 naturalNumbers

--2)
fib :: [Integer]
fib = 1 : 1 : zipWith (+) fib (drop 1 fib)
takeNofFib :: Int -> [Integer]
takeNofFib n= take n fib 

--3)
squareNum :: Num a => a -> a
squareNum n = n*n 
squaredNumbers :: [Integer]
squaredNumbers = map squareNum [1..]
takeNofSquare :: Int -> [Integer]
takeNofSquare n = take n squaredNumbers

--4)
ones :: [Integer]
ones = 1 : ones
lazySum :: Int -> Integer
lazySum n = sum (take n ones)

--5)
-- 0 : Up
-- 1 : Right
robotAlgorithm :: Int -> Int -> [Int] -> (Int, Int)
robotAlgorithm x y [] = (x, y)
robotAlgorithm x y (z:zs)
  | z == 0    = robotAlgorithm x (y + 1) zs
  | z == 1    = robotAlgorithm (x + 1) y zs
  | otherwise = robotAlgorithm x y zs

robot :: IO ()
robot = do
  g <- newStdGen
  let nums = randomRs (0,1) g :: [Int]
  let steps = take 50 nums
  print steps
  let finalPos = robotAlgorithm 0 0 steps
  print finalPos


--6)
isPerfectSquare :: Int -> Bool
isPerfectSquare n
  | n < 0     = False 
  | otherwise =
      let root = floor (sqrt (fromIntegral n :: Double))
      in root * root == n

parabol :: Num a => a -> a
parabol x = x*x-3*x+2
pNum :: [Int]
pNum = map parabol [1..]
res :: [Int]
res = filter isPerfectSquare pNum
take5Res :: [Int]
take5Res= take 5 res
--There's only 2 results, since the equation pNum can only be a perfect square when x=1 and x=2