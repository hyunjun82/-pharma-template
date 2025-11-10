#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
예제 대본 생성 스크립트
다양한 주제와 길이로 샘플 대본을 생성합니다.
"""

import sys
import os

# 상위 디렉토리의 src 모듈을 임포트하기 위한 경로 추가
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from senior_youtube_script_generator import SeniorScriptGenerator


def generate_short_script():
    """짧은 대본 생성 (1시간 20분)"""
    print("=" * 80)
    print("  짧은 대본 생성 (1시간 20분)")
    print("=" * 80)

    generator = SeniorScriptGenerator()
    script = generator.generate_script(
        theme="인생역전",
        topic="60대에 시작한 작은 가게가 대성공한 이야기",
        duration_minutes=80  # 1시간 20분
    )

    output_path = "../output/sample_script_80min.txt"
    generator.export_script(script, output_path, 'txt')
    generator.export_script(script, output_path.replace('.txt', '.md'), 'md')

    print(f"✓ 생성 완료: {output_path}")
    print()


def generate_long_script():
    """긴 대본 생성 (2시간)"""
    print("=" * 80)
    print("  긴 대본 생성 (2시간)")
    print("=" * 80)

    generator = SeniorScriptGenerator()
    script = generator.generate_script(
        theme="가족애",
        topic="30년 만에 만난 형제의 눈물겨운 재회",
        duration_minutes=120  # 2시간
    )

    output_path = "../output/sample_script_120min.txt"
    generator.export_script(script, output_path, 'txt')
    generator.export_script(script, output_path.replace('.txt', '.md'), 'md')

    print(f"✓ 생성 완료: {output_path}")
    print()


def generate_multiple_themes():
    """여러 주제로 대본 생성"""
    print("=" * 80)
    print("  다양한 주제로 대본 생성")
    print("=" * 80)

    generator = SeniorScriptGenerator()

    themes_topics = [
        ("우정", "50년 우정을 지켜온 친구들의 감동 실화"),
        ("도전과성취", "70세에 대학교에 입학한 할머니의 도전기"),
        ("사랑", "50년 전 헤어진 첫사랑과의 운명적 재회"),
        ("지혜와교훈", "가난을 극복하고 성공한 기업인의 인생 철학")
    ]

    for i, (theme, topic) in enumerate(themes_topics, 1):
        print(f"\n[{i}/4] {theme}: {topic}")
        script = generator.generate_script(
            theme=theme,
            topic=topic,
            duration_minutes=100  # 1시간 40분
        )

        output_path = f"../output/sample_script_{theme}_{i}.txt"
        generator.export_script(script, output_path, 'txt')
        print(f"    ✓ 생성 완료: {output_path}")

    print()


def generate_random_scripts(count=3):
    """랜덤 주제로 대본 생성"""
    print("=" * 80)
    print(f"  랜덤 주제로 {count}개 대본 생성")
    print("=" * 80)

    generator = SeniorScriptGenerator()

    for i in range(count):
        print(f"\n[{i+1}/{count}] 랜덤 대본 생성 중...")
        script = generator.generate_script(
            duration_minutes=100  # 1시간 40분
        )

        print(f"    주제: {script['metadata']['topic']}")
        output_path = f"../output/sample_script_random_{i+1}.txt"
        generator.export_script(script, output_path, 'txt')
        generator.export_script(script, output_path.replace('.txt', '.json'), 'json')
        print(f"    ✓ 생성 완료: {output_path}")

    print()


def interactive_mode():
    """대화형 모드"""
    print("=" * 80)
    print("  유튜브 시니어 채널 대본 생성기 - 대화형 모드")
    print("=" * 80)
    print()

    generator = SeniorScriptGenerator()

    # 주제 카테고리 선택
    print("주제 카테고리를 선택하세요:")
    themes = list(generator.story_templates.keys())
    for i, theme in enumerate(themes, 1):
        print(f"  {i}. {theme}")
    print(f"  0. 랜덤 선택")
    print()

    try:
        choice = int(input("선택 (0-{}): ".format(len(themes))))
        if choice == 0:
            selected_theme = None
            selected_topic = None
            print("→ 랜덤 주제로 생성합니다.")
        elif 1 <= choice <= len(themes):
            selected_theme = themes[choice - 1]

            # 해당 카테고리의 주제들 표시
            theme_data = next((t for t in generator.themes if t['category'] == selected_theme), None)
            if theme_data:
                print(f"\n'{selected_theme}' 카테고리의 주제들:")
                for i, topic in enumerate(theme_data['topics'], 1):
                    print(f"  {i}. {topic}")
                print(f"  0. 랜덤 선택")
                print()

                topic_choice = int(input("선택 (0-{}): ".format(len(theme_data['topics']))))
                if topic_choice == 0:
                    selected_topic = None
                    print("→ 랜덤 주제로 생성합니다.")
                elif 1 <= topic_choice <= len(theme_data['topics']):
                    selected_topic = theme_data['topics'][topic_choice - 1]
                    print(f"→ '{selected_topic}' 주제로 생성합니다.")
                else:
                    print("잘못된 선택입니다. 랜덤으로 생성합니다.")
                    selected_topic = None
            else:
                selected_topic = None
        else:
            print("잘못된 선택입니다. 랜덤으로 생성합니다.")
            selected_theme = None
            selected_topic = None

        # 대본 길이 선택
        print("\n대본 길이를 선택하세요:")
        print("  1. 짧게 (1시간 20분 = 80분)")
        print("  2. 보통 (1시간 40분 = 100분)")
        print("  3. 길게 (2시간 = 120분)")
        print("  4. 직접 입력")
        print()

        duration_choice = int(input("선택 (1-4): "))
        if duration_choice == 1:
            duration = 80
        elif duration_choice == 2:
            duration = 100
        elif duration_choice == 3:
            duration = 120
        elif duration_choice == 4:
            duration = int(input("길이를 분 단위로 입력하세요 (80-180): "))
            if duration < 80:
                duration = 80
            elif duration > 180:
                duration = 180
        else:
            duration = 100
            print("잘못된 선택입니다. 기본값(100분)으로 설정합니다.")

        print(f"\n대본을 생성하고 있습니다... (약 {duration}분 분량)")
        print()

        # 대본 생성
        script = generator.generate_script(
            theme=selected_theme,
            topic=selected_topic,
            duration_minutes=duration
        )

        print("=" * 80)
        print(f"✓ 생성 완료!")
        print(f"  주제: {script['metadata']['topic']}")
        print(f"  카테고리: {script['metadata']['theme']}")
        print(f"  예상 길이: {script['metadata']['duration_minutes']}분")
        print(f"  예상 글자수: 약 {script['metadata']['word_count_estimate']:,}자")
        print("=" * 80)
        print()

        # 파일 저장
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        txt_path = f"../output/script_{timestamp}.txt"
        json_path = f"../output/script_{timestamp}.json"
        md_path = f"../output/script_{timestamp}.md"

        generator.export_script(script, txt_path, 'txt')
        generator.export_script(script, json_path, 'json')
        generator.export_script(script, md_path, 'md')

        print("✓ 대본이 저장되었습니다:")
        print(f"  - {txt_path}")
        print(f"  - {json_path}")
        print(f"  - {md_path}")
        print()

    except ValueError:
        print("잘못된 입력입니다. 랜덤으로 생성합니다.")
        script = generator.generate_script(duration_minutes=100)
        print(f"\n✓ 생성 완료: {script['metadata']['topic']}")

    except Exception as e:
        print(f"오류 발생: {e}")


if __name__ == "__main__":
    print()
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 20 + "시니어 채널 대본 생성 예제" + " " * 30 + "║")
    print("╚" + "═" * 78 + "╝")
    print()
    print("실행할 모드를 선택하세요:")
    print("  1. 대화형 모드 (추천)")
    print("  2. 짧은 대본 생성 (80분)")
    print("  3. 긴 대본 생성 (120분)")
    print("  4. 다양한 주제로 4개 생성")
    print("  5. 랜덤 주제로 3개 생성")
    print("  6. 모두 실행")
    print()

    try:
        choice = input("선택 (1-6): ").strip()

        if choice == "1":
            interactive_mode()
        elif choice == "2":
            generate_short_script()
        elif choice == "3":
            generate_long_script()
        elif choice == "4":
            generate_multiple_themes()
        elif choice == "5":
            generate_random_scripts(3)
        elif choice == "6":
            generate_short_script()
            generate_long_script()
            generate_multiple_themes()
            generate_random_scripts(3)
        else:
            print("잘못된 선택입니다. 대화형 모드로 실행합니다.")
            interactive_mode()

    except KeyboardInterrupt:
        print("\n\n프로그램을 종료합니다.")
    except Exception as e:
        print(f"\n오류 발생: {e}")

    print()
    print("=" * 80)
    print("모든 작업이 완료되었습니다!")
    print("=" * 80)
