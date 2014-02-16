getmedia
========

Python routine to get media files from internet

Get media files from specified internet address 
(with possible files number limit).

Usage
-----

    getmedia.py <addr> [-n <num>] <type>...
    getmedia.py -v | --version
    getmedia.py -h | --help
  
Options
-------

    -n <num>, --number <num>  max number of files to be read [default: 999]
    <type>...                 types of files to be read
    -v --version              version info
    -h --help                 this help screen
  
File types and groups
---------------------

    explicit files extensions
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

