import streamlit as st
import pickle
import pandas as pd

def recommend(df,name,similar):
    spot = df[df['title'] == name].index[0]
    similarity_scores = list(enumerate(similar[spot]))
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)[1:6]
    recommendations = []
    for i in sorted_scores:
        st.write(df.iloc[i[0]].title,'\n')

movies_list = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_list)

similar = pickle.load(open('similar.pkl','rb'))

st.title('Movie Recommendation System')

option = st.selectbox(
    'Which Movie would like to watch?',
    movies['title'].values)

if st.button('Recommend'):
    recommend(movies,option,similar)
    # st.write('hello')