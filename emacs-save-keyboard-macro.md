
### 17.5 Naming and Saving Keyboard Macros {#naming-and-saving-keyboard-macros .section}

C-x C-k n
:   Give a command name (for the duration of the Emacs session) to the
    most recently defined keyboard macro (`kmacro-name-last-macro`).\

C-x C-k b
:   Bind the most recently defined keyboard macro to a key sequence (for
    the duration of the session) (`kmacro-bind-to-key`).\

M-x insert-kbd-macro
:   Insert in the buffer a keyboard macro\'s definition, as Lisp code.

[]{#index-saving-keyboard-macros-1137}[]{#index-kmacro_002dname_002dlast_002dmacro-1138}[]{#index-C_002dx-C_002dk-n-1139}
If you wish to save a keyboard macro for later use, you can give it a
name using C-x C-k n (`kmacro-name-last-macro`). This reads a name as an
argument using the minibuffer and defines that name to execute the last
keyboard macro, in its current form. (If you later add to the definition
of this macro, that does not alter the name\'s definition as a macro.)
The macro name is a Lisp symbol, and defining it in this way makes it a
valid command name for calling with M-x or for binding a key to with
`global-set-key` (see [Keymaps](Keymaps.html#Keymaps)). If you specify a
name that has a prior definition other than a keyboard macro, an error
message is shown and nothing is changed.

[]{#index-binding-keyboard-macros-1140}[]{#index-kmacro_002dbind_002dto_002dkey-1141}[]{#index-C_002dx-C_002dk-b-1142}
You can also bind the last keyboard macro (in its current form) to a
key, using C-x C-k b (`kmacro-bind-to-key`) followed by the key sequence
you want to bind. You can bind to any key sequence in the global keymap,
but since most key sequences already have other bindings, you should
select the key sequence carefully. If you try to bind to a key sequence
with an existing binding (in any keymap), this command asks you for
confirmation before replacing the existing binding.

To avoid problems caused by overriding existing bindings, the key
sequences C-x C-k 0 through C-x C-k 9 and C-x C-k A through C-x C-k Z
are reserved for your own keyboard macro bindings. In fact, to bind to
one of these key sequences, you only need to type the digit or letter
rather than the whole key sequences. For example,

``` {.example}
     C-x C-k b 4
```

will bind the last keyboard macro to the key sequence C-x C-k 4.

[]{#index-insert_002dkbd_002dmacro-1143} Once a macro has a command
name, you can save its definition in a file. Then it can be used in
another editing session. First, visit the file you want to save the
definition in. Then use this command:

``` {.example}
     M-x insert-kbd-macro <RET> macroname <RET>
```

This inserts some Lisp code that, when executed later, will define the
same macro with the same definition it has now. (You don\'t need to
understand Lisp code to do this, because `insert-kbd-macro` writes the
Lisp code for you.) Then save the file. You can load the file later with
`load-file` (see [Lisp Libraries](Lisp-Libraries.html#Lisp-Libraries)).
If the file you save in is your init file [\~/.emacs]{.file} (see [Init
File](Init-File.html#Init-File)) then the macro will be defined each
time you run Emacs.

If you give `insert-kbd-macro` a numeric argument, it makes additional
Lisp code to record the keys (if any) that you have bound to macroname,
so that the macro will be reassigned the same keys when you load the
file.
