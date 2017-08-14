
import urllib 
try: import urllib2
except: import urllib.request as urllib2 
import re 
import math


def _make_url(yid): return "https://youtube.com/watch?v=" + yid

def _get_source(yid): return urllib2.urlopen(_make_url(yid)).read().decode("utf-8")


ytm = "<meta itemprop=\"%s\" content=\"(.*?)\">"

class Youtube(object):
	def __init__(self, q=None, ID=None):
		if not ID: self.id = self._getID(q)
		else: self.id = ID
		self.title = None
		self.name = None
		self.views = None
		self.likes = None
		self.dislikes = None
		self.published = None
		self.genre = None
		self.length = None
		self.source = _get_source(self.id)
		if not q and not ID:
			raise Exception("must either be a value for ID or q")
		self._make()
	def _getItem(self, pattern, flag=re.M):
		m = re.search(pattern, self.source, flag)
		if m: return m.groups()
		else: return [None]

	def _getID(self, q):
		url = "https://youtube.com/results?search_query=" + q.replace(" ", "+")
		content = urllib2.urlopen(url).read().decode("utf-8")
		pattern = "<a href=\"/watch\?v=(\w+)\" class"
		m = re.search(pattern, content, re.M)
		return m.groups()[0]
		

	def _make(self):
		self.title = self._getItem(ytm % "name")[0]
		self.description = self._getItem(ytm % "description")[0]
		self.length = self._getItem(ytm % "duration")[0].replace("PT","")
		self.name = self._getItem("\"name\": \"(.*?)\"")[0]
		self.views = self._getItem("<div class=\"watch-view-count\">(.*?) views</div>")[0]
		self.likes = int(math.floor(float(self._getItem("<div class=\"video-extras-sparkbar-likes\" style=\"width: (.*?)%\"></div>")[0]))) 
		self.dislikes = int(math.floor(float(self._getItem("<div class=\"video-extras-sparkbar-dislikes\" style=\"width: (.*?)%\"></div>")[0])))
		self.published = self._getItem(ytm % "datePublished")[0]
		self.genre = self._getItem(ytm % "genre")[0]

	def __repr__(self): return "<Youtube.id=%s, Youtube.name=%s, Youtube.views=%s>" % (self.id, self.name, self.views)
