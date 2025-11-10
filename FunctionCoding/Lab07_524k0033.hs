import GHC.IO.Handle (Newline)
--1)
data Shape = Circle Float | Rect Float Float

square :: Float -> Shape
square n = Rect n n


area :: Shape -> Float
area (Circle r) = pi * r^2
area (Rect x y) = x * y

--2)
data Person = Person String  Int  String 
isAdult :: Person -> Bool
isAdult (Person name age address) = age > 18

--3)
data TrafficLight = Red | Green | Yellow
canGo :: TrafficLight -> String
canGo Red = "Stop"
canGo _   = "Go"

--4)
data Temperature = Celcius Float | Farenheit Float | Kelvin Float
convertFK (Farenheit f) = ((f - 32) * 5 / 9) + 273.15
convertFC (Farenheit f) =(f-32)*(5/9)

--5)
data Optional a = Some a | None
isPresent :: Optional a -> Bool
isPresent None=False
isPresent _ = True

--6)
data ThreeDPoint = ThreeDPoint Float Float Float
distanceFromOrigin (ThreeDPoint x y z) = sqrt(x*x+y*y+z*z)

--7)
data Day = Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday
isWeekend Saturday = True
isWeekend Sunday = True
isWeekend _ = False

--8)
data NewList = NewList [Int]

isElem x (NewList xs) = x `elem` xs