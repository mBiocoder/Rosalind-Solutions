#!/usr/bin/python3
# Import Basic OS functions
import os
# Import modules for CGI handling
import cgi, cgitb, jinja2
# enable debugging
import urllib.request
import subprocess

cgitb.enable()
# print content type
print("Content-type:text/html\r\n\r\n")

inFileData = None
form = cgi.FieldStorage()

UPLOAD_DIR='uploads'

if "file" in form:
    form_file = form['file']

    if form_file.filename:

        uploaded_file_path = os.path.join(UPLOAD_DIR, os.path.basename(form_file.filename))

        #out = subprocess.check_output(["echo", "Hello "])
        #out = subprocess.check_output(['~/public_html/GC_content.py', uploaded_file_path])
        #out = subprocess.check_output(['~/public_html/GC_content.py'], shell=True)
        #out = subprocess.check_output('python3 fortunes.py', shell=True)

        #if out != None:
            #out = out.decode('utf-8', 'ignore')

        with open(uploaded_file_path, 'wb') as fout:
            while True:
                chunk = form_file.file.read()
                if not chunk:
                    break

                fout.write(chunk)
            fout.close()

        with open(uploaded_file_path, 'r') as fin:
            inFileData = ""
            for line in fin:
                inFileData += line

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))
template = env.get_template('GC_content.html')

#print(template.render(title='GC_content', filedata=out))

print(template.render(title='GC_content', filedata=inFileData))
