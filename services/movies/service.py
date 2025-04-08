from flask import Flask, Response, request
import json

VERSION = "1.0"

SERVICE_NAME = "Filmes"

MOVIES_DATA = "/data/movies.json"

INFO = {
    "descricao" : f"Serviço que disponibiliza informações sobre {SERVICE_NAME}",
    "autor" : "Marco Antonio Santos Silva",
    "versao" : VERSION
}

ALIVE = "sim"

service = Flask(SERVICE_NAME)

@service.get('/')
def get():
    return get_info()

@service.get('/info')
def get_info():
    return Response(json.dumps(INFO), status = 200, mimetype = "application/json")

@service.get('/alive')
def is_alive():
    return Response(ALIVE, status = 200, mimetype = "text/plain")

@service.get('/movies')
def get_movies():
    success, movies = False, "{}"

    try:
        with open(MOVIES_DATA, "r") as file:
            content = json.load(file)
            movies = content["movies"]
            success = True
    except Exception as e:
        print(f"Ocorreu um erro acessando {SERVICE_NAME}: {str(e)}")

    return Response(json.dumps(movies) if movies is not None else movies, status = 200 if success else 204, mimetype = "application/json")

@service.get('/movies/<int:movie_id>')
def get_movie_by_movie(movie_id):
    success, filtered_movie = False, None

    try:
        with open(MOVIES_DATA, "r") as file:
            content = json.load(file)
            all_movies = content.get("movies", [])

            filtered_movie = [movie for movie in all_movies if movie.get("id") == movie_id]
            success = True
    except Exception as e:
        print(f"Ocorreu um erro acessando {SERVICE_NAME}: {str(e)}")

    return Response(json.dumps(filtered_movie), status=200 if success else 204, mimetype="application/json")

@service.post('/movies')
def add_movie():

    success = False

    try:
        new_movie = request.get_json()

        with open(MOVIES_DATA, "r") as file:
            content = json.load(file)

        content["movies"].append(new_movie)

        with open(MOVIES_DATA, "w") as file:
            json.dump(content, file, indent=4)

        success = True

    except Exception as e:
        print(f"Ocorreu um erro ao adicionar um {SERVICE_NAME}: {str(e)}")

    return Response(status = 201 if success else 422) 

if __name__ == "__main__":
    service.run(host="0.0.0.0", debug=True)