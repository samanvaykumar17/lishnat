wsl --install -d Ubuntu-24.04
wsl -d Ubuntu-24.04
sudo apt update
sudo apt install python3-pip python3-venv
python3 -m venv venv
source venv/bin/activate
pip install kivy
pip install buildozer

buildozer init

sudo apt install -y \
    git zip unzip openjdk-17-jdk \
    autoconf automake libtool pkg-config \
    zlib1g-dev libncurses-dev libffi-dev \
    libssl-dev
	
buildozer android debug

cp bin/*.apk /path/to/whatever
