#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
브런치(Brunch) 스타일 1인칭 스토리 생성기
- 클릭률 높은 제목 5개 자동 생성
- 강력한 후킹이 있는 도입부
- 1인칭 감성 스토리텔링
- 복사-붙여넣기로 브런치에 바로 포스팅 가능
"""

import json
import random
from datetime import datetime
from typing import Dict, List, Optional


class BrunchStoryGenerator:
    """브런치용 1인칭 감성 스토리 생성기"""

    def __init__(self):
        self.story_themes = self._load_story_themes()

    def _load_story_themes(self) -> Dict:
        """스토리 주제 템플릿"""
        return {
            "인생역전": {
                "keywords": ["기회", "도전", "성공", "변화", "꿈"],
                "emotion": "희망적이고 감동적인",
                "topics": [
                    "50대에 다시 시작한 나의 인생 2막",
                    "퇴직 후 찾아온 진짜 나의 꿈",
                    "늦었다고 생각했을 때가 시작이었다",
                    "아무것도 없던 내가 여기까지 온 이야기"
                ]
            },
            "가족애": {
                "keywords": ["가족", "사랑", "화해", "이해", "용서"],
                "emotion": "따뜻하고 감동적인",
                "topics": [
                    "아버지와 20년 만에 나눈 진짜 대화",
                    "엄마가 남긴 편지를 읽고 깨달은 것",
                    "가족이라는 이름의 무게를 이제야 알았다",
                    "멀어졌던 형제가 다시 가까워진 이유"
                ]
            },
            "사랑": {
                "keywords": ["사랑", "만남", "인연", "그리움", "설렘"],
                "emotion": "설레고 감성적인",
                "topics": [
                    "30년 만에 다시 만난 첫사랑 이야기",
                    "50대에 찾아온 두 번째 사랑",
                    "평생 잊지 못할 그 사람에게",
                    "늦은 나이에 알게 된 사랑의 진짜 의미"
                ]
            },
            "성장": {
                "keywords": ["배움", "깨달음", "성장", "변화", "지혜"],
                "emotion": "진솔하고 공감되는",
                "topics": [
                    "실패가 내게 가르쳐준 것들",
                    "나를 바꾼 한 사람의 말",
                    "50년을 살아보니 정말 중요한 것은",
                    "후회 없는 인생을 사는 법을 깨달았다"
                ]
            },
            "일상": {
                "keywords": ["소소함", "행복", "감사", "순간", "일상"],
                "emotion": "잔잔하고 공감되는",
                "topics": [
                    "평범한 하루가 얼마나 소중한지 몰랐다",
                    "작은 것에 감사하게 된 이유",
                    "특별할 것 없는 오늘이 가장 특별했다",
                    "일상에서 찾은 작은 행복들"
                ]
            }
        }

    def generate_titles(self, theme: str, topic: str) -> List[str]:
        """클릭률 높은 제목 5개 생성"""
        theme_data = self.story_themes.get(theme, self.story_themes["인생역전"])
        keywords = theme_data["keywords"]

        # 제목 패턴별로 생성
        titles = []

        # 1. 숫자 + 후크 패턴
        numbers = ["50대", "60대", "30년", "20년", "10년"]
        number = random.choice(numbers)
        titles.append(f"{number} 만에 깨달은 것: {random.choice(keywords)}은 이런 것이었다")

        # 2. 질문형 패턴
        titles.append(f"당신도 {random.choice(keywords)}을 포기하고 있나요?")

        # 3. 고백형 패턴
        titles.append(f"솔직히 말하자면, {random.choice(keywords)} 때문에 울었습니다")

        # 4. 비포/애프터 패턴
        titles.append(f"{random.choice(keywords)}을 만나기 전과 후, 내 인생이 달라졌다")

        # 5. 스토리텔링 패턴
        titles.append(f"그날 나는 {random.choice(keywords)}을 선택했고, 모든 것이 바뀌었다")

        return titles

    def generate_hook_intro(self, theme: str, topic: str) -> str:
        """강력한 후킹이 있는 도입부 생성"""
        hooks = [
            {
                "start": "전화를 끊고 한참을 멍하니 앉아 있었다.",
                "context": "믿을 수 없는 소식이었다. 아니, 믿고 싶지 않았다.",
                "transition": "하지만 이것은 현실이었고, 나는 선택해야 했다."
            },
            {
                "start": "그날 아침, 거울을 보다가 문득 깨달았다.",
                "context": "\"아, 나는 지금까지 뭘 하며 살았던 걸까.\"",
                "transition": "50년을 살아왔지만, 처음 든 생각이었다."
            },
            {
                "start": "누군가 이런 말을 했다. 인생은 50부터라고.",
                "context": "그때는 위로로 들렸다. 하지만 지금은 안다.",
                "transition": "그 말이 위로가 아니라 진실이었다는 것을."
            },
            {
                "start": "손이 떨렸다.",
                "context": "30년 만에 받아든 편지였다. 보낸 사람을 보는 순간, 눈물이 났다.",
                "transition": "나는 편지를 펼쳤고, 그 안에서 내가 잃어버렸던 모든 것을 발견했다."
            },
            {
                "start": "\"이제 늦었어.\"",
                "context": "주변 사람들이 모두 말렸다. 나도 그렇게 생각했다.",
                "transition": "하지만 무언가가 나를 움직이게 했다. 아마도... 그것은 마지막 기회였기 때문이다."
            }
        ]

        hook = random.choice(hooks)

        intro = f"""
{hook['start']}

