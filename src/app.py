
import pickle
import streamlit as st
import requests


# OMDb API configuration
OMDB_API_KEY = "264e88b7"

def truncate_text(text, max_length=20):
    """Truncate text to fit within the poster width"""
    if len(text) > max_length:
        return text[:max_length-3] + "..."
    return text

def fetch_poster(movie_title):
    try:
        url = f"http://www.omdbapi.com/?t={requests.utils.quote(movie_title)}&apikey={OMDB_API_KEY}"
        response = requests.get(url, timeout=10)
        data = response.json()

        if data.get("Response") == "True" and data.get("Poster") != "N/A":
            return data.get("Poster")
        return "https://via.placeholder.com/500x750?text=No+Image"

    except requests.exceptions.RequestException:
        return "https://via.placeholder.com/500x750?text=Error"
 

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances=sorted(list(enumerate(similarity[index])), reverse=True , key=lambda x:x[1])
    recommended_movies_names = []
    recommended_movies_posters = []
    for i in distances[1:6]:
        movie_title = movies.iloc[i[0]].title
        recommended_movies_posters.append(fetch_poster(movie_title))
        recommended_movies_names.append(movie_title)
    return recommended_movies_names, recommended_movies_posters


st.header("Movie Recommender System")
movies = pickle.load(open("artifacts/movie_list.pkl" , 'rb'))
similarity = pickle.load(open("artifacts/similarity.pkl" , 'rb'))

movie_list = movies['title'].values
selected_movie=st.selectbox("Type or select a movie from the dropdown" , movie_list)

if st.button('show_recommendation'):
    recommended_movies_names, recommended_movies_posters = recommend(selected_movie)
    
    # First row - 5 movies
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movies_posters[0])
        st.caption(truncate_text(recommended_movies_names[0]))
    with col2:
        st.image(recommended_movies_posters[1])
        st.caption(truncate_text(recommended_movies_names[1])) 
    with col3:
        st.image(recommended_movies_posters[2])
        st.caption(truncate_text(recommended_movies_names[2]))
    with col4:
        st.image(recommended_movies_posters[3])
        st.caption(truncate_text(recommended_movies_names[3]))
    with col5:
        st.image(recommended_movies_posters[4])
        st.caption(truncate_text(recommended_movies_names[4]))
    

