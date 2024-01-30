# Slides for the defence of my Ph. D. thesis.
The `main.py` file contains the python code. In order to run it you will need [Manim-slides](https://eertmans.be/manim-slides/) and [Manim](https://www.manim.community/).

My code is not the best, it is my first project using Manim and it was intended to look pretty in the presentation only (insert Homer meme).
I decided to share it because I think it could be used as inspiration for somebody.

## The slides
There are several ways to see the presentation. 
1. Recomended: Download the selfcontained html file](https://github.com/luis-telesforo/phd_slides/blob/main/slides.html). Then open it in the comuter browser.
2. Clone the repository and run `manim-slides SimplicialComplexes PseudoesferaDefinicion Ejemplos Matroides PosetChrom Join GEspacios BorsukUlam Generaliza Portadores DC`
3. Download [this html file](https://github.com/luis-telesforo/phd_slides/blob/main/slides_not_unique.html) with its [assets](https://github.com/luis-telesforo/phd_slides/tree/main/slides_not_unique_assets). 
4. Download the [power point version](https://github.com/luis-telesforo/phd_slides/blob/main/slides.pptx).
5. Not recommended: Download [the pdf version](https://github.com/luis-telesforo/phd_slides/blob/main/slides.pdf) (it won't do the reverse animations)

## Things I think are useful
- The `main.py` file uses `config.background_color = WHITE` and the `construct` method of the `BlackSlide(Slide, Scene)` class allowed me to change the background color to white whereas all objects are black by default (so you do not need to change the color each time). This is useful for presentations using a projector. For computer presentations I will suggest the original black background.
- The `colors` (`ROSA`, `NARANJA`, `AZUL` and `VERDOSO`) are color blind friendly!

## The mathematical material
My thesis is basically the paper: Pseudospheres: combinatorics, topology and distributed systems. It will appear in the special issue on Topological Methods in Computer Science of the [Journal of Applied and Computational Topology](https://link.springer.com/journal/41468). Any comments on it are welcomed.
