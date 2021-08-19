#!/usr/bin/python3
# Import Basic OS functions
import os
# Import modules for CGI handling
import cgi, cgitb, jinja2
# enable debugging
import urllib.request

cgitb.enable()
# print content type
print("Content-type:text/html\r\n\r\n")

HTML = """
<html>
<head>
<title></title>
</head>
<body>

  <h1>Upload File</h1>
  <form action="form.py" method="POST" enctype="multipart/form-data">
    File: <input name="file" type="file">
    <input name="submit" type="submit">
</form>

{% if filedata %}

<blockquote>

{{filedata}}

</blockquote>

{% endif %}

</body>
</html>
"""


inFileData = None

form = cgi.FieldStorage()

UPLOAD_DIR='uploads'


if "file" in form:
    form_file = form['file']

    if form_file.filename:
        uploaded_file_path = os.path.join(UPLOAD_DIR, os.path.basename(form_file.filename))
        with open(uploaded_file_path, 'wb') as fout:
            while True:
                chunk = form_file.file.read(100000)
                if not chunk:
                    break

                fout.write(chunk)

        with open(uploaded_file_path, 'r') as fin:
            inFileData = ""
            for line in fin:
                inFileData += line

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
print(jinja2.Environment().from_string(HTML).render(filedata=inFileData))
