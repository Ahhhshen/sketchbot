# sketchbot

First, clone this repo to your local project file folder, (note: please put it into a independent folder!)

## set up the loacal env

a. Inside your pset/project folder, create the environment: python3 -m venv env
b. Activate the environment: source env/bin/activate. You’ll have to do this every time you want Drake/manipulation packages. 
   In VSCode, you can do this automatically by using the “Python: Select Interpreter” command and selecting the virtual environment. If you are using a notebook, ensure you select your virtual environment for the Python kernel.

## Install Pydrake
Install manipulation. It should automatically install the required Drake version. Run:

`pip install manipulation --upgrade --extra-index-url https://drake-packages.csail.mit.edu/whl/nightly/`
