import eel
import poisson_image

eel.init("web")

# Exposing the random_python function to javascript
source_image = ['figs/requin2.jpeg']

@eel.expose
def sourceshark():
    print("Random function running")
    source_image[0] = 'figs/requins.jpeg'
    print(source_image[0])


@eel.expose
def f():
    poisson_image.solve_derivatives_max()


eel.start("index.html")