#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
유튜브 시니어 채널 대본 생성기
김은숙 작가 스타일의 스토리텔링으로 1시간 20분~2시간 분량의 흥미로운 대본 생성
"""

import json
import random
from datetime import datetime
from typing import Dict, List, Optional


class SeniorScriptGenerator:
    """시니어 채널용 스토리텔링 대본 생성기"""

    def __init__(self):
        self.story_templates = self._load_story_templates()
        self.themes = self._load_themes()

    def _load_story_templates(self) -> Dict:
        """스토리 템플릿 로드"""
        return {
            "인생역전": {
                "기": "평범하거나 힘든 삶을 살아온 주인공의 일상과 배경 소개",
                "승": "예상치 못한 기회나 만남이 찾아오고, 조금씩 변화가 시작됨",
                "전": "큰 시련이나 선택의 순간을 맞이하며 갈등이 최고조에 달함",
                "결": "주인공이 지혜와 용기로 난관을 극복하고 새로운 삶을 찾음"
            },
            "가족애": {
                "기": "가족 간의 오해나 단절로 시작하는 일상적인 상황 묘사",
                "승": "작은 사건을 통해 서로를 이해하기 시작하는 계기가 생김",
                "전": "과거의 상처나 비밀이 드러나며 큰 갈등 상황 발생",
                "결": "진심 어린 대화와 용서로 가족애를 회복하고 화해하는 감동"
            },
            "우정": {
                "기": "오랜 친구 또는 새로운 만남으로 시작되는 관계 형성",
                "승": "함께하는 시간이 늘어나고 서로에게 힘이 되어주는 모습",
                "전": "오해나 배신, 질투로 인한 관계의 위기 상황",
                "결": "진정한 우정의 가치를 깨닫고 더욱 돈독해지는 관계"
            },
            "도전과성취": {
                "기": "새로운 꿈을 갖게 되거나 도전 욕구가 생기는 계기",
                "승": "첫 발걸음을 내딛고 작은 성공을 경험하며 자신감 상승",
                "전": "주변의 반대와 현실적 어려움으로 좌절의 순간",
                "결": "포기하지 않고 끝까지 노력하여 목표를 달성하는 감동"
            },
            "사랑": {
                "기": "운명적인 만남 또는 재회로 시작되는 감정의 씨앗",
                "승": "서로에게 끌리며 사랑을 확인하는 달콤한 시간",
                "전": "신분 차이, 오해, 또는 외부 방해로 인한 갈등",
                "결": "진정한 사랑의 힘으로 모든 장애물을 극복하고 맺어짐"
            },
            "지혜와교훈": {
                "기": "인생의 중요한 교훈을 담은 과거 이야기 시작",
                "승": "주인공이 경험을 통해 조금씩 성장하는 과정",
                "전": "큰 실수나 시련을 겪으며 깨달음의 순간을 맞이",
                "결": "얻은 지혜를 나누며 청취자들에게 감동과 교훈 전달"
            }
        }

    def _load_themes(self) -> List[Dict]:
        """시니어들이 공감할 수 있는 다양한 주제들"""
        return [
            {
                "category": "인생역전",
                "topics": [
                    "60대에 시작한 작은 가게가 대성공한 이야기",
                    "평생 가난했던 농부가 발명가가 된 감동 스토리",
                    "실직 후 새로운 인생을 찾은 중년의 도전기",
                    "말년에 숨겨진 재능을 발견한 할머니의 이야기"
                ]
            },
            {
                "category": "가족애",
                "topics": [
                    "30년 만에 만난 형제의 눈물겨운 재회",
                    "치매 부모를 모시는 자식들의 아름다운 사랑",
                    "세대 차이를 극복한 할아버지와 손자의 우정",
                    "가출한 딸을 10년 동안 기다린 어머니의 사랑"
                ]
            },
            {
                "category": "우정",
                "topics": [
                    "50년 우정을 지켜온 친구들의 감동 실화",
                    "노인정에서 만난 새로운 친구와의 특별한 인연",
                    "전쟁 중 목숨을 구해준 전우와의 재회",
                    "젊은 시절 라이벌이었던 두 사람의 늦은 화해"
                ]
            },
            {
                "category": "도전과성취",
                "topics": [
                    "70세에 대학교에 입학한 할머니의 도전기",
                    "퇴직 후 세계여행을 떠난 부부의 모험담",
                    "평생 꿈이었던 책을 출간한 할아버지 이야기",
                    "80세에 마라톤 완주에 성공한 노인의 열정"
                ]
            },
            {
                "category": "사랑",
                "topics": [
                    "50년 전 헤어진 첫사랑과의 운명적 재회",
                    "배우자를 잃은 후 다시 찾은 황혼의 사랑",
                    "전쟁으로 갈라선 연인의 70년 만의 상봉",
                    "계급 차이를 극복한 1960년대의 비밀 연애"
                ]
            },
            {
                "category": "지혜와교훈",
                "topics": [
                    "한국전쟁을 겪으며 배운 생존의 지혜",
                    "가난을 극복하고 성공한 기업인의 인생 철학",
                    "시골 할머니가 전하는 세상을 사는 지혜",
                    "평생 교사로 살며 깨달은 교육의 진정한 의미"
                ]
            },
            {
                "category": "역사와추억",
                "topics": [
                    "1960년대 서울의 변화를 목격한 택시기사 이야기",
                    "새마을운동 시절의 농촌 개발 실화",
                    "광복 직후 혼란기를 살아낸 가족의 이야기",
                    "경제개발 시대 산업역군들의 땀과 눈물"
                ]
            },
            {
                "category": "극복과회복",
                "topics": [
                    "불치병을 이겨낸 할아버지의 긍정 에너지",
                    "사업 실패 후 재기에 성공한 사업가 이야기",
                    "자녀를 잃은 슬픔을 봉사로 승화시킨 부모",
                    "장애를 극복하고 화가가 된 노인의 열정"
                ]
            }
        ]

    def _create_opening(self, theme: str, topic: str) -> str:
        """오프닝 멘트 생성 (5-7분 분량)"""
        openings = [
            f"""안녕하세요, 여러분. 오늘도 찾아주셔서 감사합니다.

