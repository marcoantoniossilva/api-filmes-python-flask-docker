from flask import Flask, Response, request
import json

VERSION = "1.0"

SERVICE_NAME = "Recomendações"

RECOMMENDATIONS_DATA = "/data/recommendations.json"

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

@service.get('/recommendations')
def get_movies():
    success, recommendations = False, "{}"

    try:
        with open(RECOMMENDATIONS_DATA, "r") as file:
            content = json.load(file)
            recommendations = content["recommendations"]
            success = True
    except Exception as e:
        print(f"Ocorreu um erro acessando {SERVICE_NAME}: {str(e)}")

    return Response(json.dumps(recommendations) if recommendations is not None else recommendations, status = 200 if success else 204, mimetype = "application/json")

@service.get('/recommendations/<int:movie_id>')
def get_recommendations_by_movie(movie_id):
    success, filtered_recommendations = False, []

    try:
        with open(RECOMMENDATIONS_DATA, "r") as file:
            content = json.load(file)
            all_recommendations = content.get("recommendations", [])

            filtered_recommendations = [recommendation for recommendation in all_recommendations if recommendation.get("movie_id") == movie_id]
            success = True
    except Exception as e:
        print(f"Ocorreu um erro acessando {SERVICE_NAME}: {str(e)}")

    return Response(json.dumps(filtered_recommendations), status=200 if success else 204, mimetype="application/json")

@service.post('/recommendations')
def add_recommendation():

    success = False

    try:
        new_recommendation = request.get_json()

        with open(RECOMMENDATIONS_DATA, "r") as file:
            content = json.load(file)

        content["recommendations"].append(new_recommendation)

        with open(RECOMMENDATIONS_DATA, "w") as file:
            json.dump(content, file, indent=4)

        success = True

    except Exception as e:
        print(f"Ocorreu um erro ao adicionar uma {SERVICE_NAME}: {str(e)}")

    return Response(status = 201 if success else 422) 

if __name__ == "__main__":
    service.run(host="0.0.0.0", debug=True)