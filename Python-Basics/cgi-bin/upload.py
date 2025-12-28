#!/usr/bin/env python3
import cgi
import cgitb
import os
import html

cgitb.enable()  # show errors in browser

UPLOAD_DIR = "/tmp/uploads"   # change to your writable folder
os.makedirs(UPLOAD_DIR, exist_ok=True)

print("Content-Type: text/html\n")

form = cgi.FieldStorage()

# -------------------------
# 1. SHOW UPLOAD FORM
# -------------------------
if "file" not in form:
    print("""
    <html>
    <body>
        <h2>Upload a File</h2>
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file" required>
            <input type="submit" value="Upload">
        </form>
    </body>
    </html>
    """)
    exit()

# -------------------------
# 2. PROCESS UPLOAD
# -------------------------
file_item = form["file"]

if not file_item.filename:
    print("<h3>No file selected.</h3>")
    exit()

filename = os.path.basename(file_item.filename)
save_path = os.path.join(UPLOAD_DIR, filename)

# Save file to disk
with open(save_path, "wb") as f:
    f.write(file_item.file.read())

# -------------------------
# 3. READ CONTENT BACK
# -------------------------
try:
    with open(save_path, "r", errors="ignore") as f:
        content = f.read()
    content = html.escape(content)   # safe for HTML
except:
    content = "(Cannot display binary file.)"

# -------------------------
# 4. DISPLAY RESULT
# -------------------------
print(f"""
<html>
<body>
    <h2>File Uploaded Successfully!</h2>
    <p><b>Saved as:</b> {filename}</p>

    <h3>File Content:</h3>
    <pre>{content}</pre>

    <hr>
    <a href="upload.py">Upload Another File</a>
</body>
</html>
""")




""""

Desktop/my_project/
    cgi-bin/
        upload.py

cd ..
chmod 755 upload.py


python3 -m http.server --cgi 8000


http://localhost:8000/cgi-bin/upload.py


"""