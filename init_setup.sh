echo [$(date)]: "START"

echo [$(date)]: "creating env with python 3.11 version" 

python3.11 -m venv ./env

echo [$(date)]: "activating the environment" 
source ./env/bin/activate

echo [$(date)]: "installing the dev requirements" 
pip install -r requirements_dev.txt

echo [$(date)]: "END" 