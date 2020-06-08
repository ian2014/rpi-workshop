* install virtualenv

```
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install -U virtualenv
mkdir lab01
cd lab01
```

* create virtual environment

```
virtualenv venv
source venv/bin/activate
(venv) pi@raspberrypi:~/lab01 $
```

* install dependency packages

```
pip3 install flask
pip3 install gpiozero
pip3 install RPi.GPIO
pip3 install pigpio
```
