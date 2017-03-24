For my streamgraph, i get the viewport size and map it to the SVG
viewbox sizes, which are also used for the range of the scales. This
is not responsive, but it works well. No width is set to the SVG
element, which fits the whole viewport automatically

Something that is not very intuitive, is that setting a viewbox on the
SVG makes it expand to the full width of the viewport, while its
height will be determined depending on the width, keeping the
proportions as they are defined in the viewbox. Also the sizes of the
viewbox will determine how internal elements will fit the SVG. So the
viewbox sizes need to be set in a way that:

- They have the same proportions as the viewport
- They use the same values used by the internal elements in a visualisation

So for example if i have a screen that is wide 1000px and heigh 500px,
i want to set a viewBox with sizes 1000 and 500, and the rages of
scales in my vis will have to be 1000 and 500. That would also work
with 10 and 5 or 2 and 1, though
