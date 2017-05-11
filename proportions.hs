-- Haskell as a spreadsheet
import Control.Monad (mapM)
import Data.Monoid ((<>))

data Share = Share { label :: String, amount :: Float }
instance Show Share where
  show (Share l a) = l <> " " <> show a

personal = [Share "social" (1/4), -- twitter, facebook, slack
            Share "study" (1/2), -- code, study, tech
            Share "other" (1/4)]

clients = Share "clients" (4/5)

onAmount f s = Share (label s) (f (amount s))

week = [clients] <> map (onAmount (* (1/5))) personal

days = map (onAmount (* 5)) week

hours = map (onAmount (* 7)) days

main = do
  putStrLn "Days"
  mapM print days
  putStrLn ""
  putStrLn "Hours"
  mapM print hours
  return ()
