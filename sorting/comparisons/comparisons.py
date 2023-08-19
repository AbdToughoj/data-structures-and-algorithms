# Sort movies by most recent year first
def sort_by_year(movies):
    return sorted(movies, key=lambda movie: movie["year"], reverse=True)

# Sort movies alphabetically by title, ignoring leading articles
def sort_by_title(movies):
    ignored_articles = ["A", "An", "The"]

    def ignore_leading_articles(title):
        for article in ignored_articles:
            if title.startswith(article + " "):
                return title[len(article) + 1:]
        return title

    return sorted(movies, key=lambda movie: ignore_leading_articles(movie["title"]))

# Tests for the comparator functions
def test_comparators():
    movies = [
        {"title": "The Matrix", "year": 1999},
        {"title": "A Beautiful Mind", "year": 2001},
        {"title": "Inception", "year": 2010},
        {"title": "Annie Hall", "year": 1977},
        {"title": "The Avengers", "year": 2012},
    ]

    # by_year
    sorted_by_year = sort_by_year(movies)
    sorted_titles_by_year = [movie["title"] for movie in sorted_by_year]
    assert sorted_titles_by_year == [
        "The Avengers",
        "Inception",
        "A Beautiful Mind",
        "The Matrix",
        "Annie Hall",
    ]

    # by_title
    sorted_by_title = sort_by_title(movies)
    sorted_titles_by_title = [movie["title"] for movie in sorted_by_title]
    assert sorted_titles_by_title == [
        "Annie Hall",
        "The Avengers",
        "A Beautiful Mind",
        "Inception",
        "The Matrix",
    ]

    print("All tests passed!")

# Run the tests
test_comparators()
