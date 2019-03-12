# NO IMPORTS ALLOWED!

import json

def did_x_and_y_act_together(data, actor_id_1, actor_id_2):
    for movie in data:
        if actor_id_1 in movie and actor_id_2 in movie:
            return True
    return False

def who_did_x_act_with(data, actor_id):
    actors = set()
    for movie in data:
        if  actor_id == movie[1] and actor_id != movie[0]:
            actors.add(movie[0])
        elif actor_id == movie[0] and actor_id != movie[1]:
            actors.add(movie[1])
    return actors

def get_actors_with_bacon_number(data, n):
    numbers = {0:{4724}}

    for i in range(n):
        numbers[i+1] = set()

        for movie in data:
            if movie[0] in numbers[i]:

                add = True
                for itemp in range(i + 1):
                    if movie[1] in numbers[itemp]:
                        add = False
                if add:
                    numbers[i+1].add(movie[1])

            elif movie[1] in numbers[i]:
                add = True
                for itemp in range(i + 1):
                    if movie[0] in numbers[itemp]:
                        add = False
                if add:
                    numbers[i+1].add(movie[0])
        if len(numbers[i+1]) == 0:
            return set()

    return numbers[n]

def get_actor_bacon_number(data, actor,ref=4724):
    numbers = {0:{ref}}
    n = 0
    while True:
        numbers[n+1] = set()
        for movie in data:
            if movie[0] in numbers[n]:

                add = True
                for itemp in range(n + 1):
                    if movie[1] in numbers[itemp]:
                        add = False
                if add:
                    numbers[n+1].add(movie[1])

            elif movie[1] in numbers[n]:
                add = True
                for itemp in range(n + 1):
                    if movie[0] in numbers[itemp]:
                        add = False
                if add:
                    numbers[n+1].add(movie[0])
            if actor in numbers[n+1]:
                return numbers
        if len(numbers[n+1]) == 0:
            return None
        n += 1

    return numbers

def get_bacon_path(data, actor_id):
    numbers = get_actor_bacon_number(data,actor_id)
    if not numbers:
        return None
    path = [actor_id]
    
    for n in range(max(list(numbers.keys())))[::-1]:
        for movie in data:
            if path[0] == movie[0]:
                if movie[1] in numbers[n]:
                    path = [movie[1]] + path
                    break
            elif path[0] == movie[1]:
                if movie[0] in numbers[n]:
                    path = [movie[0]] + path
                    break
    return path


    

def get_path(data, actor_id_1, actor_id_2):
    numbers = get_actor_bacon_number(data,actor_id_1, actor_id_2)
    if not numbers:
        return None
    path = [actor_id_1]
    movie_path = []
    
    for n in range(max(list(numbers.keys())))[::-1]:
        for movie in data:
            if path[0] == movie[0]:
                if movie[1] in numbers[n]:
                    movie_path.append(movie[2])
                    path = [movie[1]] + path
                    break
            elif path[0] == movie[1]:
                if movie[0] in numbers[n]:
                    movie_path.append(movie[2])
                    path = [movie[0]] + path
                    break
                    
    path.reverse()

    with open('resources/movies.json') as f:
        movies = json.load(f)
    

    for key, value in movies.items():
        if value in movie_path:
            movie_path[movie_path.index(value)] = key
    print(movie_path)

    return path

if __name__ == '__main__':
    with open('resources/large.json') as f:
        db = json.load(f)
    with open('resources/names.json') as f:
        names = json.load(f)
    
    actor1 = names['Kevin Bacon']
    actor2 = names['Harry Moody']

    result = get_path(db, actor1, actor2)
    for key, value in names.items():
        if value in result:
            result[result.index(value)] = key
    print(result)
    # additional code here will be run only when lab.py is invoked directly
    # (not when imported from test.py), so this is a good place to put code
    # used, for example, to generate the results for the online questions.
    pass
