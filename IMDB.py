#sheriyenna

import requests
from info import API_KEY

user = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57"}

def get_movie_info(query):    
    try:
       url = f'http://www.omdbapi.com/?apikey={API_KEY}&t={query}'
       resp = requests.get(url, headers=user).json()
       poster=resp['Poster']
       id=resp['imdbID']
       text=f"""π π³ππππΎ : <b><u>{resp['Title']}</u></b>
                            
β±οΈ π±ππππππΎ : <b>{resp['Runtime']}</b>
π π±πΊππππ : <b>{resp['imdbRating']}/10</b>
π³οΈ π΅πππΎπ : <b>{resp['imdbVotes']}</b>

π π±πΎππΎπΊππΎ : <b>{resp['Released']}</b>
π­ π¦πΎπππΎ : <b>{resp['Genre']}</b>
π π«πΊππππΊππΎ : <b>{resp['Language']}</b>
π π’ππππππ : <b>{resp['Country']}</b>

π₯ π£πππΎπΌππππ : <b>{resp['Director']}</b>
π πΆππππΎππ : <b>{resp['Writer']}</b>
π π²ππΊππ : <b>{resp['Actors']}</b>

π π―πππ : <code>{resp['Plot']}</code>

<b>powered by: @Subhan011 β</b>"""

    except Exception as error:
        print(error)
    return poster, id, text
         
