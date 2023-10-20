def MoviesCategory(n): 
    for i in movies: 
        if i["name"]==n and i["imdb"]>5.5: 
            return True 
    return False 

