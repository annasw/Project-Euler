-- pretty slow
euler5 n k = if divByAll n k then n else euler5 (n+k) k
    where divByAll n k
            | k <= 1 = True
            | n`mod`k/=0 = False
            | otherwise = divByAll n (k-1)
