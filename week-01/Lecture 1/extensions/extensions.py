name = input("What's the file name and extension? ").strip().lower()

#extension = name.rsplit('.', 1)[1]

if name.endswith((".jpg", ".jpeg")):
    print("image/jpeg")
elif name.endswith((".gif", ".png")):
    print(f"image/{name.split('.')[-1]}")
elif name.endswith((".pdf", ".zip")):
    print(f"application/{name.split('.')[-1]}")
elif name.endswith((".txt")):
    print("text/plain")
else:
    print("application/octet-stream")
