def catMovie(arg, x):
    for i in range(len(arg)):
        name = arg[i]['name']
        for key in arg[i]:
            if key == "category" and arg[i][key] == x:
                print(f"Movie: {name}\t\t category: {arg[i][key]}")

x = input("Input category name: ")

