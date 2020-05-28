# Setup Tutorial For ROK bot Development
 
## Development Environments
 
### Man Power
- Project Manager : Moon.Jungsam
- Software Designer : Moon.Jungsam
- Programmer : 
  - backend: Moon.Jungsam
  - frontend: 
- Visual Designer : Moon.Jungsam
 
 
### Hardware
- Computer: PC 2EA, MacMini
- Mobile: iPad mini, Galaxy Note 8
 
 
### Software
- O/S:
  - windows10
  - osx
- Edit Tool
  - Visual Studio Code
- DataBase
  - mongodb
  - google drive
- Emulator
  - bluestack
  - ldplayer
  - nox
- Language
  - coding: english + korean
  - programming: python
- Version Control
  - github
 
 
## Contents
- Python
  - virtual environment
  - install packages
 
- Git
  - remote repository
  - local repository
 
- Visual Studio Code
 
 
## Python
 
### python 가상 환경 설정
 
#### 리눅스, 맥
 
```bash
/Volumes/data/dev/SynologyDrive/projects$ mkdir _venv
/Volumes/data/dev/SynologyDrive/projects$ cd _venv
/Volumes/data/dev/SynologyDrive/projects/_venv$ pip install virtualenv  // 가상환경 모듈 설치
/Volumes/data/dev/SynologyDrive/projects/_venv$ virtualenv rok  // 가상환경 만들기
/Volumes/data/dev/SynologyDrive/projects/_venv$ source rok/bin/activate  // 가상환경 활성화
(venv) /Volumes/data/dev/SynologyDrive/projects/_venv$ cd ../ESROK
(venv) /Volumes/data/dev/SynologyDrive/projects/ESROK$ pip list  // 설치 패키지 목록 확인
```
 
#### 윈도우
 
```
> pip install virtualenv  // 가상환경 모듈 설치
D:\moon\dev\projects\rok> virtualenv venv  // 가상환경 만들기
d:\moon\dev\_venv> call venv/scripts/activate  // 가상환경 활성화
(venv) > pip list  // 설치 패키지 목록 확인
```
 
### 버전 관리
 
#### 원격 저장소
 
- https://github.com/hopelife/rok.git
 
 
#### 로컬 저장소
 
##### windows10

- 로컬1: 
- 로컬2: D:\moon\dev\projects\rok\bot
- init_rok.bat

###### 리모트에 README.md가 없는 경우

````bash
echo "# ESROK(Every Services For Rise Of Kingdoms)" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/hopelife/esrok.git
git push -u origin master
```

###### 리모트에 README.md가 있는 경우

```bash
git init
git remote add origin https://github.com/hopelife/esrok.git
git pull origin master
```
 
##### osx
 
 
### python 패키지 설치
 
#### pyautogui
 
- GUI 
```
pip3 install pyautogui
```
 
 
#### opencv
 
 
```
pip uninstall opencv-contrib-python
pip uninstall opencv-python
 
# 가상환경인 경우
pip3 install opencv-contrib-python==3.4.2.16
 
# 가상환경이 아닌 경우
pip install --user opencv-contrib-python==3.4.2.16
```
 
#### gspread / oauth2client
```
# 가상환경인 경우
pip3 install gspread
pip3 install --upgrade oauth2client
 
# 가상환경이 아닌 경우
pip install --user gspread
pip install --user --upgrade oauth2client
```
 
#### pytesseract
 
- https://github.com/UB-Mannheim/tesseract/wiki

##### osx

```


brew install tesseract


sudo chown -R macmini /usr/local/share/Library/Caches/Yarn/v4


brew install tesseract-lang

brew list tesseract



/usr/local/Cellar/tesseract/4.1.1/bin/tesseract
/usr/local/Cellar/tesseract-lang/4.0.0/share/tessdata/

```


```
pip install pytesseract
```
 
 
#### 
 
## Visual Studio Code