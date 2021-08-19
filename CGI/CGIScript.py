#!/usr/bin/python

print("Content-type: text/html\r\n\r\n")
print()

print("<html>")
print("<head>")
print("<title> My first CGI App </title>")
print("</head>")
print("<body>")
print("<h3> This is the HTML body </h3>")
print("</body>")
print("</html>")



#!/usr/bin/python3

# Import Basic OS functions
# Import modules for CGI handling
import cgi, cgitb, jinja2
#import urllib.request

import subprocess

# enable debugging
cgitb.enable()
# print content type
print("Content-type:text/html\r\n\r\n")

welcome="Hello!"

form = cgi.FieldStorage()
name = form.getvalue('print')
if not 'print' in form or name is None:
    out = None
else:
    out = subprocess.check_output(["echo","Hello "+name])
    # welcome = "Hello "+str(name)
    # out = subprocess.check_output(["~/public_html/fortunes.sh"], shell=True)

    if out != None:
        out = out.decode('utf-8', 'ignore')


env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
template = env.get_template('helloWorld.html')

print(template.render(
    title='Awesome Templated Website',
    randomstr=welcome,
    awesomeText=out
))