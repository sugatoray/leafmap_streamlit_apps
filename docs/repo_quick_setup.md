# Repository Quick Setup

SSH: `git@github.com:sugatoray/leafmap_streamlit_apps.git`
HTTPS: `https://github.com/sugatoray/leafmap_streamlit_apps.git`

## Create a new local reository on the command line and push it to remote (at GitHub)

```sh
echo "# leafmap_streamlit_apps" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M master
## For SSH:
git remote add origin git@github.com:sugatoray/leafmap_streamlit_apps.git
## For HTTPS:
# git remote add origin https://github.com/sugatoray/leafmap_streamlit_apps.git
git push -u origin master
```

## Push an existing local repository to the remote (at GitHub)

```sh
## For SSH:
git remote add origin git@github.com:sugatoray/leafmap_streamlit_apps.git
## For HTTPS:
# git remote add origin https://github.com/sugatoray/leafmap_streamlit_apps.git
git branch -M master
git push -u origin master
```