{hook['context']}

{hook['transition']}

---

"""
        return intro

    def generate_first_person_story(
        self,
        theme: str,
        topic: str,
        word_count: int = 3000
    ) -> str:
        """1인칭 감성 스토리 본문 생성"""

        sections = []

        # 1부: 과거 - 어떻게 시작되었나
        sections.append(self._generate_past_section(theme, topic))

        # 2부: 전환점 - 무엇이 나를 변화시켰나
        sections.append(self._generate_turning_point_section(theme, topic))

        # 3부: 과정 - 어떻게 극복했나
        sections.append(self._generate_process_section(theme, topic))

        # 4부: 현재 - 지금의 나
        sections.append(self._generate_present_section(theme, topic))

        # 5부: 메시지 - 당신에게 전하고 싶은 것
        sections.append(self._generate_message_section(theme, topic))

        return "\n\n---\n\n".join(sections)

    def _generate_past_section(self, theme: str, topic: str) -> str:
        """과거 회상 섹션"""
        pasts = [
            """## 그때의 나는

솔직히 말하면, 나는 평범한 사람이었다.

특별한 재능도 없었고, 대단한 학벌도 없었다. 그저 하루하루를 살아가는 것만으로도 벅찼다.

아침에 일어나면 출근하고, 일하고, 퇴근하고, 자는 것의 반복.

"이게 인생인가?" 하는 생각이 들 때도 많았다.

하지만 그때는 몰랐다. 변화는 예고 없이 찾아온다는 것을.""",

            """## 시작은 평범했다

돌이켜보면, 나도 한때는 꿈이 많았다.

젊었을 때는 세상을 다 가질 수 있을 것 같았다. 뭐든지 할 수 있을 것 같았다.

하지만 시간이 지나면서 하나둘씩 포기하게 되었다.

"나이가 들면 원래 그런 거야."
"현실적으로 생각해야지."

그렇게 나를 설득했다. 아니, 스스로를 속였다.""",

            """## 매일이 똑같았다

변화 없는 일상이 계속됐다.

기쁨도 없었지만, 그렇다고 큰 고통도 없었다. 그저 무덤덤하게 하루하루를 보냈다.

주변 사람들도 마찬가지였다. 모두 비슷하게 살고 있었다.

"다들 이렇게 사는 거야."

그렇게 생각하며 나 자신을 위로했다.

하지만 마음 한구석에는 늘 불편한 감정이 있었다."""
        ]

        return random.choice(pasts)

    def _generate_turning_point_section(self, theme: str, topic: str) -> str:
        """전환점 섹션"""
        turning_points = [
            """## 그날, 모든 것이 바뀌었다

그날은 평범한 화요일 오후였다.

특별할 것 없는, 여느 날과 다름없는 하루.

하지만 오후 3시 27분, 내 인생이 바뀌기 시작했다.

전화 한 통이었다. 아니, 어쩌면 그보다 더 작은 계기였을지도 모른다.

중요한 것은, 그 순간 나는 깨달았다.

**"이대로는 안 되겠다."**

더 이상 미룰 수 없었다. 더 이상 핑계 댈 수 없었다.""",

            """## 우연이라고 하기엔

어쩌면 우연이었을까.

아니면 필연이었을까.

그날 우연히 만난 한 사람. 우연히 들은 한마디.

"당신은 왜 그렇게 살고 있나요?"

낯선 사람의 질문이었다. 하지만 그 말이 내 가슴을 찔렀다.

나는 대답할 수 없었다.

왜? 왜 나는 이렇게 살고 있지?

그날 밤, 잠을 이룰 수 없었다.""",

            """## 더 이상은 안 되겠다고 생각했다

한계였다.

