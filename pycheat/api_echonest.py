#Don`t forget pip install pyechonest & getting your api!

#Set your api key

from pyechonest import config
    config.ECHO_NEST_API_KEY="YOUR API KEY"

#Find artists similar to Guns`N Roses

from pyechonest import artist
bk = artist.Artist('Guns and roses')
print "Artists similar to: %s:" % (bk.name,)
for similar_artist in bk.similar: print "\t%s" % (similar_artist.name,)

#Search for artists

from pyechonest import artist
weezer_results = artist.search(name='weezer')
weezer = weezer_results[0]
weezer_blogs = weezer.blogs
print 'Blogs about weezer:', [blog.get('url') for blog in weezer_blogs]


#Get an artist by name:

from pyechonest import artist
a = artist.Artist('lady gaga')
print a.id


#Get the top hottt artists:

from pyechonest import artist
for hottt_artist in artist.top_hottt():
print hottt_artist.name, hottt_artist.hotttnesss

#Search for songs:

from pyechonest import song
rkp_results = song.search(artist='radiohead', title='karma police')
karma_police = rkp_results[0]
print karma_police.artist_location
print 'tempo:',karma_police.audio_summary['tempo'],'duration:',karma_police.audio_summary['duration']


#Get a song's audio_url and analysis_url:

from pyechonest import song
ss_results = song.search(artist='the national', title='slow show', buckets=['id:7digital-US', 'tracks'], limit=True)
slow_show = ss_results[0]
ss_tracks = slow_show.get_tracks('7digital-US')
print ss_tracks[0].get('preview_url')
