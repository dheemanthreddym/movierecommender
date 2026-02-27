import pickle
import streamlit as st
import requests


def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        response = requests.get(url, timeout=5)
        data = response.json()

        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        return "https://via.placeholder.com/500x750?text=No+Image"

    except requests.exceptions.RequestException:
        return "https://via.placeholder.com/500x750?text=Error"
 

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances=sorted(list(enumerate(similarity[index])), reverse=True , key=lambda x:x[1])
    recommended_movies_names = []
    recommended_movies_posters = []
    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_names.append(movies.iloc[i[0]].title)
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
        st.text(recommended_movies_names[0])
        st.image(recommended_movies_posters[0])
    with col2:
        st.text(recommended_movies_names[1])
        st.image(recommended_movies_posters[1]) 
    with col3:
        st.text(recommended_movies_names[2])
        st.image(recommended_movies_posters[2])
    with col4:
        st.text(recommended_movies_names[3])
        st.image(recommended_movies_posters[3])
    with col5:
        st.text(recommended_movies_names[4])
        st.image(recommended_movies_posters[4])
    
    # Second row - 5 more movies
    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.text(recommended_movies_names[5])
        st.image(recommended_movies_posters[5])
    with col7:
        st.text(recommended_movies_names[6])
        st.image(recommended_movies_posters[6])
    with col8:
        st.text(recommended_movies_names[7])
        st.image(recommended_movies_posters[7])
    with col9:
        st.text(recommended_movies_names[8])
        st.image(recommended_movies_posters[8])
    with col10:
        st.text(recommended_movies_names[9])
        st.image(recommended_movies_posters[9])
    

