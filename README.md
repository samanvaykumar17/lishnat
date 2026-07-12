# Android Build Setup (Kivy + Buildozer)

This guide shows how to build the app APK using WSL Ubuntu.

## 1. Install and open WSL Ubuntu

```bash
wsl --install -d Ubuntu-24.04
wsl -d Ubuntu-24.04
```

## 2. Install Python tools

```bash
sudo apt update
sudo apt install -y python3-pip python3-venv
```

## 3. Create and activate virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Install project dependencies

```bash
pip install kivy
pip install buildozer
```

## 5. Initialize Buildozer (first time only)

```bash
buildozer init
```

## 6. Install Android build dependencies

```bash
sudo apt install -y \
    git zip unzip openjdk-17-jdk \
    autoconf automake libtool pkg-config \
    zlib1g-dev libncurses-dev libffi-dev \
    libssl-dev
```

## 7. Build APK

```bash
buildozer android debug
```

## 8. Copy generated APK

```bash
cp bin/*.apk /path/to/whatever
```