오늘 여러분께 들려드릴 이야기는 정말 특별합니다.
{topic}에 대한 이야기인데요,
이 이야기를 들으시면 아마 여러분도 눈시울이 붉어지실 겁니다.

우리 인생이란 참 알 수 없는 것이죠.
때로는 절망의 순간이 오고, 때로는 기쁨의 순간이 찾아옵니다.
하지만 중요한 건, 그 모든 순간들이 우리를 성장시킨다는 것입니다.

자, 그럼 이제부터 제가 들려드릴 이야기에 귀 기울여 주세요.
여러분의 인생에도 큰 울림을 줄 수 있는 이야기입니다.""",

            f"""시청자 여러분, 반갑습니다.

오늘 제가 준비한 이야기는 듣는 것만으로도
가슴이 뭉클해지는 감동적인 사연입니다.

{topic}...
제목만 들어도 벌써 궁금하시죠?

이 이야기의 주인공은 우리 주변에서 흔히 볼 수 있는 평범한 분이셨습니다.
하지만 그분의 삶은 결코 평범하지 않았습니다.

인생은 때때로 우리에게 큰 시련을 주지만,
동시에 그 시련을 이겨낼 수 있는 힘도 함께 주는 것 같습니다.

편안하게 앉으셔서, 따뜻한 차 한 잔과 함께
이 아름다운 이야기를 들어보시기 바랍니다.""",

            f"""여러분, 안녕하세요.

오늘 이 시간에는 정말 특별한 분의 이야기를 들려드리려고 합니다.
{topic}에 관한 이야기입니다.

살다 보면 우리는 수많은 사람들을 만나게 됩니다.
그리고 그들의 이야기를 통해 우리 자신을 돌아보게 되죠.

오늘의 주인공도 마찬가지입니다.
이분의 이야기는 우리에게 많은 것을 생각하게 만듭니다.

인생이란 무엇인가, 행복이란 무엇인가,
그리고 진정으로 가치 있는 것은 무엇인가...

자, 이제 시작해보겠습니다.
끝까지 함께 해주시기 바랍니다."""
        ]
        return random.choice(openings)

    def _create_ki_section(self, template: Dict, topic: str, duration: int) -> str:
        """기(起) - 배경과 상황 소개 (20-25분 분량)"""
        word_count = duration * 150  # 분당 약 150자

        section = f"""
【 제1장: 시작 】

{template['기']}

