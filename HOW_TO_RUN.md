# 프로그램 실행 방법 완벽 가이드

## 어디서 실행하나요?

이 프로그램은 **여러 곳에서** 실행할 수 있습니다:

### 1️⃣ 지금 대화하는 이 채팅창 (Claude Code) ✅ **가장 쉬움**
- **바로 여기서** 실행 가능!
- 제가 이미 테스트해드렸어요
- 파일이 자동으로 저장됨

### 2️⃣ 내 컴퓨터 (Windows/Mac/Linux)
- Python만 설치하면 됨
- 터미널/명령 프롬프트에서 실행
- 내 컴퓨터에 파일 저장

### 3️⃣ VS Code (Visual Studio Code)
- 코드 에디터에서 실행
- 개발자라면 추천

### 4️⃣ 클로드 웹사이트 (claude.ai)
- 일반 채팅에서는 실행 안 됨
- 파일이 필요하므로 여기서 해야 함

---

## 지금 바로 실행하기 (가장 쉬운 방법)

### 브런치용 1인칭 스토리 생성

저한테 이렇게 말씀하시면 됩니다:

```
python src/brunch_story_generator.py 실행해줘
```

또는 제가 대신 실행해드릴게요!

**주제를 선택하고 싶으시면:**
- "인생역전 주제로 브런치 글 생성해줘"
- "가족애 테마로 감동적인 1인칭 스토리 만들어줘"
- "사랑 이야기로 브런치 포스팅 생성해줘"

---

## 내 컴퓨터에서 실행하는 법

### 준비물
- Python 3.7 이상 (무료)
- 이 프로젝트 파일들

### Windows에서 실행

#### 1단계: Python 설치 확인
```cmd
python --version
```

없다면: https://www.python.org/downloads/ 에서 다운로드

#### 2단계: 프로젝트 폴더로 이동
```cmd
cd C:\Users\내이름\Downloads\-pharma-template
```

#### 3단계: 실행!

**브런치 스토리 생성:**
```cmd
python src\brunch_story_generator.py
```

**유튜브 시니어 대본 생성:**
```cmd
python src\senior_youtube_script_generator.py
```

#### 4단계: 결과 확인
```cmd
dir output
notepad output\brunch_post_최신파일.txt
```

### Mac/Linux에서 실행

#### 1단계: Python 설치 확인
```bash
python3 --version
```

#### 2단계: 프로젝트 폴더로 이동
```bash
cd ~/Downloads/-pharma-template
```

#### 3단계: 실행!

**브런치 스토리 생성:**
```bash
python3 src/brunch_story_generator.py
```

**유튜브 시니어 대본 생성:**
```bash
python3 src/senior_youtube_script_generator.py
```

#### 4단계: 결과 확인
```bash
ls output/
cat output/brunch_post_최신파일.txt
```

---

## 두 가지 생성기 차이점

### 🎯 브런치 스토리 생성기 (신규!)
```bash
python src/brunch_story_generator.py
```

**특징:**
- ✅ 1인칭 감성 글쓰기
- ✅ 클릭률 높은 제목 5개 자동 생성
- ✅ 강력한 후킹 도입부
- ✅ 브런치에 복사-붙여넣기 바로 가능
- ✅ 3,000자 분량 (읽기 적당)

**용도:**
- 브런치 블로그 포스팅
- 미디엄, 네이버 블로그
- 감성 에세이
- SNS 긴 글

**생성 예시:**
```
제목: 50대에 다시 시작한 나의 인생 2막
길이: 약 3,000자
스타일: 1인칭 회고록
```

### 📺 유튜브 시니어 대본 생성기 (기본)
```bash
python src/senior_youtube_script_generator.py
```

**특징:**
- ✅ 김은숙 작가 스타일 스토리텔링
- ✅ 기승전결 구조
- ✅ 1시간 20분 ~ 2시간 분량
- ✅ 3인칭 서술
- ✅ 영상 대본 형식

**용도:**
- 유튜브 나레이션 대본
- 팟캐스트 스크립트
- 오디오북 대본
- 긴 형식 콘텐츠

**생성 예시:**
```
제목: 60대에 시작한 작은 가게가 대성공한 이야기
길이: 약 15,000자 (100분)
스타일: 3인칭 서술 + 대화
```

---

## Python 프로그래밍으로 사용하기

### 브런치 스토리 생성

```python
from brunch_story_generator import BrunchStoryGenerator

# 생성기 생성
generator = BrunchStoryGenerator()

# 완전한 포스트 생성 (주제 자동 선택)
post = generator.generate_complete_brunch_post()

# 특정 주제로 생성
post = generator.generate_complete_brunch_post(
    theme="인생역전",
    topic="50대에 다시 시작한 나의 인생 2막"
)

# 제목 확인
print("추천 제목 5개:")
for i, title in enumerate(post['titles'], 1):
    print(f"{i}. {title}")

# 파일로 저장
generator.export_for_brunch(post, "output/my_story.txt")
```

### 원하는 주제로 여러 개 생성

