# setting up for functional test

## Install browser

- install browser, here we use google chrome

usually the error of unknown chrome binary is caused by not installed or path not set correctly

```shell

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

```

## download and unzip browser driver for selenium

- since selenium 4.11.0, it will handle webdriver for you. no need to worry about the driver

```shell

wget https://chromedriver.storage.googleapis.com/<version>/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
```

# Functional Test == Acceptance Test == End-to-End Test

- using unittest module
- using FT to scope out a minimum viable app
- writing basic test,
- Using Fixture
- Mocking and advanced testing
