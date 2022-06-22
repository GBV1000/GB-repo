import os

home_dir = 'my_project'
inside_dirs = ['adminapp', 'authapp', 'mainapp', 'settings']

if not os.path.exists(home_dir):
    os.mkdir(home_dir)

for i in inside_dirs:
    if not os.path.exists(os.path.join(home_dir, i)):
        dirs_sky = os.path.join(home_dir, i)
        os.mkdir(dirs_sky)
