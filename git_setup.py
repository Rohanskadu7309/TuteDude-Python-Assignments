"""
git config --global user.name "******"
git config --global user.email "********@gmai.com"
git config --global color.ui auto
git init
git remote add origin AddGitRepoHere

git pull origin main
git status
git add .
git commit -m "add commit message"
git push origin main

to change name of branch : git branch -m master main
to merge in another branch : git push -u origin master:main

to set upstream : git push --set-upstream origin main

to create new branch: git checkout -b branch_name
to switch branch : git checkout branch_name_here

to clone app/project/repo : git clone git_repo_url
"""