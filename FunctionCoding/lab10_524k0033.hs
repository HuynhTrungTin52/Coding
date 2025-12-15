--1)
type Row a = [a]
type Matrix a = [Row a]

--2)
isEmptyMatrix :: Matrix a -> Bool
isEmptyMatrix [] = True
isEmptyMatrix _ = False

--3)
matrixSize :: Matrix a -> (Int, Int)
matrixSize [] = (0, 0)
matrixSize m = (length m, length (head m))

--4)
addMatrix :: Num a => Matrix a -> Matrix a -> Maybe (Matrix a)
addMatrix m1 m2
    | matrixSize m1 /= matrixSize m2 = Nothing
    | otherwise = Just (zipWith (zipWith (+)) m1 m2)

--5)
scalarMultiplyRow :: Num a => a -> Row a -> Row a
scalarMultiplyRow k row = map (* k) row

--6)
transposeMatrix :: Matrix a -> Matrix a
transposeMatrix [] = []
transposeMatrix ([]:_) = []
transposeMatrix m = (map head m) : transposeMatrix (map tail m)

--7)
isUpperTriangular :: (Num a, Eq a) => Matrix a -> Bool
isUpperTriangular mat = checkZeros 0 mat
    where
        checkZeros _ [] = True
        checkZeros n (row:rows) = all (== 0) (take n row) && checkZeros (n + 1) rows