import os
import leafmap
import streamlit as st
import streamlit.components.v1 as components
from bs4 import BeautifulSoup


DEFAULT_MAP_SPECS = dict(height=450, width=800)  # in px
DEFAULT_FILEPATH = "https://raw.githubusercontent.com/giswqs/leafmap/master/examples/data/us_cities.csv"
DEFAULT_ARTIFACT_PATH = './.artifacts'

APP_TITLE = 'Leafmap Streamlit App'

#@st.cache(suppress_st_warning=True)
def make_map_from_csv(filepath: str=None, height: int=450, width: int=800, zoom=4):

    if filepath is None:
        filepath = DEFAULT_FILEPATH
    m = leafmap.Map(
            tiles='stamentoner',
            google_map=None,
            height=f"{height}px",
            width=f"{width}px",
            zoom=4,
        )
    m.add_heatmap(
        filepath,
        latitude="latitude",
        longitude='longitude',
        value="pop_max",
        name="Heat map",
        radius=20,
    )
    return m

@st.cache
def save_map_to_html(m: leafmap.Map):
    map_html_path = os.path.join(DEFAULT_ARTIFACT_PATH, 'map.html')
    m.to_html(map_html_path)

@st.cache
def read_map_from_html(map_html_path: str = None) -> str:
    if map_html_path is None:
        map_html_path = os.path.join(DEFAULT_ARTIFACT_PATH, 'map.html')
    with open(map_html_path) as f:
        html_content = f.read()

#@st.cache(suppress_st_warning=True)
def app():

    st.set_page_config(layout="wide")
    st.title(APP_TITLE)


    filepath = st.text_input(
        label='CSV file url',
        value=DEFAULT_FILEPATH,
        help="URL to your csv file on github."
    )

    if not filepath:
        filepath = DEFAULT_FILEPATH
        st.warning(f'Invalid filepath provided. Loading default filepath: \n\t{DEFAULT_FILEPATH}')

    map_specs = DEFAULT_MAP_SPECS

    m = make_map_from_csv(filepath, **map_specs)
    html_content = m.to_html()

    soup = BeautifulSoup(html_content, 'html.parser')
    # body = soup.find('body')

    # Show map by loading html
    components.html(
        m.to_html(),
        width=map_specs['width'] * 2,
        height=map_specs['height'] * 1.5,
        scrolling=False)

    '### Generated html from the `leafmap.Map` object'

    st.write(
        ':bulb: This html was generated with the method: `leafmap.Map.to_html()`.')
    expander = st.beta_expander(
        label='HTML of leafmap.Map object', expanded=False)
    with expander:
        #st.markdown(m.to_html(), unsafe_allow_html=True)
        st.code(soup.prettify(), language='html')

if __name__ == "__main__":
    app()
