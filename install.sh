source bin/activate
echo "installing dependencies"
sudo apt-get install python3.6-dev
pip3 install --upgrade pip -r requirements.txt
echo "all done!"
