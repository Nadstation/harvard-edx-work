SHOWS = [
    " Avatar: the last airbender",
    "Ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and ferb",
    "Kim possible",
    "Jimmy Neutron ",
    "the Proud family"
    ]


def main():
    cleaned_shows = []
    for show in SHOWS:
        print(show.strip().title())
        cleaned_shows.append(show.strip().title())

    #print(', '.join(cleaned_shows))
    #print(cleaned_shows)


main()

#print(SHOWS)


