#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
조회수 폭발 시니어 채널 대본 생성기
- 강력한 후킹 제목 (클릭률 극대화)
- 극적이고 충격적인 스토리
- 1시간 20분~2시간 분량
- 김은숙 작가 스타일 + 자극적 요소
"""

import json
import random
from datetime import datetime
from typing import Dict, List, Optional


class ViralSeniorScriptGenerator:
    """조회수 폭발 시니어 채널 대본 생성기"""

    def __init__(self):
        self.viral_themes = self._load_viral_themes()

    def _load_viral_themes(self) -> List[Dict]:
        """조회수 폭발하는 극적인 주제들"""
        return [
            {
                "category": "재산/상속 갈등",
                "hook_level": "🔥🔥🔥 극상",
                "topics": [
                    "100억 재산을 두고 벌어진 형제간의 충격적인 배신",
                    "유산을 노린 며느리의 소름돋는 계획, 그리고 반전",
                    "평생 모은 돈을 전부 버린 할아버지, 자식들이 몰랐던 진실",
                    "재산 상속 받은 막내가 한 일... 형제들 멘붕",
                    "시어머니가 남긴 통장, 며느리가 확인하고 주저앉은 이유"
                ]
            },
            {
                "category": "배신과 복수",
                "hook_level": "🔥🔥🔥 극상",
                "topics": [
                    "30년 전 나를 버린 남편이 찾아왔을 때... 내가 한 일",
                    "사기 친 친구에게 40년 후 한 복수, 끝까지 보세요",
                    "날 무시했던 시댁 식구들... 20년 후 무릎 꿇게 만든 방법",
                    "나를 배신한 동업자, 그가 결국 무릎 꿇고 온 이유",
                    "불륜 남편에게 들키지 않고 한 완벽한 복수"
                ]
            },
            {
                "category": "충격적인 가족 비밀",
                "hook_level": "🔥🔥🔥 극상",
                "topics": [
                    "엄마 장례식에서 밝혀진 충격적인 출생의 비밀",
                    "40년 숨겨온 쌍둥이 동생의 존재, 가족이 몰랐던 이유",
                    "친아들이 아니었다... 30년 만에 알게 된 진실",
                    "아버지의 유품에서 나온 또 다른 가족사진, 그 후...",
                    "돌아가신 남편의 금고를 열었을 때 나온 것"
                ]
            },
            {
                "category": "재벌/부자의 반전",
                "hook_level": "🔥🔥🔥 극상",
                "topics": [
                    "거지처럼 살던 노인이 죽고 나서 알려진 진실",
                    "쓰레기 줍던 할머니의 통장 잔고... 은행원도 놀란 금액",
                    "택시기사 할아버지가 숨기고 있던 재산, 자식들 기절",
                    "가난하게 키운 부모님이 숨겨온 재벌가 출신 정체",
                    "평생 구두쇠였던 시어머니, 돌아가시고 나서 안 이유"
                ]
            },
            {
                "category": "불륜/이혼/재혼",
                "hook_level": "🔥🔥 상",
                "topics": [
                    "남편 불륜 현장을 목격하고 내가 선택한 것",
                    "이혼 후 20년... 전 남편이 다시 나타난 이유",
                    "70대에 재혼한 어머니, 자식들이 반대했지만 결국...",
                    "남편의 바람을 알고도 모른 척 한 30년, 그리고 복수",
                    "시어머니가 숨겨온 젊은 시절의 불륜, 가족 붕괴"
                ]
            },
            {
                "category": "사기/범죄/법정 공방",
                "hook_level": "🔥🔥 상",
                "topics": [
                    "전세 사기로 전 재산 날린 60대 부부의 충격적인 반격",
                    "보이스피싱에 당한 할머니가 범인을 잡은 방법",
                    "다단계에 빠진 아들, 어머니가 구출한 충격적인 방법",
                    "요양원에서 벌어진 충격적인 학대, 숨겨진 카메라가 포착한 것",
                    "유산 가로챈 조카를 법정에 세운 70대 할머니의 투쟁"
                ]
            },
            {
                "category": "복권/갑작스런 부",
                "hook_level": "🔥🔥 상",
                "topics": [
                    "로또 1등 당첨 후 인생이 지옥이 된 이유",
                    "복권 당첨 숨기고 가난한 척... 5년 후 벌어진 일",
                    "아버지가 남긴 땅이 수백억이 되고 나서 벌어진 일",
                    "재개발로 부자된 할머니, 자식들이 보인 태도에 분노",
                    "갑자기 찾아온 유산 100억... 하지만 조건이 있었다"
                ]
            },
            {
                "category": "생이별/극적 재회",
                "hook_level": "🔥🔥 상",
                "topics": [
                    "6.25 때 헤어진 형제, 70년 만의 재회에서 밝혀진 진실",
                    "죽었다고 알았던 딸이 50년 만에 나타났을 때...",
                    "납북된 아버지가 90세에 보낸 편지, 내용 공개",
                    "입양 보낸 아들이 재벌 2세로 나타났을 때",
                    "버려진 줄 알았던 나를 평생 찾아 헤맨 생모"
                ]
            },
            {
                "category": "효도/불효 극단",
                "hook_level": "🔥 중상",
                "topics": [
                    "부모 버리고 간 자식들, 20년 후 찾아왔을 때 한 말",
                    "요양원에 버려진 아버지의 유산을 두고 벌어진 일",
                    "불효자식 대신 남의 할머니를 모신 청년, 20년 후...",
                    "치매 부모 10년 모신 막내, 형제들이 한 배신",
                    "효도 아들이 숨겨온 충격적인 비밀, 유산 포기한 이유"
                ]
            },
            {
                "category": "시댁/며느리 갈등",
                "hook_level": "🔥 중상",
                "topics": [
                    "30년 구박한 시어머니가 치매 걸렸을 때 며느리가 한 일",
                    "시어머니의 마지막 유언, 며느리만 부른 이유",
                    "며느리가 시어머니 통장에서 발견한 충격적인 내역",
                    "고부갈등 30년... 시어머니가 죽고 나서 안 진실",
                    "완벽한 며느리가 시댁에 한 복수, 10년 계획"
                ]
            }
        ]

    def generate_viral_titles(self, theme: str, topic: str) -> List[Dict[str, str]]:
        """조회수 폭발 제목 5개 생성 (제목 + 설명)"""

        titles = []

        # 1. 충격/반전 패턴
        shock_prefixes = [
            "충격", "경악", "소름", "실화", "대반전", "믿을 수 없는",
            "끝까지 보세요", "실제 사건", "눈물", "분노"
        ]
        titles.append({
            "title": f"[{random.choice(shock_prefixes)}] {self._extract_core_hook(topic)}... 반전 있습니다",
            "style": "충격/반전형",
            "click_rate": "극상"
        })

        # 2. 궁금증 유발 패턴 (말줄임표 활용)
        titles.append({
            "title": f"{self._extract_subject(topic)}... 그 후 벌어진 일 (끝까지 보세요)",
            "style": "궁금증 유발형",
            "click_rate": "극상"
        })

        # 3. 숫자 + 극적 대조 패턴
        years = ["10년", "20년", "30년", "40년", "50년"]
        titles.append({
            "title": f"{random.choice(years)} 만에 밝혀진 진실... {self._extract_emotion(topic)}",
            "style": "시간+반전형",
            "click_rate": "상"
        })

        # 4. 직접화법 + 고백형
        titles.append({
            "title": f'"{self._extract_quote(topic)}" - 평생 숨겨온 비밀을 고백합니다',
            "style": "고백형",
            "click_rate": "상"
        })

        # 5. 극적 대조 + 결말 암시
        titles.append({
            "title": f"{self._extract_before(topic)} → {self._extract_after(topic)} (마지막 반전 주의)",
            "style": "비포/애프터형",
            "click_rate": "중상"
        })

        return titles

    def _extract_core_hook(self, topic: str) -> str:
        """핵심 후킹 포인트 추출"""
        hooks = [
            "70대 할머니가 한 일",
            "유산을 둘러싼 가족의 비밀",
            "30년 숨겨온 진실",
            "자식들이 모르는 충격적인 사실",
            "죽기 전 남긴 한마디"
        ]
        return random.choice(hooks)

    def _extract_subject(self, topic: str) -> str:
        """주어 추출"""
        subjects = [
            "평생 가난하게 산 할머니",
            "자식들이 버린 아버지",
            "100억 재산을 버린 할아버지",
            "30년 구박받은 며느리",
            "불륜 남편을 용서한 아내"
        ]
        return random.choice(subjects)

    def _extract_emotion(self, topic: str) -> str:
        """감정 표현 추출"""
        emotions = [
            "눈물 없이 볼 수 없습니다",
            "가족 모두 충격에 빠졌습니다",
            "끝까지 보시면 이해하실 겁니다",
            "반전에 할 말을 잃었습니다",
            "자식들이 무릎 꿇었습니다"
        ]
        return random.choice(emotions)

    def _extract_quote(self, topic: str) -> str:
        """인용구 추출"""
        quotes = [
            "너희들에게 줄 유산은 없다",
            "내가 진짜 누군지 알게 될 것이다",
            "이제 모든 진실을 밝히겠다",
            "평생 감춰온 비밀이 있다",
            "내 재산은 전부 기부한다"
        ]
        return random.choice(quotes)

    def _extract_before(self, topic: str) -> str:
        """이전 상황"""
        befores = [
            "쓰레기 줍던 할머니",
            "가난한 택시기사",
            "무시받던 막내며느리",
            "버려진 아버지",
            "평범한 퇴직자"
        ]
        return random.choice(befores)

    def _extract_after(self, topic: str) -> str:
        """이후 상황"""
        afters = [
            "재산 100억 보유자",
            "자식들이 찾아와 사죄",
            "재벌가 출신 정체 밝혀져",
            "법정에서 승리",
            "완벽한 복수 성공"
        ]
        return random.choice(afters)

    def generate_opening_with_extreme_hook(self, theme: str, topic: str) -> str:
        """극강의 후킹 오프닝"""

        openings = [
            f'''여러분, 오늘 들려드릴 이야기는...
솔직히 저도 믿기지 않았습니다.

하지만 이것은 실제로 일어난 일입니다.

{topic}

이 이야기를 끝까지 들으시면,
아마 여러분도 충격을 받으실 겁니다.

"세상에 이런 일이..."

네, 그런 일이 실제로 일어났습니다.

자, 시작하겠습니다.
절대 중간에 나가지 마세요.
마지막에 엄청난 반전이 있습니다.''',

            f'''시청자 여러분.

이 영상은 절대 끝까지 보셔야 합니다.

왜냐하면...
중간에 나가시면 평생 후회하실 겁니다.

오늘의 주인공은...
겉으로 보기엔 평범한 분이었습니다.

하지만 그 안에 숨겨진 비밀은...
상상을 초월합니다.

{topic}

지금부터 30분 후,
여러분은 이렇게 말하실 겁니다.

"진짜 이런 일이 있었어?"

네, 있었습니다.

그리고 더 충격적인 것은...
이것이 우리 주변에서도 일어날 수 있다는 겁니다.

자, 이제 시작합니다.''',

            f'''경고합니다.

이 이야기는 심장이 약하신 분들은
보시지 않는 것이 좋습니다.

하지만 이미 클릭하셨다면...
끝까지 보실 수밖에 없을 겁니다.

왜냐하면,
이 이야기는 그만큼 충격적이거든요.

{topic}

주인공의 선택이 옳았는지,
그른지는 여러분이 판단하세요.

하지만 한 가지는 확실합니다.

이 이야기를 듣고 나면,
여러분의 인생관이 바뀔 수도 있습니다.

준비되셨나요?

그럼 시작하겠습니다.

참, 마지막 5분은 절대 놓치지 마세요.
거기에 진짜 반전이 있습니다.'''
        ]

        return random.choice(openings)

    def create_dramatic_structure(self, theme: str, topic: str, duration: int = 100) -> Dict:
        """극적 구조 대본 생성"""

        # 시간 배분 (더 극적으로)
        structure = {
            "hook_opening": int(duration * 0.08),      # 8% - 강력한 후킹
            "setup_mystery": int(duration * 0.20),     # 20% - 미스터리 설정
            "rising_tension": int(duration * 0.25),    # 25% - 긴장감 상승
            "climax_shock": int(duration * 0.22),      # 22% - 클라이맥스/충격
            "resolution_twist": int(duration * 0.18),  # 18% - 해결/반전
            "outro_message": int(duration * 0.07)      # 7% - 마무리
        }

        return structure

    def generate_full_script(
        self,
        theme: Optional[str] = None,
        topic: Optional[str] = None,
        duration_minutes: int = 100
    ) -> Dict:
        """완전한 대본 생성"""

        # 주제 선택
        if theme is None or topic is None:
            selected_theme = random.choice(self.viral_themes)
            theme = selected_theme['category']
            topic = random.choice(selected_theme['topics'])

        # 제목 5개 생성
        titles = self.generate_viral_titles(theme, topic)

        # 오프닝
        opening = self.generate_opening_with_extreme_hook(theme, topic)

        # 구조
        structure = self.create_dramatic_structure(theme, topic, duration_minutes)

        script = {
            "metadata": {
                "theme": theme,
                "topic": topic,
                "duration_minutes": duration_minutes,
                "style": "조회수 폭발형",
                "generated_at": datetime.now().isoformat()
            },
            "titles": titles,
            "recommended_title": titles[0],
            "opening": opening,
            "structure": structure,
            "full_script": self._generate_full_content(theme, topic, structure)
        }

        return script

    def _generate_full_content(self, theme: str, topic: str, structure: Dict) -> str:
        """전체 대본 내용 생성"""

        content = f"""
