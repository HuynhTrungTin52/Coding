second :: [t] -> t
-- Polymorphic function
second xs = head (tail xs)

swap :: (t,t1) -> (t1,t)
swap (x,y) = (y,x)

pair :: t -> t1 ->(t,t1)
pair x y = (x,y)

double :: Num t=> t->t 
double x = x*2

palindrome :: Eq t=> [t]->Bool
palindrome xs = reverse xs == xs

-- twice :: 
twice f x = f (f x)