@echo off


cd /d %~dp0
mkdir flaskapp
cd flaskapp
mkdir templates
mkdir static
type nul>app.py
cd templates
type nul>index.html
cd ../
cd static
type nul>style.css
cd ../

python -m venv myv
call myv\scripts\activate
python -m pip install --upgrade pip
pip install flask
call deactivate

exit
