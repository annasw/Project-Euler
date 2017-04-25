euler2 = sum $ takeWhile (<=4000000) $ filter even fib where fib = 0 : scanl (+) 1 fib
