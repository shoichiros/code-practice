import os


def make_folder_file(main_dir):
    for make_number in range(1, 2):
        dir_css = main_dir + '/' + main_dir + str(make_number) + '/templates'
        dir_img = main_dir + '/' + main_dir + str(make_number) + '/static'

        os.makedirs(dir_css, exist_ok=True)
        os.makedirs(dir_img, exist_ok=True)
        with open(main_dir + '/' + main_dir + str(make_number) + '/templates/index.html', 'w'):
            with open(main_dir + '/' + main_dir + str(make_number) + '/static/style.css', 'w'):
                make_number += 1


main = input('新規フォルダ名を指定してください')
make_folder_file(main)