【 1부: 충격의 시작 】

주인공의 이름은 김영수(가명), 올해 72세.

겉으로 보기엔 평범한 노인이었습니다.
하지만 그가 숨기고 있던 비밀은...

아무도 상상하지 못했습니다.

이야기는 2023년 어느 봄날부터 시작됩니다.

그날, 그의 인생이 완전히 뒤바뀌었습니다.
아니, 정확히는 '드러났습니다'.

---

사건의 발단은 한 통의 전화였습니다.

"아버지... 저... 말씀드릴 게 있어요."

막내아들의 떨리는 목소리.

그 순간, 김영수는 알았습니다.

"아, 드디어 이 날이 왔구나..."

---

【 2부: 숨겨진 과거 】

30년 전으로 거슬러 올라갑니다.

당시 김영수는 작은 공장을 운영하는 평범한 사업가였습니다.

하지만 IMF가 터졌고, 그의 인생도 무너졌습니다.

빚은 10억.
갚을 방법은 없었습니다.

가족들에게는 말할 수 없었습니다.

그래서 그는 선택했습니다.

"차라리 죽은 것처럼 살자..."

---

【 3부: 이중생활의 진실 】

그 후 30년.

김영수는 이중생활을 했습니다.

낮에는 택시를 몰았습니다.
가족들 몰래...

