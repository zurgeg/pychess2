echo Installing pyinstaller...

pip install pyinstaller

echo Updating pyinstaller...

pip install pyinstaller --update

echo Updating setuptools...

pip install setuptools --update

echo Making onlinechess.py...

python -m pyinstaller-3.4 -F onlinechess.py

echo Make complete!
