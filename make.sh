echo Installing pyinstaller...
#<<<<<<< developer

pip install pyinstaller

echo Updating pyinstaller...

pip install pyinstaller --update

echo Updating setuptools...

pip install setuptools --update

echo Making onlinechess.py...

python -m pyinstaller-3.4 -F onlinechess.py

echo Make complete!
#=======
#pip install pyinstaller
#echo Updating pyinstaller...
#pip install pyinstaller --update
#echo Updating setuptools...
#pip install setuptools --update
#echo Making onlinechess.py...
#python -m pyinstaller -F onlinechess.py
#echo Make complete!


#>>>>>>> master