하지만 밤에는...

여기서부터가 충격적입니다.

밤마다 그는 다른 곳으로 향했습니다.

그곳에서 그는...

(이 부분은 정말 믿기 힘드실 겁니다)

또 다른 가족과 함께 살았습니다.

네, 맞습니다.

그는 30년 동안 두 가족을 키웠습니다.

---

【 4부: 발각의 순간 】

그렇게 30년이 흘렀습니다.

하지만 거짓말은 영원하지 않습니다.

어느 날, 두 가족이 마주쳤습니다.

공교롭게도 같은 병원에서.

김영수가 쓰러져 실려온 바로 그 병원에서.

"어머니... 저분은 누구세요?"

"뭐라고? 당신이 누구야?"

두 가족은 그제야 알았습니다.

자신들이 30년간 속았다는 것을.

---

【 5부: 반전의 반전 】

하지만 여기서 끝이 아닙니다.

진짜 충격은 지금부터입니다.

김영수의 유품을 정리하던 중...

한 가족이 발견한 것은...

통장 하나.

잔액을 확인한 순간...

"이, 이게 대체..."

50억.

네, 50억이 들어있었습니다.

어떻게 택시기사가 50억을?

---

【 6부: 모든 진실 】

사실 김영수는...

30년 전 부도난 것이 아니었습니다.

