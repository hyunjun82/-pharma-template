# 빠른 시작 가이드

## 5분 안에 시작하기

### 1단계: 기본 대본 생성

가장 간단한 방법으로 대본을 생성해봅시다:

```bash
python src/senior_youtube_script_generator.py
```

이 명령어 하나로:
- 랜덤 주제가 자동 선택됩니다
- 100분(1시간 40분) 분량의 대본이 생성됩니다
- output/ 폴더에 TXT, JSON, MD 형식으로 저장됩니다

### 2단계: 대화형 모드로 원하는 대본 만들기

더 세밀한 제어가 필요하다면:

```bash
cd examples
python generate_sample_scripts.py
```

메뉴에서 **1번 (대화형 모드)**를 선택하세요.

그러면:
1. 주제 카테고리를 선택할 수 있습니다
2. 구체적인 주제를 고를 수 있습니다
3. 대본 길이를 정할 수 있습니다 (80~180분)

### 3단계: 생성된 대본 확인

```bash
ls output/
```

생성된 파일을 확인하고 원하는 편집기로 열어보세요:

```bash
# 텍스트 파일 보기
cat output/senior_script_*.txt

# 또는 에디터로 열기
nano output/senior_script_*.txt
```

## 자주 사용하는 명령어

### 특정 주제로 대본 생성

Python 스크립트에서:

```python
from senior_youtube_script_generator import SeniorScriptGenerator

generator = SeniorScriptGenerator()

# 인생역전 스토리 생성
script = generator.generate_script(
    theme="인생역전",
    topic="60대에 시작한 작은 가게가 대성공한 이야기",
    duration_minutes=100
)

# 파일로 저장
generator.export_script(script, "output/my_script.txt", 'txt')
```

### 여러 개의 대본 한번에 생성

```bash
cd examples
python generate_sample_scripts.py
# 5번 선택 → 랜덤 주제로 3개 생성
```

## 주제 선택 가이드

### 시청자 반응이 좋은 주제

1. **가족애** - 특히 재회, 화해 이야기
   - "30년 만에 만난 형제의 눈물겨운 재회"
   - "가출한 딸을 10년 동안 기다린 어머니의 사랑"

2. **인생역전** - 희망과 도전의 메시지
   - "60대에 시작한 작은 가게가 대성공한 이야기"
   - "평생 가난했던 농부가 발명가가 된 감동 스토리"

3. **사랑** - 로맨틱하고 감동적인
   - "50년 전 헤어진 첫사랑과의 운명적 재회"
   - "배우자를 잃은 후 다시 찾은 황혼의 사랑"

### 콘텐츠 길이 가이드

- **80분** (1시간 20분)
  - 간결하고 임팩트 있는 스토리
  - 시니어 청중의 집중력 고려
  - 빠른 전개를 원할 때

- **100분** (1시간 40분) ⭐ **추천**
  - 균형잡힌 스토리텔링
  - 감정 몰입과 전개의 밸런스
  - 대부분의 유튜브 채널에 적합

- **120분** (2시간)
  - 깊이 있는 감동 스토리
  - 여러 에피소드 포함 가능
  - 팟캐스트나 긴 형식 선호 시

## 예제 사용 시나리오

### 시나리오 1: 일주일치 콘텐츠 제작

```python
from senior_youtube_script_generator import SeniorScriptGenerator

generator = SeniorScriptGenerator()

weekly_themes = [
    ("인생역전", "60대에 시작한 작은 가게가 대성공한 이야기"),
    ("가족애", "30년 만에 만난 형제의 눈물겨운 재회"),
    ("우정", "50년 우정을 지켜온 친구들의 감동 실화"),
    ("사랑", "50년 전 헤어진 첫사랑과의 운명적 재회"),
    ("지혜와교훈", "가난을 극복하고 성공한 기업인의 인생 철학")
]

for i, (theme, topic) in enumerate(weekly_themes, 1):
    script = generator.generate_script(
        theme=theme,
        topic=topic,
        duration_minutes=100
    )

    generator.export_script(script, f"output/week1_day{i}.txt", 'txt')
    generator.export_script(script, f"output/week1_day{i}.md", 'md')

    print(f"✓ Day {i} 완료: {topic}")
```

### 시나리오 2: 특별 기획 시리즈

```python
# 한국전쟁 특집 시리즈
war_topics = [
    "전쟁 중 목숨을 구해준 전우와의 재회",
    "한국전쟁을 겪으며 배운 생존의 지혜",
    "전쟁으로 갈라선 연인의 70년 만의 상봉"
]

for i, topic in enumerate(war_topics, 1):
    script = generator.generate_script(
        theme="역사와추억",
        topic=topic,
        duration_minutes=120  # 특별 기획이므로 2시간
    )
    generator.export_script(script, f"output/war_series_ep{i}.txt", 'txt')
```

## 문제 해결

### Python이 실행되지 않아요

Python이 설치되어 있는지 확인:

```bash
python --version
# 또는
python3 --version
```

Python이 없다면:
- Windows: https://www.python.org/downloads/
- Mac: `brew install python3`
- Linux: `sudo apt install python3`

### 한글이 깨져요

파일을 UTF-8 인코딩으로 열어야 합니다:

```bash
# Linux/Mac
cat output/senior_script_*.txt

# Windows
type output\senior_script_*.txt
```

에디터 설정에서 UTF-8 인코딩 확인하세요.

### 대본이 너무 짧거나 길어요

`duration_minutes` 값을 조정하세요:

```python
# 짧게 (80분)
script = generator.generate_script(duration_minutes=80)

# 길게 (120분)
script = generator.generate_script(duration_minutes=120)

# 맞춤 (150분)
script = generator.generate_script(duration_minutes=150)
```

## 다음 단계

1. **README.md**를 읽어보세요 - 전체 기능 설명
2. **주제를 커스터마이징**하세요 - 내 채널에 맞는 주제 추가
3. **대본을 편집**하세요 - 실제 사연과 통계 추가
4. **피드백을 반영**하세요 - 시청자 반응에 따라 조정

## 유용한 팁

### Markdown 파일을 활용하세요

`.md` 파일은:
- 노션(Notion)에서 바로 임포트 가능
- GitHub에서 예쁘게 렌더링
- 다른 도구로 쉽게 변환 (Word, PDF 등)

### JSON 파일로 데이터 관리

`.json` 파일은:
- 프로그래밍으로 쉽게 처리 가능
- 메타데이터 포함 (주제, 길이 등)
- 다른 시스템과 연동 용이

### 실제 활용 시 추가할 것들

생성된 대본에 추가하면 좋은 요소:
- 실제 인터뷰나 증언
- 역사적 사실과 통계
- 관련 사진이나 영상 자료
- 현재 상황 업데이트
- 시청자 댓글이나 사연

---

**5분 안에 시작할 수 있습니다. 지금 바로 시도해보세요!**

```bash
python src/senior_youtube_script_generator.py
```
