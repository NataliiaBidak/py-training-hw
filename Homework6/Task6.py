"""
Provided a text file with information about artists and songs:
Joy Division - Love Will Tear Us Apart
Joy Division - New Dawn Fades
Pixies - Where Is My Mind
Pixies - Hey
Genesis - Mama
"""
from collections import defaultdict


class Artist:
    def __init__(self, artist_name, songs):
        self.artist_name = artist_name
        self._songs = songs

    @property
    def songs(self):
        return self._songs


class MusicFile:
    def __init__(self, file_name):
        self.music_dict = self.read_file(file_name)

    def read_file(self, file_name):
        music_dict = defaultdict(list)
        with open(file_name) as musicfile:
            for line in musicfile.readlines():
                artist, song = line.split('-')
                artist = artist.strip()
                song = song.strip()
                # if artist in music_dict.keys():
                #     songs_list = list()
                #     songs_list.append(music_dict.get(artist))
                #     songs_list.append(song)
                #     music_dict.update({artist: songs_list})
                # else:
                #     music_dict[artist] = song
                music_dict[artist].append(song)
        return music_dict

    def artist(self, name):
        artist = Artist(name, self.music_dict.get(name))
        return artist


music = MusicFile('music.txt')
print(music.artist('Joy Division').songs)

# a = Artist("blalalalal", )
