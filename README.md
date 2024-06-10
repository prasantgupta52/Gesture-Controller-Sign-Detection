# Setup


### 1) First make sure your device has the [python ](https://www.python.org/downloads/) if not Download and install 

### 2) Install [Anaconda](https://www.anaconda.com/products/individual) as the program needs to be run on anaconda powershell

### 3) Pre-requisites
  
  Python: (3.6 - 3.8.5)<br>
  Anaconda Distribution: To download click [here](https://www.anaconda.com/products/individual).
  
  ### Procedure
  clone the github project Or Open the source code
  ```bash
  git clone https://github.com/prasantgupta52/Gesture-Controller-Sign-Detection.git
  ```

  Step 1: open the folder through anaconda powershell
  ```bash
  conda create --name gest python=3.8.5
  ```
  
  Step 2:
  ```bash
  conda activate gest
  ```
  
  Step 3:
  ```bash
  pip install -r requirements.txt
  ```
  
  Step 4:
  ```bash 
  conda install PyAudio
  ```
  ```bash 
  conda install pywin32
  ```

### 4) open the folder through anaconda powershell move inside subfolders and install all requirements

```bash
cd .\Mouse-Controll-USing-Gesture\
```
```bash
pip install -r .\requirements.txt
```
```bash
cd ..
```
```bash
cd .\sign-language-detector-python\
```
```bash
pip install -r .\requirements.txt
```
```bash
cd ..
```
          
### 5) Now Lets run the program

```bash
python.exe .\main.py
```

### 6) Now we can see a menu driven program which shows 2 option by pressing 1 you will enter Gesture control and by pressing 2 you will enter Sign detection

### 7) If you want to terminate the program execution the go to anaconda power shell and press

Ctrl + C
