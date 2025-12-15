import Graphics.Gloss
import Queens_524K0033 (queens) 


cellSize :: Float
cellSize = 70

boardSize :: Int
boardSize = 8

drawSquare :: Int -> Int -> Picture
drawSquare row col = 
    let color' = if even (row + col) then white else black
        x = fromIntegral col * cellSize
        y = fromIntegral row * cellSize
    in translate x y $ color color' $ rectangleSolid cellSize cellSize

drawQueen :: Int -> Int -> Picture
drawQueen row col =
    let x = fromIntegral col * cellSize
        y = fromIntegral row * cellSize
    in translate x y $ color red $ circleSolid (cellSize * 0.3)

drawBoard :: [Int] -> Picture
drawBoard solution = pictures (squares ++ queens)
  where
    indices = [0..boardSize-1]
    squares = [drawSquare r c | r <- indices, c <- indices]
    queens  = [drawQueen r (c-1) | (r, c) <- zip indices solution]

main :: IO ()
main = do
    let solution = head (queens boardSize) 
    display 
        (InWindow "8 Queens Solution" (600, 600) (10, 10)) 
        (greyN 0.5)                                         
        (translate (-200) (-200) (drawBoard solution))     