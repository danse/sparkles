class Functor f => Applicative f where
  pure  :: a -> f a
  infixl 4 <*>
  (<*>) :: f (a -> b) -> f a -> f b

instance Monoid [a] where
        mempty  = []