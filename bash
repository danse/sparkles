##### Array variable

    $ s=( 4880101 4880104 4882008 4898984 4868689 )
    $ for n in ${s[@]}; do mamd.vodafone.it"$n" restart; done

##### Array, direct use

    for s in a b c; do echo $s; done

#### Generate a sequence

```
#!/bin/bash
for i in {1..5}
do
   echo "Welcome $i times"
done
```

#### Exclude pattern

    ls !(dir)
    