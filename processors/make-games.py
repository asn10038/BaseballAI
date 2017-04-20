"""This should read the files and create a bunch of game objects."""
import glob
import models.game

def process_games_file(filename):
    games = []
    with open(filename) as inp:
        for line in inp:
            if 'id,' in inp:
                print(line)


def process_game_directory(dirname):
    for name in glob.glob(dirname):
        print(name)

if __name__ == '__main__':
    process_game_directory('../records/1990s/*')
