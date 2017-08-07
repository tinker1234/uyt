# uyt
scrap / search Youtube. You might ask why I use urllib/urllib2 instead of requests. Well, its because I've noticed requests is a bit slower, plus I wanted it to be used out of the box. What can it do?

It can search youtube and find the ID of the first video.
It can grab,
-auther, 
-titles, 
-description,
-length (M=Minutes, S=seconds etc),
-views (it has commas) likes/dislikes (int value),
-published (year-month-day),
-genres

// NOTE
Everything network wise is done in the __init__ to make things faster.

# How to use to search

```python
from uyt import youtube

yt = youtube.Youtube("test") # grabs id then scraps YouTube so its slower
print("Author: %s" % yt.name)
print("Title: %s" % yt.title)
print("Description: %s" % yt.description)
print("Length: %s" % yt.length)
print("Views: %s" % yt.views)
print("Likes: {0}%".format(yt.likes))
print("Dislikes: {0}%".format(yt.dislikes))
print("Published: %s" % yt.published)
print("Genre: %s" % yt.genre)
```
# How to use with ID
```python
from uyt import youtube

yt = youtube.Youtube(ID="<id>") # faster
print("Author: %s" % yt.name)
print("Title: %s" % yt.title)
print("Description: %s" % yt.description)
print("Length: %s" % yt.length)
print("Views: %s" % yt.views)
print("Likes: {0}%".format(yt.likes))
print("Dislikes: {0}%".format(yt.dislikes))
print("Published: %s" % yt.published)
print("Genre: %s" % yt.genre)
```

# How to install
```bash
python setup.py install
python3 setup.py install
```
# Test it
```bash
python -m "uyt.youtube"
python3 -m "uyt.youtube"
```
# Supported OS's

Linux/Windows
