import System.Random
ex5 :: IO ()
ex5 = do
    g <- newStdGen
    let moves = randomRs (0, 1) g :: [Int]

        robot_seq (x, y) []     = (x, y)
        robot_seq (x, y) (0:ms) = robot_seq (x + 1, y) ms
        robot_seq (x, y) (1:ms) = robot_seq (x, y + 1) ms

        finalPos = robot_seq (0, 0) (take 50 moves)

    putStrLn $ "Position of robot after 50 moves: " ++ show finalPos