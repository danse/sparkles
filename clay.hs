import System.Environment (getArgs)
import System.IO
import System.Console.ANSI
import Data.List

main = do
  args <- getArgs
  writeFile (intercalate " " args) "clay"
  clearScreen
