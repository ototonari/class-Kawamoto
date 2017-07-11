#!/usr/bin/env python
# coding: UTF-8

print("Content-Type: text/html;charset=utf-8")
print("")

print("<TITLE>CGI script output</TITLE>")
print("<H1>This is my first CGI script</H1>")
print("Hello,world!")

form1 = """
<form action="spy_camera.py" method="">
<input type="submit" value="button1">
"""

print(form1)

