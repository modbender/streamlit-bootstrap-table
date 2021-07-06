# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st

import numpy as np
import pandas as pd
import streamlit
import streamlit.components.v1 as components


def common():
    st.markdown(
        '''
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <script>
            console.log("Does this work");
        </script>
        ''',
        unsafe_allow_html=True,
    )
    st.title("Project Landing")


def sidebar():
    sb_options = ("Select Version", "Version1", "Version2")
    sb_value = st.sidebar.selectbox(
        "Dashboard",
        sb_options
    )


def run_tabs():
    tabs = ["Tab1", "Tab2"]
    active_tab = tabs[0]

    header_buttons = "".join(
        f"""
        <button class="nav-link{' active' if t == active_tab else ''}" id="nav-{t}-tab" data-bs-toggle="tab" data-bs-target="#nav-{t}" type="button" role="tab" aria-controls="nav-{t}" aria-selected="true">
            {t}
        </button>
        """.strip()
        for t in tabs
    )
    tab_header_html = f"""
    <nav>
        <div class="nav nav-tabs" id="nav-homeTab" role="tablist">
            {header_buttons}
        </div>
    </nav>
    """.strip()
    st.markdown(tab_header_html, unsafe_allow_html=True)

    tab_contents = [
        pd.DataFrame(
            np.random.randn(10, 5), columns=('col %d' % i for i in range(5))
        ),
        pd.DataFrame(
            np.random.randn(10, 5), columns=('col %d' % i for i in range(5))
        ),
        pd.DataFrame(
            np.random.randn(10, 5), columns=('col %d' % i for i in range(5))
        )
    ]
    tab_contents_html = "".join(
        f"""
        <div class="tab-pane fade show{' active' if t == active_tab else ''}" id="nav-{t}" role="tabpanel" aria-labelledby="nav-{t}-tab">        
        {tab_contents[i].to_html()}
        </div>
        """.strip()
        for (i, t) in enumerate(tabs)
    )
    tab_contents_html = f"""
    <div class="tab-content" id="nav-homeTabContent">{tab_contents_html}</div>
    """
    st.markdown(tab_contents_html, unsafe_allow_html=True)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    common()
    run_tabs()
    sidebar()
