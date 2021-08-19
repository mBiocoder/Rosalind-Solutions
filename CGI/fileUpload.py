#!/usr/bin/python3
import cgi, os
import cgitb; cgitb.enable();
form = cgi.FieldStorage()

#Get filename here
fileitem = form['filename']
#Test if file was uploaded
if fileitem.filename:
    #strip leading path from file name
    fn = os.path.basename(fileitem.filename.replace("\\", "/"))
    open('/templates/' + fn, 'wb').write(fileitem.file.read())
    message = 'The file ' + fn + 'was uploaded successfully.'

else:
    message = 'No file was uploaded'

print("""\
Content-Type: text/html\n
<html>
<body>
   <p>%s</p>
</body>
</html>
""" %(message,))
