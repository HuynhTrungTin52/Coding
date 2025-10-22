isPrime :: Int -> Bool
isPrime n
 | n <= 1    = False
 | otherwise = null [d | d <- [2..isqrt n], n `mod` d == 0]
 where
  isqrt :: Int -> Int
  isqrt = floor . sqrt . fromIntegral

isPerfectSquare :: Int -> Bool
isPerfectSquare n = n >= 0 && s * s == n
 where s = floor . sqrt . fromIntegral $ n

reverseInt :: Int -> Int
reverseInt = read . reverse . show

perfectNumbers :: [Int]
perfectNumbers = [n | n <- [1..9999], sum [d | d <- [1..n-1], n `mod` d == 0] == n]

primeSumTuples :: [(Int, Int)]
primeSumTuples = [(x, y) | x <- [1..99], y <- [1..99], isPrime (x + y)]

combinationsOfThree :: [(Int, Int, Int)]
combinationsOfThree =  [(a, b, c) | a <- nums, b <- nums, a < b, c <- nums, b < c]
 where nums = [1,2,3,4,5,6]

perfectSquareCubes :: [Int]
perfectSquareCubes = [n^6 | n <- [1..], n^6 < 1000]

knightMoves :: (Int, Int) -> [(Int, Int)]
knightMoves (x, y) = [(x', y') | (dx, dy) <- moves,
         let x' = x + dx, let y' = y + dy,
         x' >= 1 && x' <= 8,
         y' >= 1 && y' <= 8]
 where
  moves = [(1, 2), (1, -2), (-1, 2), (-1, -2),
     (2, 1), (2, -1), (-2, 1), (-2, -1)]

primeFibonacciNumbers :: [Int]
primeFibonacciNumbers = [n | n <- [1..9999], isFib n, isPrime n]
 where
  isFib n = isPerfectSquare (5 * n^2 + 4) || isPerfectSquare (5 * n^2 - 4)

emirpNumbers :: [Int]
emirpNumbers = [p | p <- [1..199], isPrime p, let rp = reverseInt p, p /= rp, isPrime rp]

