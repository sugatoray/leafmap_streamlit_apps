import os
import inspect
import leafmap
import streamlit as st
import streamlit.components.v1 as components
from dotenv import dotenv_values

CONFIG = {
    **dotenv_values(".secrets/.env.shared"),  # load shared development variables
    **dotenv_values(".secrets/.env.secret"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}

DEFAULT_MAP_SPECS = dict(height=450, width=600)  # in px
APP_TITLE = 'Leafmap Streamlit App - *Adding Layers*'
LEAFMAP_TILES = [x for x, _ in inspect.getmembers(
    leafmap, predicate=inspect.isfunction) if x.endswith('tiles')]
LOGO = "https://icons.iconarchive.com/icons/paomedia/small-n-flat/1024/layers-icon.png"
DEFAULT_TILES = "basemap_xyz_tiles"


#@st.cache(suppress_st_warning=True)
def add_title(uselogo: bool = True, logowidth: str='50px'):
    col1, col2 = st.beta_columns(2)
    with col1:
        st.write(f'# {APP_TITLE}')
    with col2:
        if uselogo:
            st.markdown(
                f'<img src="{LOGO}" width="{logowidth}"/>',
                unsafe_allow_html=True,
            )

def app(wide_layout: bool=False):

    if wide_layout:
        layout = 'wide'
    st.set_page_config(layout=layout, page_icon=LOGO, page_title=APP_TITLE)

    add_title(uselogo=True, logowidth='50px')

    map_specs = DEFAULT_MAP_SPECS

    # for k, v in CONFIG.items():
    #     st.write(f"- `{k}`\t\t: \t{v}")
    os.environ["PLANET_API_KEY"] = CONFIG.get("PLANET_API_KEY")

    m = leafmap.Map(center=[38.2659, -103.2447], zoom=13,
                    height=f"{map_specs['height']}px",
                    width=f"{map_specs['width']}px")

    tiles = dict()
    available_tiles = LEAFMAP_TILES
    with st.sidebar:
        tiles['type'] = st.radio(
            label='Layers',
            options=available_tiles,
            index=available_tiles.index(DEFAULT_TILES),
        )

    expander = st.beta_expander('List of Leafmap Tiles:', expanded=False)
    with expander:
        st.write(available_tiles)

    # add time slider
    layers_dict = dict()
    if tiles.get('type'):
        apply_tiles = getattr(leafmap, tiles.get('type'))
        layers_dict = apply_tiles()

    if layers_dict:
        m.add_time_slider(layers_dict, time_interval=1)

    # Show map by loading html
    components.html(
        m.to_html(),
        width=map_specs['width'] * 2,
        height=map_specs['height'] * 1.5,
        scrolling=False)

    st.info('''
    :bulb: **Note**: If you are trying to use one of the
    latest features in *leafmap*, you could run
    **`leafmap.update_package()`** once to update the package.
    ''')

if __name__ == "__main__":
    app(wide_layout=True)
