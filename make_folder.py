import os


def makefolderfile(maindir):
    for mknumber in range(1, 2):
        dircss = maindir + '/' + maindir + str(mknumber) + '/templates'
        dirimg = maindir + '/' + maindir + str(mknumber) + '/static'

        os.makedirs(dircss, exist_ok=True)
        os.makedirs(dirimg, exist_ok=True)
        with open(maindir + '/' + maindir + str(mknumber) + '/templates/index.html', 'w'):
            with open(maindir + '/' + maindir + str(mknumber) + '/static/style.css', 'w'):
                mknumber += 1


main = input('新規フォルダ名を指定してください')
makefolderfile(main)
