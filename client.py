import urllib.request as requisition
import json
from datetime import datetime
from time import sleep

MOVIES_SERVER_URL = "http://localhost:5001"
MOVIES_ALIVE_URL = f"{MOVIES_SERVER_URL}/alive"
MOVIES_API_URL = f"{MOVIES_SERVER_URL}/movies"

COMMENTS_SERVER_URL = "http://localhost:5002"
COMMENTS_ALIVE_URL = f"{COMMENTS_SERVER_URL}/alive"
COMMENTS_API_URL = f"{COMMENTS_SERVER_URL}/comments"

RECOMMENDATIONS_SERVER_URL = "http://localhost:5003"
RECOMMENDATIONS_ALIVE_URL = f"{RECOMMENDATIONS_SERVER_URL}/alive"
RECOMMENDATIONS_API_URL = f"{RECOMMENDATIONS_SERVER_URL}/recommendations"

def access(url):
    success, content = False, []

    try:
        response = requisition.urlopen(url)

        if response.code == 200:
            content = response.read().decode('utf-8')
            success = True

    except Exception as e:
        print(f"Ocorreu um erro acessando a URL: {url}")
    
    return success, content

def access_with_param(base_url, param):
    success, content = False, []

    url = f"{base_url}/{param}"

    try:
        response = requisition.urlopen(url)

        if response.code == 200:
            content = response.read().decode('utf-8')
            success = True

    except Exception as e:
        print(f"Ocorreu um erro acessando a URL: {url}")
    
    return success, content


def get_movies():
    success, movies = access(MOVIES_API_URL)
    if success:
        movies = json.loads(movies)
        success = success and bool(movies)
    
    return success, movies

def get_comments(movie_id):
    comments = None
    if is_alive(COMMENTS_ALIVE_URL):
            success, comments = access_with_param(COMMENTS_API_URL, movie_id)
            if success == False:
                print(f'Não existem Comentários')
    else:
        print(f'O Serviço de Comentários não está disponível')
    return json.loads(comments) if comments is not None else []

def get_recommendations(movie_id):
    movie_recommendations = []
    if is_alive(RECOMMENDATIONS_ALIVE_URL):
            success, recommendations = access_with_param(RECOMMENDATIONS_API_URL, movie_id)
            if success:
                recommendations = json.loads(recommendations)
                for recommendation in recommendations:
                    success, movies = access_with_param(MOVIES_API_URL, recommendation["recomendation_movie_id"])
                    if success:
                        movies = json.loads(movies)
                        for movie in movies:
                            movie_recommendations.append(movie["title"])
            else:
                print(f'Não existem Recomendações')
    else:
        print(f'O Serviço de Recomendações não está disponível')
    return movie_recommendations if bool(movie_recommendations) else []

def print_movie(movie, comments, recommendations):
    print(f"Filme: {movie.get('title')}")
    print(f"Gênero: {movie.get('genre')}")
    print(f"Elenco:")
    for actor in movie.get('cast'):
        print(f"        {actor}")
    print(f"Ano: {movie.get('year')}")
    print(f"Diretor: {movie.get('director')}")
    print(f"Sinopse: {movie.get('synopsis')}")
    print(f"Comentários:")
    for comment in comments:
        print(f"        Autor: {comment.get('user_name')}")
        print(f"        Data: {datetime.strptime(comment.get('date'), "%Y-%m-%d").strftime("%d/%m/%Y")}")
        print(f"        Comentário: {comment.get('comment')}\n")
    print(f"Recomendações:")
    for recommendation in recommendations:
        print(f"        {recommendation}")
    print("==========================================================================\n")

def is_alive(url):
    success, alive = access(url)

    return success and alive == "sim"


if __name__ == "__main__":
    while True:
        if is_alive(MOVIES_ALIVE_URL):
            success, movies = get_movies()
            if success:
                for movie in movies:
                    print_movie(
                        movie,
                        get_comments(movie.get("id")),
                        get_recommendations(movie.get("id"))
                    )
            else:
                print(f'Não existem Filmes')

        else:
            print(f'O Serviço de Filmes não está disponível')
            
        sleep(3)