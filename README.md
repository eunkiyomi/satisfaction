# satisfaction
Bless you, my dear
[https://github.com/PPYAPgit/satisfaction]

## How to edit
We should use *satisfaction-git* directory.

After edit, use
- `git add`, then changed files will be tracked. (We can see this by `git status`)
- `git commit -m "<description>"`, then tracked files will be committed.
- `git push origin master`, then committed files will be saved in the master branch. (which is online.)

After push, go to server and
- `git pull origin master`, then files in server will be updated.

## Use Local Server
Run `runserver` in *satisfaction/manage.py*
- `python3 manage.py runserver`, then local server will run at port 8000.
