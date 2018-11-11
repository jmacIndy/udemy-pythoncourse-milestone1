"""
The Complete Python Course - Udemy - Jose Salvatierra
Milestone project 1
Movie Project

A movie storage application, that will allow users to manage their movie collection
and find any movie they want.

Here's the main three features:
    o First, the application must allow users to add new movies to collection,
    o Second, the application must allow users to view all the movies in their
      collection, and,
    o Finally, the application must allow users to find any particular movie by
      any of its attributes.

User Input:
    'a' = add a movie
    'l' = list movies
    'f' = find a movie
    'q' = quit

Attributes of a movie are:
    Title
    Director
    Year

Tasks:
    [X]: Decide how we will store the movies
    [X]: Show user menu and get their input
    [X]: Allow users to add movies
    [X]: Show user all their movies
    [X]: Find a movie
    [X]: Allow user to quit
"""

movies = []


def display_menu():

    done = False

    # loop until user chooses to end
    while not done:

        # display menu
        print('\nMenu:')
        print('    a. Add a movie')
        print('    l. List all movies')
        print('    f. Search for a movie')
        print('    q. End this program')
        choice = input('What do you want to do? ')

        # add movie
        if choice.lower() == 'a':

            add_movie()

        # view all movies in collection
        elif choice.lower() == 'l':

            list_movies(movies)

        # search for movie by a field
        elif choice.lower() == 'f':

            find_movies()

        # in this case, we are done
        elif choice.lower() == 'q':
            done = True

        # in this case, the user made an invalid choice
        else:
            print('ERROR: Invalid choice. Please try again!')


def add_movie():

    # ask user for inputs
    print('Input Movie Information:')
    title = input('    Movie Title: ')
    director = input('    Movie Director: ')
    year = input('    Year Released: ')

    # store record in 'database'
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })


def list_movies(movies):

    # print out information in a list
    print('Your Library:')
    for movie in movies:
        list_movie_details(movie)


def list_movie_details(movie):

    # print detailed movie information
    print(f"   Title: {movie['title']}")
    print(f"      Director: {movie['director']}")
    print(f"      Year Released: {movie['year']}")


def find_movies():

    # ask user what field and value to search on
    search_type = input('What movie property to find by? ')
    search_value = input('What value to find? ')

    # find those results and show to user
    # a lambda is kind of overkill, but we want to use it
    found_movies = find_by_attribute(movies, search_value, lambda x: x[search_type])

    list_movies(found_movies)


def find_by_attribute(items, expected, finder):
    """ This function is really nice and generic. Could be used anywhere. """

    found = []

    for i in items:
        if finder(i) == expected:
            found.append(i)

    return found


"""
MAIN PROGRAM
"""

display_menu()
