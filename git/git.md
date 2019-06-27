# Command line instructions
You can also upload existing files from your computer using the instructions below.

## Git global setup
```bash
git config --global user.name "Zi Wei Zhang"
git config --global user.email "ziwei.zhang@siemens.com"
```

## Create a new repository
```bash
git clone git@code.siemens.com:ziwei.zhang/gist.git
cd gist
touch README.md
git add README.md
git commit -m "add README"
git push -u origin master
```

## Push an existing folder
```bash
cd existing_folder
git init
git remote add origin git@code.siemens.com:ziwei.zhang/gist.git
git add .
git commit -m "Initial commit"
git push -u origin master
```

## Push an existing Git repository
```bash
cd existing_repo
git remote rename origin old-origin
git remote add origin git@code.siemens.com:ziwei.zhang/gist.git
git push -u origin --all
git push -u origin --tags
```