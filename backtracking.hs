-- https://groups.google.com/forum/#!topic/comp.lang.functional/ELVPeuLqN-c

-- find a subset of `xs` such that the sum of numbers is `n`
subSets 0 [] = [[]]
subSets _ [] = []
subSets n (x:xs)
   | x <= n = withX ++ withoutX
   | x >  n = withoutX
   where withX = map (x:) (subSets (n-x) xs)
         withoutX = subSets n xs

main = print $ subSets 10 [1..10]