```python
from brunch_story_generator import BrunchStoryGenerator

generator = BrunchStoryGenerator()

themes = ["인생역전", "가족애", "사랑", "성장", "일상"]

for theme in themes:
    post = generator.generate_complete_brunch_post(theme=theme)
    generator.export_for_brunch(post, f"output/brunch_{theme}.txt")
    print(f"✓ {theme} 스토리 생성 완료")
```

---

## 자주 묻는 질문 (FAQ)

### Q1. Python이 없는데요?
**A:** 무료로 설치하세요!
- Windows: https://www.python.org/downloads/
- Mac: `brew install python3` (터미널에서)
- Linux: `sudo apt install python3`

### Q2. 에러가 나요: "python을 찾을 수 없습니다"
**A:** Python 설치 시 "Add Python to PATH" 체크했나요?
- 안 했다면 Python 재설치
- 또는 `python3` 대신 `py` 사용해보세요 (Windows)

### Q3. 한글이 깨져요
**A:** 파일을 UTF-8로 열어야 합니다
- 메모장 → 다른 이름으로 저장 → 인코딩: UTF-8
- VS Code, Sublime Text 등 사용 권장

### Q4. 파일이 어디 저장되나요?
**A:** `output/` 폴더에 저장됩니다
```bash
# Windows
dir output

# Mac/Linux
ls output/
```

### Q5. 제목을 바꾸고 싶어요
**A:** 생성된 txt 파일에 5개 제목이 있습니다
- 마음에 드는 것 선택
- 또는 조합해서 사용
- 또는 다시 생성 (실행할 때마다 새로운 제목)

### Q6. 내용을 수정할 수 있나요?
**A:** 당연히 가능합니다!
- txt 파일을 메모장이나 에디터로 열기
- 자유롭게 편집
- 브런치에 복사-붙여넣기

### Q7. 여러 개를 한 번에 만들고 싶어요
**A:** Python 코드로 반복 실행하시면 됩니다
```python
for i in range(10):  # 10개 생성
    post = generator.generate_complete_brunch_post()
    generator.export_for_brunch(post, f"output/story_{i+1}.txt")
```

### Q8. 상업적으로 사용 가능한가요?
**A:** 네! 자유롭게 사용하세요
- 블로그 포스팅
- 유튜브 대본
- 전자책 출판
- 모두 가능합니다

---

## 빠른 명령어 모음

### 브런치 스토리 1개 생성
```bash
python src/brunch_story_generator.py
```

### 유튜브 대본 1개 생성
```bash
python src/senior_youtube_script_generator.py
```

### 대화형 모드 (주제 선택 가능)
```bash
cd examples
python generate_sample_scripts.py
```

### 생성된 파일 목록 보기
```bash
# Windows
dir output

# Mac/Linux
ls -lh output/
```

### 가장 최신 파일 보기
```bash
# Windows
type output\brunch_post_*.txt | more

# Mac/Linux
cat output/brunch_post_*.txt
```

---

## 실전 사용 예시

### 예시 1: 일주일치 브런치 포스트 만들기

```python
from brunch_story_generator import BrunchStoryGenerator

generator = BrunchStoryGenerator()

# 월~일 7개 주제
themes = ["인생역전", "가족애", "사랑", "성장", "일상", "인생역전", "가족애"]
days = ["월", "화", "수", "목", "금", "토", "일"]

for day, theme in zip(days, themes):
    post = generator.generate_complete_brunch_post(theme=theme)
    generator.export_for_brunch(post, f"output/week_{day}요일.txt")
    print(f"✓ {day}요일 포스트 완성!")
```

### 예시 2: 제목만 100개 뽑기

```python
from brunch_story_generator import BrunchStoryGenerator

generator = BrunchStoryGenerator()

with open("output/titles_100.txt", "w", encoding="utf-8") as f:
    for i in range(100):
        titles = generator.generate_titles("인생역전", "샘플")
        f.write(f"\n=== 제목 세트 {i+1} ===\n")
        for title in titles:
            f.write(f"- {title}\n")
```

### 예시 3: 특정 주제로 여러 버전 만들기

```python
# "인생역전" 주제로 10가지 다른 스토리
for i in range(10):
    post = generator.generate_complete_brunch_post(theme="인생역전")
    generator.export_for_brunch(post, f"output/comeback_{i+1}.txt")
```

---

## 도움이 더 필요하시면

1. **README.md** 읽어보기
2. **QUICKSTART.md** 빠른 시작 가이드
3. **저한테 물어보기** - 제가 도와드릴게요!

---

## 지금 바로 시작하세요!

**가장 쉬운 방법:**

저한테 그냥 이렇게 말씀하세요:

> "브런치 스토리 하나 만들어줘"

제가 바로 실행해서 결과를 보여드리겠습니다!

**주제를 정하고 싶으시면:**

> "인생역전 주제로 브런치 글 만들어줘"
> "가족 이야기로 감동적인 1인칭 스토리 만들어줘"

**제목만 뽑고 싶으시면:**

> "클릭률 높은 제목 20개만 만들어줘"

---

**질문 있으시면 언제든 물어보세요!** 😊
