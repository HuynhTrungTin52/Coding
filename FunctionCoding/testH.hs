module Main
where
import Graphics.Gloss
import Graphics.Gloss.Interface.Pure.Game
import Data.List (intercalate)


type Board = [Int]        
type Position = (Int, Int) 

isSafe :: Board -> Int -> Int -> Bool
isSafe board row col = 
    not (rowConflict || diagonalConflict)
  where
    rowConflict = row `elem` board
    
    diagonalConflict = any checkDiagonal (zip board [0..])
    
    checkDiagonal (prevRow, prevCol) =
        abs (row - prevRow) == abs (col - prevCol)


queens :: Int -> [Board]
queens n = solve [] 0
  where
    
    solve :: Board -> Int -> [Board]
    solve board col
        | col == n = [board]
       
        | otherwise = 
           concatMap tryRow [0..n-1]
      where
        tryRow row
            | isSafe board row col = solve (board ++ [row]) (col + 1)
            | otherwise = []        

solveNQueens :: Int -> [Board]
solveNQueens n = queens n

getFirstNSolutions :: Int -> Int -> [Board]
getFirstNSolutions n count = take count (queens n)

--Total solutions?
countSolutions :: Int -> Int
countSolutions = length . queens

--Checking
isValidSolution :: Int -> Board -> Bool
isValidSolution n board = 
    length board == n && 
    all (\col -> isSafe (take col board) (board !! col) col) [0..n-1]

--5
boardToString :: Board -> String
boardToString board = 
    unlines [rowToString row | row <- [0..n-1]]
  where
    n = length board
    rowToString r = intercalate " " [if board !! c == r then "Q" else "." | c <- [0..n-1]]

printSolution :: Int -> Board -> IO ()
printSolution num board = do
    putStrLn $ "\n=== Solution " ++ show num ++ " ==="
    putStrLn $ boardToString board

-- Print all solutions
printAllSolutions :: Int -> IO ()
printAllSolutions n = do
    let solutions = queens n
    putStrLn $ "Found " ++ show (length solutions) ++ " solutions for " ++ show n ++ "-Queens problem\n"
    mapM_ (uncurry printSolution) (zip [1..] solutions)


--6
window :: Display
window = InWindow "8-Queens Problem Solution" (800, 800) (100, 100)

background :: Color
background = white

-- Chessboard size
cellSize :: Float
cellSize = 80

boardOffset :: Float
boardOffset = -320


drawChessboard :: Int -> Picture
drawChessboard n = pictures [drawCell row col | row <- [0..n-1], col <- [0..n-1]]
  where
    drawCell row col = 
        translate x y $ color cellColor $ rectangleSolid cellSize cellSize
      where
        x = boardOffset + fromIntegral col * cellSize + cellSize / 2
        y = boardOffset + fromIntegral (n - 1 - row) * cellSize + cellSize / 2
        cellColor = if (row + col) `mod` 2 == 0 
                    then makeColor 0.9 0.9 0.9 1.0 
                    else makeColor 0.4 0.4 0.4 1.0 

drawQueens :: Int -> Board -> Picture
drawQueens n board = pictures [drawQueen row col | (row, col) <- zip board [0..]]
  where
    drawQueen row col = 
        translate x y $ pictures
            [ color red $ circleSolid (cellSize * 0.35)  -- Main circle
            , color yellow $ circleSolid (cellSize * 0.15)  -- Crown
            ]
      where
        x = boardOffset + fromIntegral col * cellSize + cellSize / 2
        y = boardOffset + fromIntegral (n - 1 - row) * cellSize + cellSize / 2


drawSolution :: Int -> Board -> Picture
drawSolution n board = pictures
    [ drawChessboard n
    , drawQueens n board
    , drawTitle n
    , drawInfo board
    ]

drawTitle :: Int -> Picture
drawTitle n = translate (-150) 380 $ scale 0.3 0.3 $ 
              color black $ text (show n ++ "-Queens Problem Solution")

-- Bottom: solution
drawInfo :: Board -> Picture
drawInfo board = translate (-150) (-380) $ scale 0.2 0.2 $ 
                 color black $ text ("Solution: " ++ show board)


data AppState = AppState
    { currentSolution :: Int
    , allSolutions :: [Board]
    , boardSize :: Int
    }

initialState :: Int -> AppState
initialState n = AppState
    { currentSolution = 0
    , allSolutions = queens n
    , boardSize = n
    }

renderState :: AppState -> Picture
renderState state = 
    case allSolutions state of
        [] -> translate (-200) 0 $ scale 0.3 0.3 $ color red $ text "No solutions found"
        sols -> pictures
            [ drawSolution (boardSize state) (sols !! idx)
            , drawNavigation idx (length sols)
            ]
  where
    idx = currentSolution state `mod` length (allSolutions state)

drawNavigation :: Int -> Int -> Picture
drawNavigation current total = translate (-300) (-420) $ scale 0.15 0.15 $ 
    color blue $ text $ "Solution " ++ show (current + 1) ++ " / " ++ show total ++ 
                        " | Press LEFT/RIGHT arrows to navigate"

handleInput :: Event -> AppState -> AppState
handleInput (EventKey (SpecialKey KeyRight) Down _ _) state =
    state { currentSolution = (currentSolution state + 1) `mod` length (allSolutions state) }
handleInput (EventKey (SpecialKey KeyLeft) Down _ _) state =
    state { currentSolution = (currentSolution state - 1) `mod` length (allSolutions state) }
handleInput _ state = state

updateState :: Float -> AppState -> AppState
updateState _ state = state


--Main
mainConsole :: IO ()
mainConsole = do
    putStrLn " 8-Queens Problem Solver"
    putStrLn "\nTesting with 4-Queens (simple case)"
    printAllSolutions 4
    
    putStrLn "\nTesting with 8-Queens (main problem)"
    let solutions8 = queens 8
    putStrLn $ "Found " ++ show (length solutions8) ++ " solutions for 8-Queens problem"
    putStrLn "\nShowing first 3 solutions:"
    mapM_ (uncurry printSolution) (zip [1..3] (take 3 solutions8))

--single solution
mainStatic :: IO ()
mainStatic = do
    let solutions = queens 8
    case solutions of
        [] -> putStrLn "No solutions found!"
        (firstSolution:_) -> do
            putStrLn $ "Displaying solution: " ++ show firstSolution
            display window background (drawSolution 8 firstSolution)

--browse solution
mainInteractive :: IO ()
mainInteractive = do
    let n = 8
    putStrLn $ "=== Interactive " ++ show n ++ "-Queens Visualizer ==="
    putStrLn "Use LEFT/RIGHT arrow keys to browse through solutions"
    putStrLn "Close window to exit"
    play window background 30 (initialState n) renderState handleInput updateState

-- interactive mode
main :: IO ()
main = mainInteractive