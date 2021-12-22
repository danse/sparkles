
{,un}highlight-regexp

M-x overwrite-mode

C-x C-e eval before point

M-:

https://www.gnu.org/software/emacs/manual/html_node/emacs/Lisp-Eval.html

use `a` in dired to visit without opening a new buffer
https://www.emacswiki.org/emacs/DiredReuseDirectoryBuffer#toc2

C-M s \ b w o r d \ b

C-M-Space M-w select word or s exp after point and put it in the kill ring

C-u before replace-string matches whole word

C-u M-| -- filter through command

find in multiple files: grep-find

#### replace in multiple files

find-dired, t or *t, Q, then Y replaces everywhere, C-s, ! saves everywhere

----

kill rectangle: C-x r k

----

kill buffer: C-x k
execute macro: C-x e

----

set bookmark:     C-x r m
jump to bookmark: C-x r b
list bookmarks:   C-x r l

mark and delete like in dired

----

insert literal character: C-q

`global-auto-revert-mode`: reload all files when they change

----

rename file:
  dired-jump
  R

font-lock-mode

replace-string

