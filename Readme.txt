Code for Checking the KIPO CODE @ patent.go.kr



구동 조건

<ubuntu 초기 서버 기준>

0. python3 설치 & virtualenv 설치


1. requirement.txt 설치


2. manage.py 있는 dir에 chromedriver linux 실행파일(디렉토리 아님에 유의)을 복사

(다운로드) http://chromedriver.chromium.org/downloads

ex) ubuntu의 경우, /home/ubuntu/kipocode/kipocode/ 에 복하사면 됨. OS따라 위치 다를 수 있으므로, 참고만 할것.


3. 서버에 크롬이 설치되어 있지 않는 경우 별도 설치해야 함.(우분투기준)

1) 크롬 설치 파일 받기 

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

2) 파일로 설치

sudo apt-get -f install ./google-chrome-stable_current_amd64.deb


<독립적인 구동>

개별구동을 위하여 임시적으로 linux screen 명령어를 사용함

추후 배포 방법을 찾아야 함.

screen 명령어 : crtl+a 이후에 d

(터미널 종료 가능)

회복 : (이후 접속 후에) screen -r





