with open('file.txt','r') as f:
    print(type(f))

#seek and tell funcation.
    f.seek(10)

    print(f.tell())

    data = f.read(5)
    print(data)