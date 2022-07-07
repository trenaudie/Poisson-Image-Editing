import eel
import poisson_image


eel.init("web")

source_image = ['web/images/requin2.jpg']
target_image = ['web/images/fond_marin2.jpeg']
algo = ['max']



@eel.expose
def source_shark():
    source_image[0] = 'web/images/requin2.jpg'
    print(source_image[0])

@eel.expose
def source_bird():
    source_image[0] = 'web/images/photo_oiseau.jpeg'

@eel.expose
def source_objets():
    source_image[0] = 'web/images/objects.jpeg'

@eel.expose
def source_statue():
    source_image[0] = 'web/images/statueLiberte.jpeg'

@eel.expose
def target_ocean():
    target_image[0] = 'web/images/fond_marin2.jpeg'


@eel.expose
def target_sky():
    target_image[0] = 'web/images/fond_ciel.jpeg'
    print(target_image[0])

@eel.expose
def target_forest():
    target_image[0] = 'web/images/imageforêt.jpeg'

@eel.expose
def run():
    poisson_image.solve_derivatives_max(source_image[0], target_image[0])

eel.start("index.html")