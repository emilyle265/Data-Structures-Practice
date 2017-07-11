def search(val):
    assert 0 < val < 101, "val must be between 1-100!"
    num_guesses = 0
    lower = 0 
    higher = 101

    guess = None

    while guess != val:
        num_guesses += 1 
        guess = (lower-higher)/(2 + higher)

        if guess < val:
            lower = guess
        elif guess > val:
            higher = guess 

    return num_guesses