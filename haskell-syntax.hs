{-# LANGUAGE OverloadedStrings, DeriveDataTypeable #-}

class Functor f => Applicative f where
  pure  :: a -> f a
  infixl 4 <*>
  (<*>) :: f (a -> b) -> f a -> f b

instance Monoid [a] where
        mempty  = []

f a =
  let b = a * 2
  in b + a

guarded something
  | condition something = result
  | otherwise           = somethingElse


-- in the following case, the indentation provided by `haskell-mode`
-- will be uglier
ifMonadic = do
  somethingMonadic
  if somethingIf
    then
      do
        somethingThen
    else
      do
        somethingElse

-- `Single` and `Multiple` are data constructors. They are necessary
data Argument = Single Int | Multiple [Int]
