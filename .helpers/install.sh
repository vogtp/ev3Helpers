

mv main.py main.temp
mv main_template.py main.py

for USER in Andrin debby lauri
do
    echo "Installing ${USER} template"
    sudo  rm /Users/${USER}/.vscode/extensions/lego-education.ev3-micropython-1.0.3/resources/template/*.py
    sudo  cp *.py /Users/${USER}/.vscode/extensions/lego-education.ev3-micropython-1.0.3/resources/template/
    sudo  cp -a .beispiele /Users/${USER}/.vscode/extensions/lego-education.ev3-micropython-1.0.3/resources/template/
done

mv  main.py main_template.py
mv main.temp main.py 

pip3 install pybricks-stubs --upgrade

