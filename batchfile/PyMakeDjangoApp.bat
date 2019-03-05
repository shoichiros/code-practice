@echo off


cd /d %~dp0
mkdir StarrySky
cd StarrySky

python -m venv myv
call myv\scripts\activate
python -m pip install --upgrade pip
pip install django

django-admin startproject starrysky
cd starrysky
python manage.py startapp accounts
mkdir templates
cd accounts
type nul>urls.py
mkdir static
mkdir templates
cd static
mkdir accounts
cd accounts
type nul>style.css
cd ../../
cd templates
mkdir accounts
cd accounts
type nul>index.html
call deactivate

exit
