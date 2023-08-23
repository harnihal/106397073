x = input("File name: ")

x = x.lower()

if '.gif' in x:
    print('image/gif')
elif '.jpeg' in x:
    print('image/jpeg')
elif '.jpg' in x:
    print('image/jpeg')
elif '.png' in x:
    print('image/png')
elif '.pdf' in x:
    print('application/pdf')
elif '.txt' in x:
    print('text/plain')
elif '.zip' in x:
    print('application/zip')
else:
    print('application/octet-stream')