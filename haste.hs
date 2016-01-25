-- minimal example of client-server app in Haste, from http://ekblad.cc/lic.pdf
import Haste.App

helloServer :: String -> Server ()
helloServer name = liftIO $ putStrLn $ name ++ " says hello!"

app :: App Done
app = do
  greetings <- remote helloServer

  runClient $ do
    name <- prompt "Hi there, what is your name?"
    onServer $ greetings <.> name

main :: IO ()
main = runApp (mkConfig "localhost" 1111) app
