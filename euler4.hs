euler4 = maximum [ x*y | x <- [100..999], y <- [100..999], isPal $ show (x*y) ]
    where isPal n -- string n. Not using the reverse xs function b/c i want to practice
            | length n <= 1 = True
            | head n /= last n = False
            | otherwise = isPal $ init $ tail n
            
