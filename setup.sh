echo "Initializing program environment and installing dependencies..."

sudo apt-get update
sudo apt-get install python3.6 python3-pip
python3 -m pip install beautifulsoup4 requests schedule pytest coverage

chmod u+x ./run.sh
chmod u+x ./test.sh
chmod u+x ./delhistory.sh

file=./src/env.py
touch $file
echo "TELEGRAM_BOT_API_KEY = ''" > $file
echo "CHAT_IDS = ['']" >> $file

python3 ./check.py