더 이상 참을 수 없었다. 더 이상 자신을 속일 수 없었다.

거울을 보며 물었다.

"너는 정말 행복하니?"
"너는 정말 원하는 삶을 살고 있니?"

대답은 침묵이었다.

그리고 그 침묵이 내 모든 것을 말해주고 있었다.

나는 결심했다. 변화해야 한다고."""
        ]

        return random.choice(turning_points)

    def _generate_process_section(self, theme: str, topic: str) -> str:
        """과정 섹션"""
        processes = [
            """## 쉽지 않았다

처음에는 확신이 있었다.

"이번에는 정말 바꿀 수 있어."

하지만 현실은 호락호락하지 않았다.

주변 사람들은 반대했다.

"그 나이에 무슨 짓이야."
"현실을 봐."
"실패하면 어떡하려고."

나 자신도 흔들렸다.

'정말 내가 할 수 있을까?'
'혹시 실수하는 건 아닐까?'

밤마다 고민했다. 눈물도 많이 흘렸다.

하지만 포기하지 않았다. 포기할 수 없었다.""",

            """## 하루하루가 전쟁이었다

매일이 도전이었다.

새벽에 일어나 준비하고, 하루 종일 부딪히고, 밤에는 반성하고.

실수도 많았다. 실패도 했다.

한 번은 너무 힘들어서 그만두려고 했다.

"역시 난 안 되는 사람인가 봐."

하지만 그때마다 떠올랐다.

**과거의 나로 돌아갈 수는 없다.**

그 생각이 나를 다시 일으켜 세웠다.""",

            """## 조금씩 변하기 시작했다

3개월쯤 지났을까.

변화가 보이기 시작했다.

작은 변화였다. 아주 작은.

하지만 분명히 달랐다.

주변 사람들도 알아차렸다.

"뭔가 달라졌네?"
"표정이 밝아졌어."

나 자신도 느꼈다.

거울 속의 내가 예전과 달랐다. 눈빛이 달랐다.

**"아, 나는 할 수 있구나."**

처음으로 확신이 들었다."""
        ]

        return random.choice(processes)

    def _generate_present_section(self, theme: str, topic: str) -> str:
        """현재 섹션"""
        presents = [
            """## 지금의 나는

지금도 완벽하지 않다.

여전히 실수하고, 여전히 고민한다.

하지만 예전과는 다르다.

이제는 안다. 실수는 배움의 과정이라는 것을. 고민은 성장의 증거라는 것을.

가장 큰 변화는 마음이었다.

예전에는 항상 불안했다. 항상 불만족스러웠다.

하지만 지금은 감사할 줄 안다. 지금 이 순간을 즐길 줄 안다.

**그것만으로도 충분히 행복하다.**""",

            """## 후회는 없다

돌이켜보면, 모든 것이 의미가 있었다.

힘들었던 순간들, 좌절했던 순간들, 포기하고 싶었던 순간들.

그 모든 것들이 나를 만들었다.

지금의 나는 과거의 모든 순간들이 모여서 만들어진 결과다.

그래서 후회하지 않는다.

실수도, 실패도, 고통도.

모두 내 인생의 일부였고, 그것들이 나를 더 강하게 만들었다.""",

            """## 행복의 의미를 알았다

행복이 뭔지 이제야 안다.

어릴 때는 행복이 큰 것인 줄 알았다. 성공, 명예, 돈.

하지만 아니었다.

행복은 작은 것들에 있었다.

아침에 눈을 떴을 때의 감사함.
사랑하는 사람과 함께하는 시간.
스스로 성장하고 있다는 뿌듯함.

그런 것들이 진짜 행복이었다.

그리고 나는 지금, 행복하다."""
        ]

        return random.choice(presents)

    def _generate_message_section(self, theme: str, topic: str) -> str:
        """메시지 섹션"""
        messages = [
            """## 당신에게 전하고 싶은 말

이 글을 읽는 당신에게 말하고 싶다.

**늦은 것은 없다.**

나이는 숫자일 뿐이다. 중요한 것은 지금 이 순간의 당신의 선택이다.

주변에서 뭐라고 하든, 당신이 원한다면 시작하라.

실패할 수도 있다. 힘들 수도 있다.

하지만 시도조차 하지 않는 것보다는 백배 낫다.

나는 당신이 용기를 내기를 바란다.

그리고 당신도 곧 깨닫게 될 것이다.

**변화는 생각보다 가까이에 있다는 것을.**

---

당신의 이야기는 무엇인가요?

댓글로 나눠주시면 함께 응원하겠습니다.""",

            """## 지금이라도 늦지 않았다

