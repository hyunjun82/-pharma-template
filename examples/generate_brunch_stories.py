#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
브런치 스토리 생성 예제
다양한 방법으로 1인칭 감성 스토리를 생성합니다
"""

import sys
import os

# 상위 디렉토리의 src 모듈을 임포트하기 위한 경로 추가
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from brunch_story_generator import BrunchStoryGenerator


def generate_single_story():
    """단일 스토리 생성"""
    print("=" * 80)
    print("  단일 브런치 스토리 생성")
    print("=" * 80)
    print()

    generator = BrunchStoryGenerator()
    post = generator.generate_complete_brunch_post()

    print(f"주제: {post['metadata']['topic']}")
    print(f"테마: {post['metadata']['theme']}")
    print()
    print("추천 제목 5개:")
    for i, title in enumerate(post['titles'], 1):
        marker = "⭐" if i == 1 else "  "
        print(f"{marker} {i}. {title}")
    print()

    output_path = "../output/brunch_single.txt"
    generator.export_for_brunch(post, output_path)
    print(f"✓ 저장 완료: {output_path}")
    print()


def generate_multiple_themes():
    """다양한 주제로 여러 개 생성"""
    print("=" * 80)
    print("  5가지 테마로 스토리 생성")
    print("=" * 80)
    print()

    generator = BrunchStoryGenerator()
    themes = ["인생역전", "가족애", "사랑", "성장", "일상"]

    for i, theme in enumerate(themes, 1):
        print(f"[{i}/5] {theme} 테마 생성 중...")
        post = generator.generate_complete_brunch_post(theme=theme)

        output_path = f"../output/brunch_{theme}.txt"
        generator.export_for_brunch(post, output_path)
        print(f"  ✓ 완료: {output_path}")
        print(f"  추천 제목: {post['titles'][0]}")
        print()


def generate_weekly_posts():
    """일주일치 포스트 생성"""
    print("=" * 80)
    print("  일주일치 브런치 포스트 생성")
    print("=" * 80)
    print()

    generator = BrunchStoryGenerator()

    # 월~일 요일별 테마
    weekly_themes = [
        ("월", "인생역전"),
        ("화", "가족애"),
        ("수", "사랑"),
        ("목", "성장"),
        ("금", "일상"),
        ("토", "인생역전"),
        ("일", "가족애")
    ]

    for i, (day, theme) in enumerate(weekly_themes, 1):
        print(f"[{i}/7] {day}요일 - {theme} 테마")
        post = generator.generate_complete_brunch_post(theme=theme)

        output_path = f"../output/week_{day}요일.txt"
        generator.export_for_brunch(post, output_path)
        print(f"  ✓ 저장: {output_path}")
        print(f"  제목: {post['titles'][0]}")
        print()

    print("✓ 일주일치 포스트 생성 완료!")
    print()


def generate_titles_only(count=20):
    """제목만 대량 생성"""
    print("=" * 80)
    print(f"  클릭률 높은 제목 {count}개 생성")
    print("=" * 80)
    print()

    generator = BrunchStoryGenerator()

    output_path = f"../output/titles_{count}개.txt"

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write(f"  클릭률 높은 브런치 제목 {count}개\n")
        f.write("=" * 80 + "\n\n")

        for i in range(count):
            # 랜덤 테마 선택
            themes = ["인생역전", "가족애", "사랑", "성장", "일상"]
            import random
            theme = random.choice(themes)

            titles = generator.generate_titles(theme, "샘플 주제")

            f.write(f"[제목 세트 {i+1}] - {theme} 테마\n")
            for j, title in enumerate(titles, 1):
                f.write(f"  {j}. {title}\n")
            f.write("\n")

            if (i + 1) % 5 == 0:
                print(f"  ... {i+1}개 생성 완료")

    print(f"\n✓ 총 {count}개 제목 세트 생성 완료")
    print(f"✓ 저장 위치: {output_path}")
    print()


def interactive_mode():
    """대화형 모드"""
    print("=" * 80)
    print("  브런치 스토리 생성기 - 대화형 모드")
    print("=" * 80)
    print()

    generator = BrunchStoryGenerator()

    # 테마 선택
    print("테마를 선택하세요:")
    print("  1. 인생역전 - 새로운 시작, 도전, 성공")
    print("  2. 가족애 - 가족의 사랑, 화해, 이해")
    print("  3. 사랑 - 인연, 만남, 그리움")
    print("  4. 성장 - 배움, 깨달음, 변화")
    print("  5. 일상 - 소소한 행복, 감사")
    print("  0. 랜덤 선택")
    print()

    try:
        choice = int(input("선택 (0-5): "))

        theme_map = {
            1: "인생역전",
            2: "가족애",
            3: "사랑",
            4: "성장",
            5: "일상"
        }

        if choice == 0:
            selected_theme = None
            print("→ 랜덤 테마로 생성합니다\n")
        elif choice in theme_map:
            selected_theme = theme_map[choice]
            print(f"→ '{selected_theme}' 테마로 생성합니다\n")
        else:
            print("잘못된 선택입니다. 랜덤으로 생성합니다\n")
            selected_theme = None

        # 생성 개수 선택
        print("몇 개를 생성하시겠습니까?")
        print("  1. 1개")
        print("  2. 3개")
        print("  3. 5개")
        print("  4. 10개")
        print()

        count_choice = int(input("선택 (1-4): "))
        count_map = {1: 1, 2: 3, 3: 5, 4: 10}
        count = count_map.get(count_choice, 1)

        print(f"\n{count}개의 스토리를 생성하고 있습니다...\n")

        # 생성
        for i in range(count):
            print(f"[{i+1}/{count}] 생성 중...")
            post = generator.generate_complete_brunch_post(theme=selected_theme)

            output_path = f"../output/interactive_{i+1}.txt"
            generator.export_for_brunch(post, output_path)

            print(f"  테마: {post['metadata']['theme']}")
            print(f"  주제: {post['metadata']['topic']}")
            print(f"  추천 제목: {post['titles'][0]}")
            print(f"  저장: {output_path}")
            print()

        print("=" * 80)
        print("✓ 모든 스토리 생성 완료!")
        print("output/ 폴더에서 확인하세요")
        print("=" * 80)

    except ValueError:
        print("잘못된 입력입니다. 기본 설정으로 1개 생성합니다\n")
        post = generator.generate_complete_brunch_post()
        generator.export_for_brunch(post, "../output/interactive_default.txt")
        print(f"✓ 생성 완료: ../output/interactive_default.txt")

    except KeyboardInterrupt:
        print("\n\n작업이 취소되었습니다.")


def show_sample_output():
    """샘플 출력 미리보기"""
    print("=" * 80)
    print("  샘플 출력 미리보기")
    print("=" * 80)
    print()

    generator = BrunchStoryGenerator()
    post = generator.generate_complete_brunch_post(theme="인생역전")

    print("【 생성 예시 】\n")
    print(f"테마: {post['metadata']['theme']}")
    print(f"주제: {post['metadata']['topic']}")
    print()
    print("추천 제목 5개:")
    for i, title in enumerate(post['titles'], 1):
        marker = "⭐" if i == 1 else "  "
        print(f"{marker} {i}. {title}")
    print()
    print("본문 미리보기 (처음 500자):")
    print("-" * 80)
    preview = post['content'][:500]
    print(preview + "...\n")
    print("-" * 80)
    print("\n(실제로는 약 3,000자 분량의 완전한 스토리가 생성됩니다)")
    print()


if __name__ == "__main__":
    print()
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 22 + "브런치 스토리 생성 예제" + " " * 29 + "║")
    print("╚" + "═" * 78 + "╝")
    print()
    print("실행할 모드를 선택하세요:")
    print("  1. 대화형 모드 (추천) - 테마와 개수 선택")
    print("  2. 단일 스토리 생성")
    print("  3. 5가지 테마로 각 1개씩 생성")
    print("  4. 일주일치 포스트 생성 (7개)")
    print("  5. 제목만 20개 생성")
    print("  6. 샘플 출력 미리보기")
    print("  7. 모두 실행")
    print()

    try:
        choice = input("선택 (1-7): ").strip()

        if choice == "1":
            interactive_mode()
        elif choice == "2":
            generate_single_story()
        elif choice == "3":
            generate_multiple_themes()
        elif choice == "4":
            generate_weekly_posts()
        elif choice == "5":
            generate_titles_only(20)
        elif choice == "6":
            show_sample_output()
        elif choice == "7":
            generate_single_story()
            generate_multiple_themes()
            generate_weekly_posts()
            generate_titles_only(20)
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
    print("output/ 폴더에서 생성된 파일을 확인하세요")
    print("=" * 80)
