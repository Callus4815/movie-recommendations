import csv
from collections import defaultdict


#item file= "ml-100k/u.item"
#data file= "ml-100k/u.data"


#name of movie by id
def get_movie_names_by_id(data_file):

    with open(data_file, encoding='windows-1252') as file:
        data1 = csv.reader(file , delimiter = "|" )
        raw_movies = (list(data1))
        for row in raw_movies:
            movie_id_list = [x[0] for x in raw_movies]
            movie_titles = [k[1] for k in raw_movies]
            movie_dict = {ID : Name for ID,Name in zip(movie_id_list, movie_titles)}
    return movie_dict

#all ratings for a user
def get_user_ratings_by_id(data_file):
    with open(data_file, encoding ='windows-1252') as a_file:
        data2 = csv.reader(a_file, delimiter = "\t")
        user_ratings_by_ids_dict = defaultdict(list)
        for row in data2:
            raw_data = list(data2)
            id_user = [x[0] for x in raw_data]
            _rating = [x[2] for x in raw_data]
            user_ids_with_movie_ratings= list(zip(id_user,_rating))
            for k,v in user_ids_with_movie_ratings:
                user_ratings_by_ids_dict[k].append(v)
    return user_ratings_by_ids_dict

#get all ratings for a movie by id
def get_movie_ratings_by_movie_id(data_file):
    with open(data_file, encoding ='windows-1252') as b_file:
        data3 = csv.reader(b_file, delimiter = '\t')
        movie_ratings_by_id = defaultdict(list)
        for row in data3:
            raw_data = list(data3)
            movie_id = [x[1] for x in raw_data]
            movie_rating = [x[2] for x in raw_data]
            user_id_ratings = list(zip(movie_id, movie_rating))
            for k,v in user_id_ratings:
                movie_ratings_by_id[k].append(int(v))
    return movie_ratings_by_id


movie_names = get_movie_names_by_id('ml-100k/u.item')
movie_ratings = get_movie_ratings_by_movie_id('ml-100k/u.data')
user_rates = get_user_ratings_by_id('ml-100k/u.data')

def get_movie_name(movie):
    return str(movie_names[movie])



def all_ratings_for_movie(movie):
    return sorted(movie_ratings[movie])

def average_ratings(movie, min_rating=8):
    ratings = all_ratings_for_movie(movie)
    if len(ratings) < min_rating:
        return None
    else:
        the_average = sum(ratings)//len(ratings)
        return the_average

def ratings_for_users(user):
    return [x for x in user_rates[user]]

def top_movies(x, min_ratings=8):
