echo "Initializing program environment and installing dependencies..."
sudo apt-get update
sudo apt-get install python3.6 
python get-pip.py
python3 -m pip install beautifulsoup4 requests schedule
chmod u+x ./run.sh
chmod u+x ./delhistory.sh
python3 ./check.py