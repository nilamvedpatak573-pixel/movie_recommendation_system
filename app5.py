import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)
# Background colour theme

st.markdown(
    """
    <style>
    .stApp {
        background-color: #120024;
    }

    /* Main heading color */
    h1 {
        color: #ffffff;
    }

    /* Caption styling */
    .stCaption {
        color: #d8b4fe;
    }

    /* Button styling */
    .stButton button {
        background-color: #7c3aed;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 8px 20px;
        font-size: 16px;
    }

    .stButton button:hover {
        background-color: #a855f7;
        color: white;
    }

    /* Poster size and design */
    .stImage img {
        height: 300px;
        width: 200px;
        object-fit: cover;
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <h1 style='
        text-align: center;
        font-size: 25px;
        color: white;
    '>
        🎬 Movie Recommendation System
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='
        text-align: center;
        font-size: 18px;
        color: #d8b4fe;
    '>
        Discover your next favourite movie using NLP
    </p>
    """,
    unsafe_allow_html=True
)



df = pd.read_csv("cleaned_data.csv")

with open("similarity.pkl", "rb") as file:
    similarity = pickle.load(file)

with open("indices.pkl", "rb") as file:
    indices = pickle.load(file)


df = pd.read_csv("cleaned_data.csv")
def recommend(movie):
    index = df[df["title"] == movie].index[0]

    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    recommended = []

    for i in distances[1:6]:
        recommended.append(df.iloc[i[0]].title)

    return recommended

tab1, tab2, tab3 = st.tabs([
    "📖 About",
    "🎬 Find Movies",
    "🔥 Popular Movies"
])

with tab1:

    st.write("""
    Welcome to the **Movie Recommendation System**!

    This application recommends movies similar to your favourite movie
    using **Natural Language Processing (NLP)** and **Cosine Similarity**.

    **Technologies Used**
    - Python
    - Pandas
    - Scikit-learn
    - Streamlit
    - NLP
    """)


# ======================= FIND MOVIES TAB =======================

with tab2:

    selected_movie = st.selectbox(
        "🎬 Select a Movie",
        sorted(df["title"].unique())
    )

    if st.button("🍿 Find Similar Movies"):

        recommendations = recommend(selected_movie)

        st.success("⭐ Recommended Movies")

        cols = st.columns(5)

        for col, movie in zip(cols, recommendations):

            file_name = movie.lower().replace(" ", "").replace("&", "").replace("-", "")

            poster_path = f"posters/{file_name}.jpg"

            with col:

                if os.path.exists(poster_path):

                    st.image(
                        poster_path,
                        caption=movie,
                        use_container_width=True
                    )

                else:

                    st.write(movie)


# ======================= POPULAR MOVIES TAB =======================

with tab3:

    top_movies = [
        ("10thwolf", "10th & Wolf"),
        ("anotherearth", "Another Earth"),
        ("stevejobs", "Steve Jobs"),
        ("supermanreturn", "Superman Return")
    ]

    cols = st.columns(len(top_movies))

    for col, (file_name, display_name) in zip(cols, top_movies):

        with col:

            st.image(
                f"posters/{file_name}.jpg",
                caption=display_name,
                use_container_width=True
            )