{self._generate_detailed_background(topic, word_count // 3)}

주인공의 일상은 평범했지만, 그 속에는 남들이 모르는 깊은 사연이 있었습니다.
매일 아침 일어나는 것조차 힘겨운 날들이었죠.

{self._generate_character_description(word_count // 3)}

하지만 인생은 참 묘한 것입니다.
가장 어두운 밤이 지나면 새벽이 오듯,
이분의 인생에도 변화의 조짐이 보이기 시작했습니다.

{self._generate_foreshadowing(word_count // 3)}
"""
        return section

    def _create_seung_section(self, template: Dict, topic: str, duration: int) -> str:
        """승(承) - 전개와 발전 (25-30분 분량)"""
        word_count = duration * 150

        section = f"""
【 제2장: 변화의 시작 】

{template['승']}

{self._generate_turning_point(topic, word_count // 4)}

처음에는 작은 변화였습니다.
하지만 그 작은 변화가 점점 큰 파도가 되어
주인공의 삶을 완전히 바꾸기 시작했습니다.

{self._generate_development(word_count // 4)}

주변 사람들도 하나둘 이 변화를 알아차리기 시작했습니다.
"뭔가 달라졌네요."
"예전과는 눈빛이 다르세요."

{self._generate_growth_process(word_count // 4)}

희망이 보이기 시작했습니다.
어쩌면 이번에는 정말 달라질 수 있을 것 같았습니다.

{self._generate_hope_building(word_count // 4)}
"""
        return section

    def _create_jeon_section(self, template: Dict, topic: str, duration: int) -> str:
        """전(轉) - 갈등과 위기 (20-25분 분량)"""
        word_count = duration * 150

        section = f"""
【 제3장: 시련의 시간 】

{template['전']}

{self._generate_crisis(topic, word_count // 3)}

모든 것이 무너지는 것 같았습니다.
그동안 쌓아왔던 모든 것들이 한순간에 무너질 위기에 처했습니다.

{self._generate_conflict(word_count // 3)}

"이제 정말 끝인가..."
주인공은 깊은 절망에 빠졌습니다.

하지만 인생의 가장 어두운 순간이 바로
새로운 시작의 순간이 되기도 합니다.

{self._generate_turning_moment(word_count // 3)}
"""
        return section

    def _create_gyeol_section(self, template: Dict, topic: str, duration: int) -> str:
        """결(結) - 해결과 마무리 (20-25분 분량)"""
        word_count = duration * 150

        section = f"""
【 제4장: 새로운 시작 】

{template['결']}

{self._generate_resolution(topic, word_count // 3)}

주인공은 깨달았습니다.
진정한 행복은 거창한 것이 아니라
우리 곁에 있는 소중한 것들에서 찾을 수 있다는 것을.

{self._generate_enlightenment(word_count // 3)}

그리고 마침내...

{self._generate_happy_ending(word_count // 3)}

이것이 오늘 제가 여러분께 들려드린 이야기입니다.
"""
        return section

    def _create_closing(self, theme: str) -> str:
        """클로징 멘트 생성 (5-7분 분량)"""
        closings = [
            f"""
【 에필로그 】

여러분, 오늘 이야기 어떠셨나요?

우리 모두의 인생에는 이런 순간들이 있습니다.
절망의 순간, 희망의 순간, 그리고 깨달음의 순간...

중요한 것은 포기하지 않는 것입니다.
아무리 힘들어도, 아무리 어려워도,
우리에게는 일어설 수 있는 힘이 있습니다.

오늘 이야기의 주인공처럼 말이죠.

여러분도 지금 힘든 시간을 보내고 계신가요?
그렇다면 이 이야기를 기억해 주세요.
반드시 좋은 날이 올 것입니다.

오늘도 끝까지 시청해 주셔서 감사합니다.
구독과 좋아요, 알림 설정 부탁드립니다.

다음 시간에 또 좋은 이야기로 찾아뵙겠습니다.
여러분, 건강하세요. 감사합니다.""",

            f"""
【 마치며 】

이렇게 오늘의 이야기를 마치겠습니다.

살면서 우리는 수많은 선택의 순간을 마주합니다.
그리고 그 선택들이 모여 우리의 인생을 만들어갑니다.

오늘 주인공의 선택이 옳았는지, 그른지는
아무도 판단할 수 없을 것입니다.
하지만 한 가지 확실한 것은,
그분은 최선을 다해 살았다는 것입니다.

그것만으로도 충분히 존경받을 만한 삶이 아닐까요?

여러분의 삶도 마찬가지입니다.
지금 이 순간 최선을 다하고 계신다면,
그것만으로도 여러분은 충분히 훌륭한 것입니다.

오늘도 함께해 주셔서 감사합니다.
댓글로 여러분의 생각을 나눠주세요.

다음 이야기도 기대해 주시고,
모두 행복한 하루 되세요.

안녕히 계세요.""",

            f"""
【 감사의 말 】

긴 이야기 끝까지 들어주셔서 진심으로 감사드립니다.

오늘 이야기가 여러분께 작은 위로가 되었길 바랍니다.
우리는 모두 각자의 이야기를 가지고 살아가고 있습니다.

때로는 힘들고, 때로는 기쁘고,
그렇게 하루하루를 살아가는 것이 인생이죠.

하지만 기억하세요.
여러분은 혼자가 아닙니다.
이렇게 함께 이야기를 나누는 우리가 있잖아요.

어려운 일이 있으시면 주저 말고 주변에 도움을 청하세요.
그리고 여유가 있으시면 어려운 이웃을 돌아봐 주세요.

우리 모두가 서로를 따뜻하게 품어줄 때,
이 세상은 더 살기 좋은 곳이 될 것입니다.

다음 시간에는 어떤 이야기를 들려드릴까요?
여러분의 제안도 환영합니다.

건강 유의하시고, 행복하세요.
감사합니다."""
        ]
        return random.choice(closings)

    # 상세 내용 생성 헬퍼 메서드들

    def _generate_detailed_background(self, topic: str, word_count: int) -> str:
        """상세한 배경 설명 생성"""
        backgrounds = [
            f"""
이야기의 주인공은 경상도의 작은 시골 마을에서 태어나셨습니다.
1950년대 초반, 우리나라가 가장 어려웠던 시절이었죠.
가난은 당연한 것이었고, 끼니를 거르는 것도 일상이었습니다.

여섯 남매 중 셋째였던 주인공은 어려서부터 집안일을 도와야 했습니다.
학교에 가고 싶었지만 형편이 여의치 않았습니다.
대신 들판에서, 산에서, 자연이 선생님이 되어 많은 것을 배웠습니다.

열두 살이 되던 해, 주인공은 큰 결심을 합니다.
서울로 올라가 돈을 벌어 가족을 돕겠다는 결심이었죠.
부모님은 말리셨지만, 주인공의 의지는 확고했습니다.""",

            f"""
1960년대 후반, 서울 변두리의 판잣집에서 이야기는 시작됩니다.
주인공은 낮에는 공장에서 일하고, 밤에는 야간학교를 다녔습니다.
하루에 서너 시간밖에 자지 못했지만, 꿈이 있었기에 버틸 수 있었습니다.

그 시절 청계천 변에는 수많은 공장들이 있었습니다.
새벽 여섯 시에 시작해서 밤 열 시까지 일하는 것이 보통이었죠.
주인공도 그런 젊은이들 중 한 명이었습니다.

월급은 쥐꼬리만 했지만, 매달 고향에 송금을 보냈습니다.
동생들만이라도 배불리 먹고 학교에 다닐 수 있기를 바라는 마음에서였죠.
그렇게 5년의 세월이 흘렀습니다.""",

            f"""
주인공의 인생이 바뀌기 시작한 것은 50대 중반의 일이었습니다.
그때까지만 해도 평범한 직장인으로 살아왔습니다.
아침 일찍 일어나 출근하고, 저녁 늦게 집에 돌아오는 일상의 반복...

자식들은 이미 다 커서 독립했고,
남은 것은 20년을 다닌 회사와 낡은 아파트 한 채뿐이었습니다.
이대로 정년까지 일하고 은퇴하는 것이 자신의 운명이라고 생각했죠.

하지만 어느 날 갑자기 찾아온 구조조정의 소식...
"명예퇴직을 하시든지, 지방으로 발령을 가시든지 선택하세요."
청천벽력 같은 통보였습니다.

평생을 바쳐 일한 회사였는데, 이렇게 쉽게 버려질 수 있다는 것에
큰 충격을 받았습니다."""
        ]
        return random.choice(backgrounds)

    def _generate_character_description(self, word_count: int) -> str:
        """인물 상세 묘사"""
        descriptions = [
            f"""
주인공은 키가 작고 마른 체구였습니다.
하지만 눈빛만은 누구보다 강렬했습니다.
"나는 반드시 성공할 거야"라는 의지가 느껴지는 눈빛이었죠.

말수는 적었지만 한번 입을 열면 진중했습니다.
함부로 약속하지 않지만, 한 번 약속하면 반드시 지켰습니다.
그래서 주변 사람들의 신뢰를 받았습니다.

새벽형 인간이었던 주인공은 매일 새벽 5시에 일어났습니다.
간단한 운동을 하고, 명상을 하고, 하루를 계획했습니다.
이런 습관은 평생 이어졌고, 주인공의 삶을 지탱하는 힘이 되었습니다.

특히 주인공에게는 특별한 버릇이 하나 있었습니다.
힘들 때마다 어머니가 해주셨던 말씀을 되뇌는 것이었죠.
"어떤 일이 있어도 정직하게 살아라. 그것이 결국 이기는 길이다."
""",

            f"""
겉으로 보기에 주인공은 평범한 사람이었습니다.
특별한 재능이 있는 것도 아니고,
대단한 학벌이나 배경이 있는 것도 아니었습니다.

하지만 그에게는 남다른 점이 있었습니다.
바로 '포기하지 않는 집념'이었습니다.
한 번 시작하면 끝을 보는 성격이었죠.

주변 사람들은 그를 이렇게 평가했습니다.
"고집이 세다", "융통성이 없다"
하지만 정작 본인은 그것을 자랑스러워했습니다.
"내가 할 수 있는 건 이것뿐이야. 끝까지 해보는 것."

또 주인공은 독서광이었습니다.
비록 제대로 된 교육을 받지 못했지만,
책만큼은 누구보다 많이 읽었습니다.
도서관이 집이요, 책이 스승이었습니다.""",

            f"""
주인공의 얼굴에는 세월의 흔적이 깊이 새겨져 있었습니다.
이마의 주름, 눈가의 잔주름 하나하나가 모두 이야기를 담고 있었습니다.
그것은 고생의 흔적이기도 했고, 지혜의 증표이기도 했습니다.

손은 거칠었습니다.
평생 노동으로 다져진 손이었죠.
하지만 그 손길은 언제나 따뜻했습니다.
어려운 사람을 만나면 먼저 손을 내밀었습니다.

목소리는 낮고 잔잔했습니다.
큰소리를 내는 법이 없었습니다.
하지만 그 목소리에는 깊은 울림이 있었습니다.
한마디 한마디에 진정성이 담겨 있었기 때문입니다.

무엇보다 주인공에게서는 특유의 편안함이 느껴졌습니다.
함께 있으면 마음이 놓이는, 그런 사람이었습니다.
그래서 사람들은 그를 찾았고, 그의 이야기를 듣고 싶어 했습니다."""
        ]
        return random.choice(descriptions)

    def _generate_foreshadowing(self, word_count: int) -> str:
        """복선 깔기"""
        foreshadowing = [
            f"""
그 무렵, 주인공은 이상한 꿈을 자주 꾸었습니다.
넓은 들판을 걸어가는데, 멀리서 빛이 보이는 꿈이었죠.
그 빛을 향해 걸어가면 갈수록 더 밝아졌습니다.

"이게 무슨 의미일까?"
주인공은 이 꿈이 무언가를 암시하고 있다고 느꼈습니다.
하지만 그때는 그것이 무엇인지 알 수 없었습니다.

또 한 가지 이상한 일이 있었습니다.
길을 가다가 우연히 오래된 사진을 발견한 것입니다.
그 사진 속에는 자신과 닮은 사람이 있었습니다.
"이분은 누구실까..."

이 모든 것들이 나중에 큰 의미를 갖게 될 줄은
그때는 전혀 몰랐습니다.""",

            f"""
어느 날, 주인공은 길에서 한 노인을 만났습니다.
"젊은이, 앞으로 좋은 일이 생길 거요."
노인은 알 수 없는 미소를 지으며 그렇게 말했습니다.

당시에는 그냥 지나쳤지만,
나중에 생각해보니 그 노인의 말이 예언처럼 들렸습니다.

또 주인공의 어머니는 임종 전에 이런 말씀을 하셨습니다.
"네가 제일 힘들 때, 하늘이 너를 도울 거다.
그때를 놓치지 말아라."

이 말의 의미를 이해하게 된 것은
한참 후의 일이었습니다.

그리고 서랍 깊숙이 보관하고 있던 오래된 편지 한 통...
그 편지가 모든 것을 바꾸게 될 줄은 꿈에도 몰랐습니다.""",

            f"""
운명의 그날은 아무 예고 없이 찾아왔습니다.
아니, 정확히는 예고가 있었지만 알아차리지 못했던 것이죠.

일주일 전부터 주인공은 계속 까치가 우는 소리를 들었습니다.
"좋은 소식이 올 징조인가?"
하지만 크게 기대하지 않았습니다.
살면서 실망한 적이 너무 많았기 때문입니다.

또 이상하게도 그 주간은 우연의 연속이었습니다.
길에서 옛 친구를 만나고,
버스에서 중요한 신문 기사를 보게 되고,
낯선 사람에게서 명함을 받게 되고...

이 모든 것들이 하나로 연결될 줄은
그때는 몰랐습니다.
하지만 인생이란 원래 그런 것이죠.
모든 것은 연결되어 있습니다."""
        ]
        return random.choice(foreshadowing)

    def _generate_turning_point(self, topic: str, word_count: int) -> str:
        """전환점 생성"""
        return f"""
그날은 평범한 화요일 오후였습니다.
특별할 것 없는, 여느 때와 다름없는 하루였죠.

하지만 오후 3시 27분, 주인공의 인생이 바뀌기 시작했습니다.
전화 한 통이 걸려온 것입니다.

"여보세요? 혹시 ○○○ 씨이신가요?"
낯선 목소리였습니다.
"네, 그런데요..."

전화를 끊은 후, 주인공은 한참을 멍하니 서 있었습니다.
믿을 수 없는 이야기였습니다.
꿈을 꾸는 것 같았습니다.

하지만 이것은 현실이었습니다.
수십 년 동안 기다려왔던, 그 순간이 드디어 찾아온 것입니다.
"""

    def _generate_development(self, word_count: int) -> str:
        """전개 과정 생성"""
        return f"""
그 다음 날부터 주인공의 일상이 조금씩 달라지기 시작했습니다.
작은 변화들이었지만, 분명히 뭔가 달랐습니다.

먼저 마음가짐이 달라졌습니다.
예전에는 매일이 버거웠는데, 이제는 아침이 기대되었습니다.
"오늘은 또 무슨 일이 일어날까?"

주변 사람들도 변화를 알아차렸습니다.
"요즘 표정이 밝아지셨네요?"
"무슨 좋은 일 있으세요?"

주인공은 아직 아무에게도 말하지 않았습니다.
확실해질 때까지는 비밀로 하고 싶었습니다.

하지만 가슴속에서는 희망이 자라고 있었습니다.
마치 봄날의 새싹처럼, 조금씩, 그러나 확실하게...
"""

    def _generate_growth_process(self, word_count: int) -> str:
        """성장 과정 생성"""
        return f"""
이후 3개월 동안 주인공은 완전히 다른 사람이 되었습니다.

매일 새벽 4시에 일어나 준비를 했습니다.
무엇을 준비했냐고요?
바로 자신의 새로운 인생을 준비한 것입니다.

공부를 시작했습니다.
비록 늦은 나이였지만, 배움에는 나이가 없다고 생각했습니다.
도서관에 가서 책을 빌려 읽고, 인터넷 강의를 듣고,
때로는 직접 현장을 찾아가 배웠습니다.

그리고 사람들을 만나기 시작했습니다.
같은 꿈을 가진 사람들, 먼저 그 길을 걸어간 사람들...
그들의 이야기를 듣고, 조언을 구하고, 때로는 실패담도 들었습니다.

6개월이 지났을 때, 주인공은 이미 다른 사람이 되어 있었습니다.
지식도 늘었고, 인맥도 생겼고, 무엇보다 자신감이 생겼습니다.

"나도 할 수 있어. 아니, 반드시 해낼 거야!"
"""

    def _generate_hope_building(self, word_count: int) -> str:
        """희망 쌓기"""
        return f"""
드디어 첫 번째 결실을 맺는 날이 왔습니다.

비록 작은 성공이었지만, 주인공에게는 큰 의미가 있었습니다.
"내가 해냈어. 정말 해냈어!"

눈물이 났습니다.
기쁨의 눈물이었습니다.
평생을 기다려온 순간이었습니다.

가장 먼저 돌아가신 부모님 산소를 찾았습니다.
"아버지, 어머니, 이 못난 자식이 드디어 해냈습니다."
무릎을 꿇고 한참을 울었습니다.

그리고 결심했습니다.
여기서 멈추지 않겠다고.
이것은 시작일 뿐이라고.

더 큰 꿈을 향해 나아가기로 한 것입니다.
"""

    def _generate_crisis(self, topic: str, word_count: int) -> str:
        """위기 상황 생성"""
        return f"""
하지만 인생은 호락호락하지 않았습니다.

순조롭게 진행되는 듯 보이던 모든 것이
한순간에 무너질 위기에 처했습니다.

문제는 예상치 못한 곳에서 터졌습니다.
가장 믿었던 사람의 배신이었습니다.

"어떻게 이럴 수가..."
주인공은 말문이 막혔습니다.
배신감과 분노, 그리고 좌절감이 한꺼번에 밀려왔습니다.

그동안 투자한 시간과 돈, 그리고 열정...
모든 것이 물거품이 될 위기였습니다.

주변에서는 포기하라고 말했습니다.
"이쯤에서 그만두는 게 어때요?"
"더 이상은 무리예요."

주인공도 흔들렸습니다.
정말 여기서 포기해야 하는 걸까?
"""

    def _generate_conflict(self, word_count: int) -> str:
        """갈등 심화"""
        return f"""
설상가상으로 건강에도 문제가 생겼습니다.
극심한 스트레스로 인해 몸이 상한 것입니다.

병원에 갔더니 의사가 말했습니다.
"당분간 푹 쉬셔야 합니다. 이러다간 큰일 납니다."

하지만 쉴 수가 없었습니다.
지금 쉬면 모든 것이 끝장이었습니다.

가족들도 걱정했습니다.
"건강이 우선이에요. 제발 쉬세요."

밤잠을 이룰 수 없었습니다.
매일 밤 천장만 바라보며 고민했습니다.
"어떻게 해야 하지? 어떻게..."

그러던 어느 날 밤, 주인공은 중대한 결심을 했습니다.
도박이었습니다.
성공하면 모든 것을 얻고, 실패하면 모든 것을 잃는...
"""

    def _generate_turning_moment(self, word_count: int) -> str:
        """반전의 순간"""
        return f"""
그 결심이 주인공을 다시 일으켜 세웠습니다.

"그래, 한 번 해보자.
여기까지 왔는데 포기할 수는 없어.
죽기 살기로 해보는 거야!"

새벽부터 밤까지, 주인공은 미친 듯이 일했습니다.
하루에 3-4시간밖에 자지 못했습니다.
식사도 제대로 못했습니다.

하지만 눈빛만은 살아있었습니다.
"반드시 해낸다"는 의지가 불꽃처럼 타올랐습니다.

그리고 마침내...

기적이 일어났습니다.
아니, 기적이 아니었습니다.
땀과 눈물, 그리고 포기하지 않는 집념이 만들어낸 결과였습니다.

문제가 풀리기 시작한 것입니다.
하나씩, 하나씩...
"""

    def _generate_resolution(self, topic: str, word_count: int) -> str:
        """해결 과정"""
        return f"""
배신했던 사람이 다시 찾아왔습니다.
무릎을 꿇고 용서를 빌었습니다.

"저를 용서해주세요. 제가 잘못했습니다."

주인공은 한참을 그를 바라보았습니다.
분노가 치밀어 올랐습니다.
하지만 동시에 연민도 느껴졌습니다.

"일어나세요. 이제 그만 괴로워하세요."

용서했습니다.
쉬운 결정은 아니었습니다.
하지만 미움을 품고 사는 것보다는
용서하고 앞으로 나아가는 것이 낫다고 생각했습니다.

그리고 놀라운 일이 일어났습니다.
용서를 한 순간, 주인공의 마음이 가벼워졌습니다.
오히려 자신이 치유되는 느낌이었습니다.

"아, 이것이 용서의 힘이구나..."
"""

    def _generate_enlightenment(self, word_count: int) -> str:
        """깨달음"""
        return f"""
이 모든 과정을 겪으며 주인공은 깨달았습니다.

인생에서 가장 중요한 것은
성공이나 돈이 아니라는 것을.

진정으로 중요한 것은
과정에서 배운 것들,
만난 사람들,
그리고 자신의 성장이라는 것을.

"나는 부자가 되지는 못했지만,
대신 훨씬 더 소중한 것을 얻었어.
그것은 바로 삶의 지혜야."

돌이켜보니 모든 시련에는 의미가 있었습니다.
고통스러운 순간들이 자신을 단련시켰고,
절망의 순간들이 희망의 소중함을 가르쳐주었습니다.

이제는 어떤 어려움이 와도 두렵지 않았습니다.
이미 최악의 순간을 견뎌냈으니까요.
"""

    def _generate_happy_ending(self, word_count: int) -> str:
        """행복한 결말"""
        return f"""
오늘도 주인공은 여전히 일을 하고 있습니다.

하지만 예전과는 다릅니다.
이제는 의무가 아닌 기쁨으로 일합니다.
돈 때문이 아니라 즐거워서 일합니다.

무엇보다 주인공은 이제 다른 사람들을 돕고 있습니다.
자신이 걸어온 길을 후배들에게 알려주고,
어려움에 처한 사람들에게 손을 내밀고 있습니다.

"제가 받은 도움을 이제는 제가 돌려줄 차례입니다."

주인공의 얼굴에는 평화로운 미소가 가득합니다.
고생의 흔적은 여전하지만,
그 속에서 깊은 만족감이 느껴집니다.

"후회 없는 인생을 살았습니다.
힘들었지만, 그래도 행복했습니다.
그리고 앞으로 남은 시간도
의미 있게 살고 싶습니다."

이것이 주인공이 우리에게 전하는 메시지입니다.
포기하지 마세요.
끝까지 최선을 다하세요.
그러면 반드시 길이 열립니다.
"""

    def generate_script(
        self,
        theme: Optional[str] = None,
        topic: Optional[str] = None,
        duration_minutes: int = 100,
        style: str = "김은숙작가"
    ) -> Dict[str, str]:
        """
        완전한 대본 생성

        Args:
            theme: 주제 카테고리 (None이면 랜덤 선택)
            topic: 구체적 주제 (None이면 랜덤 선택)
            duration_minutes: 대본 길이 (분 단위, 기본 100분 = 1시간 40분)
            style: 작가 스타일 (기본: 김은숙작가)

        Returns:
            Dict: 생성된 대본과 메타데이터
        """
        # 주제 선택
        if theme is None or topic is None:
            selected_category = random.choice(self.themes)
            theme = selected_category['category']
            topic = random.choice(selected_category['topics'])

        # 템플릿 선택
        template = self.story_templates.get(theme, self.story_templates['인생역전'])

        # 각 부분별 시간 배분 (총 duration_minutes 분)
        # 오프닝: 5%, 기: 25%, 승: 28%, 전: 22%, 결: 15%, 클로징: 5%
        opening_duration = int(duration_minutes * 0.05)
        ki_duration = int(duration_minutes * 0.25)
        seung_duration = int(duration_minutes * 0.28)
        jeon_duration = int(duration_minutes * 0.22)
        gyeol_duration = int(duration_minutes * 0.15)
        closing_duration = int(duration_minutes * 0.05)

        # 대본 생성
        script = {
            "metadata": {
                "theme": theme,
                "topic": topic,
                "duration_minutes": duration_minutes,
                "style": style,
                "generated_at": datetime.now().isoformat(),
                "word_count_estimate": duration_minutes * 150  # 분당 약 150자
            },
            "opening": self._create_opening(theme, topic),
            "act1_ki": self._create_ki_section(template, topic, ki_duration),
            "act2_seung": self._create_seung_section(template, topic, seung_duration),
            "act3_jeon": self._create_jeon_section(template, topic, jeon_duration),
            "act4_gyeol": self._create_gyeol_section(template, topic, gyeol_duration),
            "closing": self._create_closing(theme)
        }

        return script

    def export_script(self, script: Dict, output_path: str, format: str = 'txt'):
        """
        대본을 파일로 저장

        Args:
            script: 생성된 대본 딕셔너리
            output_path: 저장 경로
            format: 저장 형식 ('txt', 'json', 'md')
        """
        if format == 'json':
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(script, f, ensure_ascii=False, indent=2)

        elif format == 'md':
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"# {script['metadata']['topic']}\n\n")
                f.write(f"**주제**: {script['metadata']['theme']}\n")
                f.write(f"**예상 길이**: {script['metadata']['duration_minutes']}분\n")
                f.write(f"**생성일시**: {script['metadata']['generated_at']}\n\n")
                f.write("---\n\n")
                f.write(script['opening'] + "\n\n")
                f.write(script['act1_ki'] + "\n\n")
                f.write(script['act2_seung'] + "\n\n")
                f.write(script['act3_jeon'] + "\n\n")
                f.write(script['act4_gyeol'] + "\n\n")
                f.write(script['closing'] + "\n")

        else:  # txt
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write("=" * 80 + "\n")
                f.write(f"  {script['metadata']['topic']}\n")
                f.write("=" * 80 + "\n\n")
                f.write(f"주제: {script['metadata']['theme']}\n")
                f.write(f"예상 길이: {script['metadata']['duration_minutes']}분\n")
                f.write(f"생성일시: {script['metadata']['generated_at']}\n")
                f.write("=" * 80 + "\n\n")

                f.write(script['opening'] + "\n\n")
                f.write("-" * 80 + "\n\n")
                f.write(script['act1_ki'] + "\n\n")
                f.write("-" * 80 + "\n\n")
                f.write(script['act2_seung'] + "\n\n")
                f.write("-" * 80 + "\n\n")
                f.write(script['act3_jeon'] + "\n\n")
                f.write("-" * 80 + "\n\n")
                f.write(script['act4_gyeol'] + "\n\n")
                f.write("-" * 80 + "\n\n")
                f.write(script['closing'] + "\n")
                f.write("\n" + "=" * 80 + "\n")
                f.write("끝\n")
                f.write("=" * 80 + "\n")


def main():
    """메인 실행 함수"""
    print("=" * 80)
    print("  유튜브 시니어 채널 대본 생성기")
    print("  김은숙 작가 스타일 스토리텔링")
    print("=" * 80)
    print()

    generator = SeniorScriptGenerator()

    print("대본을 생성하고 있습니다...")
    print()

    # 랜덤 대본 생성 (100분 = 1시간 40분)
    script = generator.generate_script(duration_minutes=100)

    print(f"✓ 주제: {script['metadata']['topic']}")
    print(f"✓ 카테고리: {script['metadata']['theme']}")
    print(f"✓ 예상 길이: {script['metadata']['duration_minutes']}분")
    print(f"✓ 예상 글자수: 약 {script['metadata']['word_count_estimate']:,}자")
    print()

    # 파일로 저장
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    output_dir = "output"
    txt_path = f"{output_dir}/senior_script_{timestamp}.txt"
    json_path = f"{output_dir}/senior_script_{timestamp}.json"
    md_path = f"{output_dir}/senior_script_{timestamp}.md"

    generator.export_script(script, txt_path, 'txt')
    generator.export_script(script, json_path, 'json')
    generator.export_script(script, md_path, 'md')

    print("✓ 대본이 생성되었습니다:")
    print(f"  - {txt_path}")
    print(f"  - {json_path}")
    print(f"  - {md_path}")
    print()
    print("=" * 80)


if __name__ == "__main__":
    main()
