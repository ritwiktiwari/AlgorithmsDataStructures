from random import randint


def song_shuffler(arr):
    n = len(arr) - 1
    while n >= 0:
        random_song_index = randint(0, n+1)
        print("Playing song:", arr[random_song_index])
        arr[random_song_index], arr[n] = arr[n], arr[random_song_index]
        n -= 1


songs = [1, 2, 3, 11, 22, 33]
song_shuffler(songs)
