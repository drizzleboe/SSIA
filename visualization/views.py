from django.shortcuts import render
import pandas as pd
from bokeh.io import output_notebook
output_notebook()
bokeh_width, bokeh_height = 500,400
# Create your views here.
from bokeh.embed import components
from bokeh.io import show
from bokeh.plotting import gmap
from bokeh.models import GMapOptions

def plot(lat, lng, zoom=10, map_type='roadmap'):
    gmap_options = GMapOptions(lat=lat, lng=lng, 
                               map_type=map_type, zoom=zoom)
    p = gmap(api_key, gmap_options, title='Pays de Gex', 
             width=bokeh_width, height=bokeh_height)
    show(p)
    return p

df = pd.read_csv('/home/drizzle/Downloads/dvf_gex.csv')
lat, lon = 46.2437, 6.0251
api_key = 'AIzaSyBu0z9o7Jz6-zxbXBUzaMsKC9vDL0fImdE'


def index(request):

    plot(lat, lon)
 
    # add a circle renderer with a size, color, and alpha
 
    
 
    script, div = components(plot)
 

    return render(request, 'visualization/index.html', {
        'script': script, 
        'div': div
        })