만약 당신이 지금 고민 중이라면.

만약 당신이 변화를 망설이고 있다면.

한 가지만 기억하라.

**가장 후회하는 것은 하지 않은 것이다.**

했다가 실패한 것이 아니다. 시도조차 하지 않은 것이다.

나도 그랬다. 오랫동안 망설였다.

"다음에", "나중에", "조금만 더 준비하면"

그렇게 시간만 흘러갔다.

하지만 시작하고 나니 깨달았다.

**시작이 반이 아니라, 시작이 전부였다.**

당신도 할 수 있다. 나도 했으니까.

함께 응원한다.""",

            """## 우리 모두의 이야기

이것은 나만의 이야기가 아니다.

우리 모두의 이야기다.

당신도, 나도, 우리 모두 비슷한 고민을 한다.

"나는 괜찮을까?"
"내 선택이 맞을까?"
"지금이라도 괜찮을까?"

괜찮다. 정답이다. 지금이 바로 그때다.

인생에 완벽한 타이밍은 없다.

**지금이 바로 가장 좋은 때다.**

함께 시작하자. 함께 변화하자.

그리고 언젠가, 당신도 이런 글을 쓰게 될 것이다.

"나도 할 수 있었다"고.

당신의 이야기를 기다린다."""
        ]

        return random.choice(messages)

    def generate_complete_brunch_post(
        self,
        theme: Optional[str] = None,
        topic: Optional[str] = None
    ) -> Dict[str, any]:
        """완전한 브런치 포스트 생성"""

        # 주제 선택
        if theme is None:
            theme = random.choice(list(self.story_themes.keys()))

        if topic is None:
            topics = self.story_themes[theme]["topics"]
            topic = random.choice(topics)

        # 제목 5개 생성
        titles = self.generate_titles(theme, topic)

        # 도입부 생성
        hook_intro = self.generate_hook_intro(theme, topic)

        # 본문 생성
        story = self.generate_first_person_story(theme, topic)

        # 완전한 포스트 조합
        post = {
            "metadata": {
                "theme": theme,
                "topic": topic,
                "generated_at": datetime.now().isoformat(),
                "platform": "Brunch"
            },
            "titles": titles,
            "recommended_title": titles[0],  # 첫 번째를 추천
            "content": hook_intro + story
        }

        return post

    def export_for_brunch(self, post: Dict, output_path: str):
        """브런치에 바로 복사-붙여넣기 가능한 형식으로 저장"""

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("  브런치 포스팅용 - 복사해서 바로 사용하세요\n")
            f.write("=" * 80 + "\n\n")

            f.write("【 추천 제목 5개 】\n\n")
            for i, title in enumerate(post['titles'], 1):
                if i == 1:
                    f.write(f"⭐ {i}. {title}  (가장 추천)\n\n")
                else:
                    f.write(f"   {i}. {title}\n\n")

            f.write("\n" + "-" * 80 + "\n\n")
            f.write("【 본문 - 아래부터 복사하세요 】\n\n")
            f.write("-" * 80 + "\n\n")

            # 추천 제목을 #으로 표시
            f.write(f"# {post['recommended_title']}\n\n")

            # 본문
            f.write(post['content'])

            f.write("\n\n" + "-" * 80 + "\n")
            f.write("【 복사 끝 】\n")
            f.write("-" * 80 + "\n")


def main():
    """메인 실행 함수"""
    print("=" * 80)
    print("  브런치(Brunch) 스타일 스토리 생성기")
    print("  1인칭 감성 글쓰기 / 제목 5개 추천 / 강력한 후킹")
    print("=" * 80)
    print()

    generator = BrunchStoryGenerator()

    print("스토리를 생성하고 있습니다...")
    print()

    # 포스트 생성
    post = generator.generate_complete_brunch_post()

    print(f"✓ 주제: {post['metadata']['topic']}")
    print(f"✓ 테마: {post['metadata']['theme']}")
    print()

    print("【 추천 제목 5개 】")
    for i, title in enumerate(post['titles'], 1):
        if i == 1:
            print(f"⭐ {i}. {title}  (가장 추천)")
        else:
            print(f"   {i}. {title}")
    print()

    # 파일 저장
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"output/brunch_post_{timestamp}.txt"

    generator.export_for_brunch(post, output_path)

    print(f"✓ 브런치 포스트가 생성되었습니다:")
    print(f"  {output_path}")
    print()
    print("파일을 열어서 내용을 복사한 후,")
    print("브런치 에디터에 바로 붙여넣기 하시면 됩니다!")
    print()
    print("=" * 80)


if __name__ == "__main__":
    main()
