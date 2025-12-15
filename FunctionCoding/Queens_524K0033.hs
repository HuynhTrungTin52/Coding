module Queens_524K0033 where

safe :: Int -> [Int] -> Int -> Bool
safe _ [] _ = True
safe newCol (c:cs) dist = 
    newCol /= c &&                  
    abs (newCol - c) /= dist &&     
    safe newCol cs (dist + 1)       

queens :: Int -> [[Int]]
queens n = map reverse (solve n)
  where
    solve 0 = [[]] 
    solve k = [ q:qs | qs <- solve (k-1), q <- [1..n], safe q qs 1 ]