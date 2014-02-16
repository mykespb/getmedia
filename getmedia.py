#!python2
# coding: utf-8
# myke gm1.py 2012-11-23 2014-02-17 3.2
# get mp3 from given page
# all received files are stored in subfolder 'files' (created if needed)
# no repetetive file retrieves are made if file already exists locally

"""getmedia.py
Get media files from specified internet address 
(with possible files number limit)

Usage:
  getmedia.py <addr> [-n <num>] <type>...
  getmedia.py -v | --version
  getmedia.py -h | --help
  
Options:
  -n <num>, --number <num>  max number of files to be read [default: 999]
  <type>...                 types of files to be read
  -v --version              version info
  -h --help                 this help screen
  
File types and groups:
  all
  audio (mp3 wav wma ogg aac aiff aob aud bwg cdr flac iff m3u ra m3u8 m4a m4b m4p m4r msv pa spl wm)
  dbms  (db sql)
  doc   (oc pdf ps docx xls ppt pptx odt odc odp)
  image (gif png tif tiff pcx cgm wpg jpg jpeg dxf pcl eps)
  prog  (py pl c cpp h hpp bas js jsp bat cmd java forth ftn a68 pas tcl par)
  tex   (tex bib bbl)
  text  (txt md mmd csv tab)
  video (mp4 wmv avi flv ogm filmmkv mkt mpeg mpg mxf 3gp swf rm vob ifo m2v m2p)
  www   (html html xml css js par)

"""

import os, os.path, sys
import urllib
import lxml.html
from docopt import docopt

ver = '3.2'
print """This is getmedia.py by myke ver. %s""" % (ver,)

para = docopt(__doc__, version=ver)

mtypes = {
    'text':  'txt md mmd csv tab'.split(),
    'www':   'html html xml css js par'.split(),
    'doc':   'doc pdf ps docx xls ppt pptx odt odc odp'.split(),
    'audio': 'mp3 wav wma ogg aac aiff aob aud bwg cdr flac iff m3u ra m3u8 m4a m4b m4p m4r msv pa spl wm'.split(),
    'video': 'mp4 wmv avi flv ogm filmmkv mkt mpeg mpg mxf 3gp swf rm vob ifo m2v m2p'.split(),
    'image': 'gif png tif tiff pcx cgm wpg jpg jpeg dxf pcl eps'.split(),
    'dbms':  'db sql'.split(),
    'prog':  'py pl c cpp h hpp bas js jsp bat cmd java forth ftn a68 pas tcl par'.split(),
    'tex':   'tex bib bbl'.split(),
    }
mtypes['mmedia'] = mtypes['audio'] + mtypes['video']
mtypes['images'] = mtypes['image']
mtypes['all'] = mtypes['mmedia'] + mtypes['prog'] + mtypes['www'] + mtypes['image'] + mtypes['text'] + mtypes['tex'] + mtypes['doc'] + mtypes['dbms']

def addtype(t):
    out = set()
    for at in t:
        if at in mtypes:
            out |= set(mtypes[at])
        else:
            out |= {at}
    return out

url = para['<addr>']

maxfiles = int(para['--number'])

allends = []
inends = para['<type>']
if len(inends)>0:
    allends = list(addtype(inends))

print "url = %s,\nmax files = %d,\nfiles = %s" % (url, maxfiles, allends)
if len(allends)<1:
    print "no files requested"
    sys.exit(2)

upage, uname = os.path.split(url)

cwd = os.getcwd()
print "local path=", cwd
print "page url is", url
try:
    os.mkdir(cwd + r'/files')
    print 'files folder created'
except:
    print 'files folder not created'

try:
    html = urllib.urlopen(url).read()
    doc = lxml.html.fromstring(html)
    doc.make_links_absolute(url)
    
    nofgot = 0  # no. of files really got
    for link in doc.iterlinks():
        the = link[-2]
        for ends in allends:
            if the.endswith(r'.' + ends):
                print "link", the
                upage, uname = os.path.split(the)
                if os.path.exists(r'files/' + uname): 
                    print 'file', uname, 'already exists'
                    continue
                try:
                    fname, headers = urllib.urlretrieve(the, cwd + r'/files/' + uname)
                    print "got good file", link, "\nas", fname
                    nofgot += 1
                    if nofgot >= maxfiles: break
                except:
                    print "no good file", link
        if nofgot >= maxfiles: break
except:
    print 'no files at all'
        
print "finish"
