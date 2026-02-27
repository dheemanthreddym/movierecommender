# Movie Recommender System

A Streamlit-based movie recommendation application that suggests movies based on user preferences using collaborative filtering and content-based similarity.

## Features

- **Movie Recommendations**: Get personalized movie suggestions based on your favorite movies
- **Interactive Web Interface**: Built with Streamlit for easy user interaction
- **TMDB Dataset**: Uses The Movie Database (TMDB) 5000 movies dataset
- **Similarity Matching**: Employs cosine similarity for finding similar movies
- **Fast Search**: Quick movie lookup and recommendation generation

## Dataset

The application uses the TMDB 5000 dataset containing:
- `tmdb_5000_movies.csv`: Movie metadata including titles, genres, keywords, etc.
- `tmdb_5000_credits.csv`: Cast and crew information for movies

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd movie_recommender
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run src/app.py
```

## Usage

1. Open your browser and navigate to the Streamlit app URL (usually `http://localhost:8501`)
2. Select a movie from the dropdown menu
3. Click "Recommend" to get similar movie suggestions
4. View the recommended movies with their posters, ratings, and overviews

## Project Structure

```
movie_recommender/
├── data/
│   ├── tmdb_5000_credits.csv
│   └── tmdb_5000_movies.csv
├── artifacts/
│   ├── movie_list.pkl
│   └── similarity.pkl
├── src/
│   ├── app.py              # Main Streamlit application
│   ├── app_backup.py       # Backup version
│   └── __init__.py
├── Recommender system.ipynb  # Jupyter notebook for model development
├── requirements.txt          # Python dependencies
├── setup.py                  # Package setup
├── README.MD                 # This file
└── .gitignore               # Git ignore rules
```

## Model Training

The recommendation model is trained using:
- **Content-based filtering**: Analyzes movie features like genres, keywords, cast, and crew
- **Cosine similarity**: Measures similarity between movies
- Preprocessed data is saved as pickle files in the `artifacts/` directory

## Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning algorithms
- **Pickle**: Model serialization

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- TMDB (The Movie Database) for providing the movie dataset
- Streamlit community for the excellent web app framework
