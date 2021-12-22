
 pattern rules:

%.o : %.c ; recipe…

https://www.gnu.org/software/make/manual/make.html#Pattern-Intro

a pattern rule like:

output/%.rst:input/%.docx
	pandoc $< -o $@

is activated only when the targets are specified explicitly via `$
make output/*` for example, otherwise make does not see targets. there
is probably a way to define the desired group of targets. see also
https://unix.stackexchange.com/questions/140912/no-target-error-using-make

 automatic variables:

$@ target
$< first prerequisite
$^ all prerequisites without duplicates

http://www.gnu.org/software/make/manual/make.html#Automatic-Variables
