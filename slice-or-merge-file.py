def slice(filename):
    f = open(filename, 'rb')
    fileBytes = f.read()
    f.close()

    with open('./slice1', 'wb') as s:
        s.write(fileBytes[0:int(len(fileBytes) / 2)])

    with open('./slice2', 'wb') as s:
        s.write(fileBytes[int(len(fileBytes) / 2):])

def merge(filename):
    f = open(filename, 'wb')

    with open('./slice1', 'rb') as s1: f.write(s1.read())
    with open('./slice2', 'rb') as s2: f.write(s2.read())

    f.close()

option = input('Slice or Merge? [s/m] ')

if option == 's':
    slice(input('File?: '))
elif option == 'm':
    merge(input('Output file?: '))
else:
    print('Unknown option.')

