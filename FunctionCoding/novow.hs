removeVowel :: [Char] -> [Char]
removeVowel  = filter (not . isVowel) 
 where
 isVowel c = c `elem` "aeiouAEIOU"