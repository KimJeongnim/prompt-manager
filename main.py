# 1. 기본 프롬프트 데이터 (리스트와 딕셔너리)
prompts = [
    {
        "title": "교육생 문의사항 응대 봇",
        "content": "당신은 친절하고 전문적인 교육 운영 매니저입니다. 교육생들이 남긴 문의사항에 대해 명확하고 이해하기 쉬운 답변을 작성해주세요. 항상 격려하는 어조를 유지하고, 기술적인 용어나 복잡한 절차는 초보자도 알기 쉽게 풀어 설명해주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "Tripmind AI 광고 - 지친 여행자 탈출",
        "content": "늦은 밤, 수십 개의 열린 인터넷 탭과 복잡한 여행 계획 표를 보며 머리를 감싸쥐고 지친 표정으로 한숨 쉬는 여행자의 모습. 책상 위에는 노트북과 흩어진 메모지들이 가득함. 시네마틱 라이팅, 다크하고 답답한 분위기, 고화질, 16:9 비율.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "핵심 쏙쏙 회의록 요약",
        "content": "입력된 날것의 회의 녹취록 또는 메모를 바탕으로 깔끔한 전문 회의록을 작성해주세요. 1) 회의 개요(일시/참석자), 2) 주요 안건 및 논의 내용, 3) 결정된 사항, 4) 향후 액션 아이템(담당자 및 기한 포함) 형식으로 구조화하여 요약해주세요.",
        "category": "자동화",
        "favorite": False
    }
]

# 2. 메뉴 화면 출력 함수
def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

#  카테고리 출력 함수
def show_categories():
    print("1) 텍스트 생성")
    print("2) 이미지 생성")
    print("3) 영상 생성")
    print("4) 페르소나")
    print("5) 자동화")
    print("6) 기타")

# 3. 각 기능을 담당할 함수들 뼈대 (앞으로 채워나갈 곳)
def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    
    # 1. 제목 입력 (비어있으면 다시 입력받기)
    while True:
        title = input("제목: ").strip()
        if title != "":
            break
        print("제목은 비워둘 수 없습니다. 다시 입력해주세요.")

    # 2. 내용 입력 (비어있으면 다시 입력받기)
    while True:
        content = input("내용: ").strip()
        if content != "":
            break
        print("내용은 비워둘 수 없습니다. 다시 입력해주세요.")

   # 3. 카테고리 선택
    print("\n카테고리 선택:")
    show_categories()
    
    category_dict = {
        "1": "텍스트 생성",
        "2": "이미지 생성",
        "3": "영상 생성",
        "4": "페르소나",
        "5": "자동화",
        "6": "기타"
    }

    while True:
        cat_choice = input("선택: ").strip()
        if cat_choice in category_dict:
            category = category_dict[cat_choice]
            break
        print("올바른 번호를 선택해주세요.")

    # 4. 새로운 프롬프트 딕셔너리 생성 후 리스트에 추가
    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False  # 기본 즐겨찾기 값은 False
    }

    prompts.append(new_prompt)
    print("\n프롬프트가 추가되었습니다!")

def show_list():
    print("\n=== 프롬프트 목록 ===")
    
    # 등록된 프롬프트가 없는 경우
    if len(prompts) == 0:
        print("등록된 프롬프트가 없습니다.")
        return

    # 리스트를 순회하며 번호, 카테고리, 제목, 즐겨찾기 출력
    for i, p in enumerate(prompts, start=1):
        fav_mark = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{fav_mark}")
    
    print(f"\n총 {len(prompts)}개의 프롬프트")

def search_by_category():
    print("\n=== 카테고리별 조회 ===")
    show_categories()

    category_dict = {
        "1": "텍스트 생성",
        "2": "이미지 생성",
        "3": "영상 생성",
        "4": "페르소나",
        "5": "자동화",
        "6": "기타"
    }

    # 카테고리 번호 입력
    cat_choice = input("선택: ").strip()

    if cat_choice not in category_dict:
        print("올바른 번호를 선택해주세요.")
        return

    selected_category = category_dict[cat_choice]

    print(f"\n[{selected_category}] 카테고리 프롬프트:")

    # 해당 카테고리의 프롬프트만 찾기
    found_count = 0

    for p in prompts:
        if p["category"] == selected_category:
            found_count += 1
            fav_mark = " ⭐" if p["favorite"] else ""
            print(f"{found_count}. {p['title']}{fav_mark}")

    # 해당 카테고리에 프롬프트가 없는 경우
    if found_count == 0:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
    else:
        print(f"\n총 {found_count}개의 프롬프트")

