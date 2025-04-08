from flask import Flask, Response, request
import json

VERSION = "1.0"

SERVICE_NAME = "Comentários"

COMMENTS_DATA = "/data/comments.json"

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

@service.get('/comments')
def get_movies():
    success, comments = False, "{}"

    try:
        with open(COMMENTS_DATA, "r") as file:
            content = json.load(file)
            comments = content["comments"]
            success = True
    except Exception as e:
        print(f"Ocorreu um erro acessando {SERVICE_NAME}: {str(e)}")

    return Response(json.dumps(comments) if comments is not None else comments, status = 200 if success else 204, mimetype = "application/json")

@service.get('/comments/<int:movie_id>')
def get_comments_by_movie(movie_id):
    success, filtered_comments = False, []

    try:
        with open(COMMENTS_DATA, "r") as file:
            content = json.load(file)
            all_comments = content.get("comments", [])

            filtered_comments = [comment for comment in all_comments if comment.get("movie_id") == movie_id]
            success = True
    except Exception as e:
        print(f"Ocorreu um erro acessando {SERVICE_NAME}: {str(e)}")

    return Response(json.dumps(filtered_comments), status=200 if success else 204, mimetype="application/json")


@service.post('/comments')
def add_comment():

    success = False

    try:
        new_comment = request.get_json()

        with open(COMMENTS_DATA, "r") as file:
            content = json.load(file)

        content["comments"].append(new_comment)

        with open(COMMENTS_DATA, "w") as file:
            json.dump(content, file, indent=4)

        success = True

    except Exception as e:
        print(f"Ocorreu um erro ao adicionar um {SERVICE_NAME}: {str(e)}")

    return Response(status = 201 if success else 422) 

if __name__ == "__main__":
    service.run(host="0.0.0.0", debug=True)