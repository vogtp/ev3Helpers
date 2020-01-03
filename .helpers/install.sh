

mv main.py main.temp
mv main_template.py main.py

sudo  cp *.py /Users/Andrin/.vscode/extensions/lego-education.ev3-micropython-1.0.3/resources/template/
cp *.py /Users/debby/.vscode/extensions/lego-education.ev3-micropython-1.0.3/resources/template/

mv  main.py main_template.pys
mv main.temp main.py 

pip3 install pybricks-stubs --upgrade