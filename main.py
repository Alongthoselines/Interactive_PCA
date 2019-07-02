import bokeh
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import d3
import pandas as pd

DATA_SOURCE = './DATA/PCA_ASW_YRI'
COLUMN_NAMES = ['IDS', 'PC1','PC2', 'population']
OUTPUT_FILE_NAME = 'PCA_on_ASW_YRI.html'
PLOT_TITLE = 'PCA On ASW YRI'


data=pd.read_csv(DATA_SOURCE, sep = '\t')
data.columns = COLUMN_NAMES
output_file(OUTPUT_FILE_NAME)

TOOLTIPS = [("index", "$index"),("(x,y)", "($x, $y)"), ("name","@IDS")]


#Potentialy more colors have to be provided, this depends on the number of categories being plotted
palette = d3['Category10'][5][3:]


p = figure(plot_width=800, plot_height=800, tooltips=TOOLTIPS,
           title=PLOT_TITLE)

color_map = bokeh.models.CategoricalColorMapper(factors=data['population'].unique(),palette=palette)

for idx,i in enumerate(data['population'].unique()):
    df = data[data['population']== i]
    source = ColumnDataSource(data=df)
    p.circle(x='PC1',y='PC2',color=palette[idx],source=source, legend = i)

p.legend.location = "top_left"
p.legend.click_policy="hide"

show(p)
