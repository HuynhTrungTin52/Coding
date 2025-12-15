import Graphics.Gloss

main :: IO ()
main = display (InWindow "My Gloss Window" (500, 500) (100, 100)) white (Circle 100)