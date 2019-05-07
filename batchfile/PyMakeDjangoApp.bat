@echo off

set virtual=myv
set /P dir="new create dir name: "
set /P project="new create project name: "
set /P app="new create app name: "

cd /d %~dp0
mkdir %dir%
cd %dir%

python -m venv %virtual%
call myv\scripts\activate
python -m pip install --upgrade pip
pip install django

django-admin startproject %project%
cd %project%
python manage.py startapp %app%
mkdir templates
cd %app%
type nul>urls.py
mkdir static
mkdir templates
cd static
mkdir %app%
cd %app%
type nul>style.css
cd ../../
cd templates
mkdir %app%
cd %app%
type nul>index.html
call deactivate

exit
