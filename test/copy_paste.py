#! /usr/bin/python
import pygtk
pygtk.require('2.0')
import gtk
import os
import sys
import time

def copy_image(f):
    assert os.path.exists(f), "file does not exist"
    image = gtk.gdk.pixbuf_new_from_file(f)
    clipboard = gtk.clipboard_get(gtk.gdk.SELECTION_CLIPBOARD)
    clipboard.set_image(image)
    clipboard.store()

def paste_image():
    clipboard = gtk.clipboard_get(gtk.gdk.SELECTION_CLIPBOARD)
    clipboard.request_image(handler)

def handler(arg1, buf, arg3):
    print "**************"
    print "image width  is " + str(buf.get_width()) + "px"
    print "image height is " + str(buf.get_height()) + "px"

copy_image(sys.argv[1]);
time.sleep(1);
paste_image();