def search_prompts():
    print("\n=== 프롬프트 검색 ===")

    keyword = input("검색할 키워드를 입력하세요: ").strip().lower()

    # 검색어가 비어있는 경우
    if not keyword:
        print("키워드를 입력해야 검색이 가능합니다.")
        return

    print(f"\n'{keyword}' 검색 결과:")

    found_count = 0

    # 제목 또는 내용에서 키워드 검색
    for i, p in enumerate(prompts, start=1):
        if keyword in p["title"].lower() or keyword in p["content"].lower():
            found_count += 1

            fav_mark = " ⭐" if p["favorite"] else ""

            print(f"{found_count}. [{p['category']}] {p['title']}{fav_mark}")

    # 검색 결과가 없는 경우
    if found_count == 0:
        print("검색 결과가 없습니다.")
    else:
        print(f"\n총 {found_count}개의 프롬프트를 찾았습니다.")

def view_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 1. 전체 목록을 먼저 간략하게 보여주기
    for i, p in enumerate(prompts, start=1):
        fav_mark = " ⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']} [{p['category']}]{fav_mark}")

    # 2. 상세히 볼 번호 입력받기
    choice_input = input("\n상세 볼 프롬프트 번호 입력 (취소는 0): ").strip()
    if choice_input == "0":
        return

    if not choice_input.isdigit():
        print("올바른 숫자를 입력해주세요.")
        return

    idx = int(choice_input) - 1

    # 3. 범위 내의 번호인지 확인 후 상세 내용 출력
    if 0 <= idx < len(prompts):
        p = prompts[idx]
        fav_mark = "⭐ (즐겨찾기 됨)" if p["favorite"] else "일반"
        print(f"\n================================")
        print(f" 제목 : {p['title']}")
        print(f" 카테고리 : {p['category']}")
        print(f" 상태 : {fav_mark}")
        print(f"--------------------------------")
        print(f" [ 내용 ]\n{p['content']}")
        print(f"================================")
    else:
        print("존재하지 않는 프롬프트 번호입니다.")

def manage_favorite():
    print("\n=== 즐겨찾기 관리 ===")
    
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    # 1. 목록 보여주기
    for i, p in enumerate(prompts, start=1):
        fav_mark = " ⭐" if p["favorite"] else " [ ]"
        print(f"{i}. {fav_mark} {p['title']}")

    # 2. 번호 입력받기
    choice_input = input("\n즐겨찾기 상태를 변경할 프롬프트 번호 입력 (취소는 0): ").strip()
    if choice_input == "0":
        return

    if not choice_input.isdigit():
        print("올바른 숫자를 입력해주세요.")
        return

    idx = int(choice_input) - 1

    # 3. 상태 반전 (True <-> False)
    if 0 <= idx < len(prompts):
        prompts[idx]["favorite"] = not prompts[idx]["favorite"]
        status = "즐겨찾기 추가됨" if prompts[idx]["favorite"] else "즐겨찾기 해제됨"
        print(f"'{prompts[idx]['title']}' 프롬프트가 {status}!")
    else:
        print("존재하지 않는 번호입니다.")

def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")

    # 즐겨찾기된 프롬프트만 찾기
    favorite_count = 0

    for i, p in enumerate(prompts, start=1):
        if p["favorite"]:
            favorite_count += 1
            print(f"{favorite_count}. [{p['category']}] {p['title']} ⭐")

    # 즐겨찾기가 하나도 없는 경우
    if favorite_count == 0:
        print("즐겨찾기된 프롬프트가 없습니다.")
    else:
        print(f"\n총 {favorite_count}개의 즐겨찾기")


# 4. 메인 실행 루프 (여기를 수정하면 됩니다!)
while True:
    show_menu()
    choice = input("선택: ")

    if choice == "1":
        add_prompt()
    elif choice == "2":
        show_list()
    elif choice == "3":
        search_by_category()
    elif choice == "4":
        search_prompts()
    elif choice == "5":
        view_detail()
    elif choice == "6":
        manage_favorite()
    elif choice == "7":
        show_favorites()
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 올바른 번호를 선택해주세요.")