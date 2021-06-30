#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# REST service test
#
# (C) 2013 by Dominik Jain
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from Tkinter import *
from simpleui import *
import os
import pickle
import urllib
import urllib2
import json

# --- main gui class ---

class RestTestUI(object):

    def __init__(self, master, dir, settings):
        master.title("REST Test Client")

        self.master = master
        self.settings = settings
        if not "method4url" in settings: settings["method4url"] = {}
        if not "data4url" in settings: settings["data4url"] = {}

        self.frame = Frame(master)
        self.frame.pack(fill=BOTH, expand=1)
        self.frame.columnconfigure(1, weight=1)

        font = None #"Courier"
        row = -1

        # URL
        row += 1
        Label(self.frame, text="URL: ").grid(row=row, column=0, sticky=E)
        self.url = StringVar(master)
        self.url.set(self.settings.get("url", "http://"))
        self.urllist = DropdownList(self.frame, self.settings.get("urllist", []), None, True, self.onPickUrl)
        self.urllist.grid(row=row, column=1, sticky="NWE")
        row += 1
        Entry(self.frame, textvariable = self.url).grid(row=row, column=1, sticky="NEW")

        # method
        row += 1
        Label(self.frame, text="Method: ").grid(row=row, column=0, sticky=NE)
        self.method = StringVar(master)
        self.method.set(self.settings.get("method", "GET"))
        list = apply(OptionMenu, (self.frame, self.method) + ("GET", "POST", "PUT", "DELETE"))
        list.grid(row=row, column=1, sticky="NWE")

        # data selection
        row += 1
        Label(self.frame, text="Data: ").grid(row=row, column=0, sticky=NE)
        self.data = FilePickEdit(self.frame, "*.in", self.settings.get("data", ""), 22, rename_on_edit=self.settings.get("data_rename", 0), font=font, coloring=True)
        self.data.grid(row=row, column=1, sticky="NWES")
        self.frame.rowconfigure(row, weight=1)

        # request button
        row += 1
        start_button = Button(self.frame, text=">> Issue Request <<", command=self.start)
        start_button.grid(row=row, column=1, sticky="NEW")

        # response text field
        row += 1
        Label(self.frame, text="Response: ").grid(row=row, column=0, sticky=NE)
        self.response = SyntaxHighlightingText(self.frame)
        self.response.grid(row=row,column=1, sticky="NWES")
        self.frame.rowconfigure(row, weight=1)

        self.setGeometry()

    def onPickUrl(self, *args):
        if "urllist" in dir(self):
            url = self.urllist.get()
            self.url.set(url)
            method = self.settings["method4url"].get(url)
            if method is not None:
                self.method.set(method)
            data = self.settings["data4url"].get(url)
            if data is not None:
                self.data.select(data)

    def setGeometry(self):
        g = self.settings.get("geometry")
        if g is None: return
        self.master.geometry(g)

    def start(self, saveGeometry = True):
        url = self.url.get()
        data = self.data.get()
        method = self.method.get()
        # update settings
        self.settings["geometry"] = self.master.winfo_geometry()
        self.settings["url"] = url
        self.settings["data"] = data
        self.settings["method"] = method
        self.settings["method4url"][url] = method
        self.settings["data4url"][url] = data
        urllist = self.settings.get("urllist", [])
        if url in urllist:
            urllist.remove(url)
        urllist = [url] + urllist
        self.settings["urllist"] = urllist
        self.urllist.setItems(urllist)
        pickle.dump(self.settings, file("config.dat", "w+"))
        data = self.data.get_text()
        # make call
        try:
            opener = urllib2.build_opener(urllib2.HTTPHandler)
            print "url: %s" % url
            request = urllib2.Request(url, data=data)
            request.add_header('Content-Type', 'application/json')
            request.add_data(data)
            print "data:\n%s" % data
            request.get_method = lambda: method
            url = opener.open(request)
            response = url.read()
            try:
                obj = json.loads(response)
                self.response.setText(json.dumps(obj, indent=4))
            except:
                self.response.setText(response)
        except urllib2.HTTPError as e:
            self.response.setText(str(e))


# -- main app --

if __name__ == '__main__':

    # read previously saved settings
    settings = {}
    configname = "config.dat"
    if os.path.exists(configname):
        try:
            settings = pickle.loads("\n".join(map(lambda x: x.strip("\r\n"), file(configname, "r").readlines())))
        except:
            pass

    # create gui
    root = Tk()
    app = RestTestUI(root, ".", settings)
    root.mainloop()

