#### With Haskell:

Search:

    ~ $ nix-env -f '<nixpkgs>' -qaA haskellPackages.ghc
    
Install:

    ~ $ nix-env -f '<nixpkgs>' -iA haskellPackages.ghc

#### Upgrading all packages:

    ~ $ nix-channel --update
    ~ $ nix-env --upgrade

Note that, after these commands, i got Nix actually updating just
after i logged into a Nix shell
