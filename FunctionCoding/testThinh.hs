module Main where

import Graphics.Gloss

cellSize :: Float
cellSize = 60.0

lightSquare :: Color
lightSquare = makeColorI 240 217 181 255 

darkSquare :: Color
darkSquare = makeColorI 181 136 99 255   


sampleSolution :: [Int]
sampleSolution = [1, 5, 8, 6, 3, 7, 2, 4]

drawBoard :: Picture
drawBoard = pictures [ drawCell r c | r <- [1..8], c <- [1..8] ]
  where
    drawCell r c = translate (xPos c) (yPos r) $ color (pickColor r c) $ rectangleSolid cellSize cellSize
    pickColor r c = if even (r + c) then darkSquare else lightSquare

drawQueens :: [Int] -> Picture
drawQueens queens = pictures [ translate (xPos col) (yPos row) queenShape 
                             | (row, col) <- zip [8,7..1] queens ] 

queenShape :: Picture
queenShape = pictures [
    color red $ circleSolid (cellSize * 0.35),
    color white $ translate (-10) (-10) $ scale 0.2 0.2 $ text "Q"
    ]

xPos :: Int -> Float
xPos c = (fromIntegral c - 4.5) * cellSize

yPos :: Int -> Float
yPos r = (fromIntegral r - 4.5) * cellSize

main :: IO ()
main = display window background (pictures [drawBoard, drawQueens sampleSolution])
  where
    window = InWindow "Figure 2: 8-Queens Visualization" (600, 600) (100, 100)
    background = white