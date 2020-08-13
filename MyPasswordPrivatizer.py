def GetPassword(path):
    with open(path, 'r') as passwordSecret:
        password = passwordSecret.readline()
    return password
