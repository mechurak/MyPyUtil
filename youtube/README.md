# Youtube video 리스트 크롤러

## Usage

### 1. video id 리스트 확보

- `body.txt` 준비
  - URL = 'https://www.youtube.com/channel/UCSWPuzlD337Y6VBkyFPwT8g/videos'
  - Chrome 으로 위 사이트 들어가서, 맨 밑까지 스크롤
  - 개발자도구(F12) 로 `<body>` 부분 복사해서 `body.txt` 로 저장
- `video_list.py` 실행
  - video id를 가지는 `temp.csv` 파일 생성됨 
  
### 2. Youtube API 사용 준비

https://developers.google.com/youtube/v3/quickstart/python 의 내용 준비

- [Google API Console](https://console.developers.google.com/) 에서 프로젝트 생성
- 라이브러리에서 Youtube Data API 3.0 추가
- 사용자 인증 정보 에서 API key 와 OAuth 2.0 client ID 준비
- OAuth 동의 화면도 필요 했음. (`youtube.readonly` scope 도 추가)
- `client_secret.json` 다운 

### 3. 비디오별 상세 정보 확보
- `video_info.py` 실행
- `output.csv` 파일 생성됨
- 600 번 영상 제목에 `.` 찍어주자.

### 4. 제목 정제
- `title_divider.py` 실행
- `output2.csv` 파일 생성됨

