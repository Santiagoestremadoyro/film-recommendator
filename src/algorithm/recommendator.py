from database import connection
import requests
import os

class recommend_film:
         def __init__(self, api_key, base_url):
              self.api_key = api_key
              self.base_url = base_url
              self.params = {"api_key": self.api_key}

         def recommendation(self):
              try:
                   #coneccion a la BD
                   conn = connection.Database(os.getenv("DB_URI"), os.getenv("DB_NAME", os.getenv("DB_COLL")))

                   #solicitar input del usuario
                   user_input = input("Ingrese los titulos de sus 3 peliculas preferidas: "), input("2 pelicula preferida"), input("3 pelicula preferida")

                   #obtener titulo de la pelicula 
                   user_movie = conn.find({"title": user_input})
                   year = []
                   director = []
                   for movie in user_movie:
                        year.append(movie.get('year'))
                        director.append(movie.get('director'))
                   #realizar una query para encontrar peliculas similares en BD 
                   query = {
                        "$and":[
                             {"director": director},
                             {"year" : year}
                        ]
                   }
                   similar_movies = conn.find(query)

                   #mostrar resultados al usuario 
                   if similar_movies:
                        print("=====================Peliculas Recomendadas====================")
                        for movie in similar_movies:
                             print(movie["title"])
                   else:
                        print("No se ah encontrado ninguna pelicula de su interes en nuestra coleccion")
              except Exception as e:
                   print(f"Error ocasionado por: {e}")