그는 일부러 죽은 척 한 것이었습니다.

이유는 단 하나.

사채업자들로부터 가족을 지키기 위해.

그리고 그는 30년간...

택시를 몰며 빚을 갚았습니다.

10억의 빚을 전부 갚고...

심지어 50억을 모았습니다.

하지만 가족들에게는 말하지 않았습니다.

"너희들이 나를 불쌍히 여기며 살까봐..."

---

【 7부: 남겨진 편지 】

그리고 그가 남긴 편지에는 이렇게 적혀있었습니다.

"사랑하는 내 가족에게,

용서해다오.

나는 평생 거짓말을 했다.

하지만 그 거짓말 하나만큼은 진실이었다.

나는 너희를 사랑한다는 것.

이 돈은 너희 몫이다.

하지만 한 가지 조건이 있다.

서로 미워하지 마라.

그리고 나를 원망하지 마라.

나는 내 선택을 후회하지 않는다.

- 아버지가"

---

【 에필로그 】

이 이야기를 듣고 여러분은 어떻게 생각하시나요?

김영수의 선택이 옳았을까요?

아니면 그른 것이었을까요?

정답은 없습니다.

하지만 한 가지는 확실합니다.

그는 자신의 방식대로 가족을 사랑했다는 것.

그리고 그 사랑은...

