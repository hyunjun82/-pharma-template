# JJYU 계산기 - 대한민국 종합 계산기 사이트

애드센스 수익 최적화를 위한 한국형 종합 계산기 플랫폼입니다.

## 🎯 프로젝트 개요

- **목적**: 애드센스 광고 수익 창출을 위한 종합 계산기 사이트
- **타겟**: 대한민국 사용자 (금융, 생활, 건강, 수학 계산 필요자)
- **특징**: 60개 이상의 한국형 특화 계산기 제공

## 📁 프로젝트 구조

```
calculator/
├── index.html          # 메인 페이지 (계산기 목록)
├── css/
│   └── style.css      # 반응형 디자인 스타일
└── js/
    └── main.js        # 검색 기능 및 인터랙션
```

## ✨ 주요 기능

### 1. 💰 금융 계산기
- 대출 계산기 (월 상환액, 이자)
- 적금 계산기 (만기 금액)
- 예금 계산기
- 세금 계산기 (소득세, 부가세)
- 실수령액 계산기 (4대보험)
- 연금 계산기

### 2. 🏠 부동산 계산기
- 취득세 계산기
- 양도소득세 계산기
- 중개수수료 계산기
- 전세대출 계산기

### 3. 📅 생활 계산기
- 나이 계산기 (만 나이, 세는 나이)
- 디데이 계산기
- 음력 변환기
- 근무일수 계산기
- 띠 계산기
- 기념일 계산기

### 4. 💊 건강 계산기
- BMI 계산기
- 칼로리 계산기
- 체지방 계산기
- 배란일 계산기
- 출산예정일 계산기
- 당화혈색소 계산기

### 5. 🔢 수학/공학 계산기
- 기본 계산기
- 공학용 계산기
- 단위 변환기
- 평수 계산기 (평 ↔ m²)
- 퍼센트 계산기
- 평균 계산기

### 6. 💱 기타 계산기
- 환율 계산기
- 주유비 계산기
- 전기요금 계산기
- 가스요금 계산기
- 수도요금 계산기
- 팁 계산기 (더치페이)

## 🚀 애드센스 최적화

### 광고 배치 전략
1. **상단 배너** (728x90 또는 반응형)
2. **사이드바 광고** (160x600, PC만 표시)
3. **콘텐츠 중간 광고** (자동 크기)
4. **콘텐츠 내 광고** (in-article)
5. **하단 광고** (자동 relaxed)

### 수익 최적화 기능
- 광고 가시성 추적 (Intersection Observer)
- Google Analytics 연동 준비
- 사용자 행동 추적 (클릭, 노출)
- 모바일 최적화 (반응형)

## 📱 반응형 디자인

- **PC (1200px 이상)**: 사이드바 광고 표시
- **태블릿 (768px - 1199px)**: 그리드 레이아웃 조정
- **모바일 (768px 이하)**: 1열 레이아웃

## 🔍 SEO 최적화

### 메타태그
- 페이지 제목, 설명, 키워드
- Open Graph (소셜 미디어 공유)
- 구조화 데이터 (schema.org)

### 검색 엔진 최적화
- 시맨틱 HTML5
- 내부 링크 구조
- 키워드 밀도 최적화
- 콘텐츠 품질 (설명 텍스트)

## 🛠️ 설치 및 사용

### 1. 애드센스 설정
`calculator/index.html` 파일에서 다음을 수정하세요:

```html
<!-- YOUR_PUBLISHER_ID를 실제 애드센스 게시자 ID로 변경 -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-YOUR_PUBLISHER_ID"
     crossorigin="anonymous"></script>

<!-- YOUR_AD_SLOT_ID를 실제 광고 단위 ID로 변경 -->
<ins class="adsbygoogle"
     data-ad-client="ca-pub-YOUR_PUBLISHER_ID"
     data-ad-slot="YOUR_AD_SLOT_ID"></ins>
```

### 2. 로컬 테스트
```bash
# 간단한 HTTP 서버 실행 (Python)
cd calculator
python -m http.server 8000

# 브라우저에서 접속
http://localhost:8000
```

### 3. 배포
- GitHub Pages
- Netlify
- Vercel
- 또는 일반 웹 호스팅

## 🎨 커스터마이징

### 색상 변경
`calculator/css/style.css`에서 그라디언트 색상 수정:

```css
/* 메인 그라디언트 */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* 원하는 색상으로 변경 */
background: linear-gradient(135deg, #YOUR_COLOR1 0%, #YOUR_COLOR2 100%);
```

### 계산기 추가
`calculator/index.html`의 계산기 그리드에 카드 추가:

```html
<a href="/calculator/새계산기" class="calc-card">
    <div class="calc-icon">🎯</div>
    <h3>새 계산기</h3>
    <p>설명 텍스트</p>
</a>
```

## 📊 수익 극대화 팁

1. **트래픽 증가**
   - SEO 최적화
   - 소셜 미디어 공유
   - 블로그 백링크

2. **광고 최적화**
   - A/B 테스트
   - 광고 배치 실험
   - 클릭률 분석

3. **콘텐츠 확장**
   - 새 계산기 추가
   - 사용 가이드 작성
   - 관련 정보 제공

## 📝 라이선스

MIT License

## 🤝 기여

Pull Request 환영합니다!

## 📧 문의

- 웹사이트: https://jjyu.co.kr
- 이메일: contact@jjyu.co.kr