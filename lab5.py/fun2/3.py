
import data

def avMovie(arg):
    sum = 0
    for i in range(len(arg)):
        for key in arg[i]:
            if key == "imdb":
                sum += arg[i][key]
    print(sum/len(arg))
    
avMovie(data.movies)
    