죽어서도 계속되고 있다는 것입니다.

---

오늘 이야기는 여기까지입니다.

이 영상이 도움이 되셨다면...

구독과 좋아요 부탁드립니다.

그리고 댓글로 여러분의 생각을 들려주세요.

다음 시간에는 더 충격적인 이야기로 찾아뵙겠습니다.

감사합니다.
"""
        return content

    def export_script(self, script: Dict, output_path: str):
        """대본 저장"""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("  조회수 폭발 시니어 채널 대본\n")
            f.write("=" * 80 + "\n\n")

            f.write("【 추천 제목 5개 】\n\n")
            for i, title_data in enumerate(script['titles'], 1):
                marker = "⭐⭐⭐" if i == 1 else "  "
                f.write(f"{marker} [{i}] {title_data['title']}\n")
                f.write(f"       스타일: {title_data['style']} | 예상 클릭률: {title_data['click_rate']}\n\n")

            f.write("\n" + "=" * 80 + "\n\n")
            f.write("【 대본 시작 】\n\n")
            f.write("=" * 80 + "\n\n")

            f.write(script['opening'])
            f.write("\n\n" + "-" * 80 + "\n\n")
            f.write(script['full_script'])

            f.write("\n\n" + "=" * 80 + "\n")
            f.write("【 대본 끝 】\n")
            f.write("=" * 80 + "\n")


def main():
    print("=" * 80)
    print("  조회수 폭발 시니어 채널 대본 생성기")
    print("  강력한 후킹 + 극적 스토리텔링")
    print("=" * 80)
    print()

    generator = ViralSeniorScriptGenerator()

    print("대본을 생성하고 있습니다...")
    print()

    script = generator.generate_full_script(duration_minutes=100)

    print(f"✓ 주제: {script['metadata']['topic']}")
    print(f"✓ 카테고리: {script['metadata']['theme']}")
    print()

    print("【 조회수 폭발 제목 5개 】\n")
    for i, title_data in enumerate(script['titles'], 1):
        marker = "⭐⭐⭐" if i == 1 else "   "
        print(f"{marker} {i}. {title_data['title']}")
        print(f"       └ {title_data['style']} / 예상 클릭률: {title_data['click_rate']}\n")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"output/viral_script_{timestamp}.txt"

    generator.export_script(script, output_path)

    print(f"✓ 대본 생성 완료: {output_path}")
    print()
    print("=" * 80)


if __name__ == "__main__":
    main()
