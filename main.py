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

# 3. 각 기능을 담당할 함수들 뼈대 (앞으로 채워나갈 곳)
def add_prompt():
    print("\n[프롬프트 추가 기능 구현 예정]")

def show_list():
    print("\n[프롬프트 목록 기능 구현 예정]")

def search_by_category():
    print("\n[카테고리별 조회 기능 구현 예정]")

def search_prompt():
    print("\n[프롬프트 검색 기능 구현 예정]")

def show_detail():
    print("\n[프롬프트 상세 보기 기능 구현 예정]")

def manage_favorite():
    print("\n[즐겨찾기 관리 기능 구현 예정]")

def show_favorites():
    print("\n[즐겨찾기 목록 기능 구현 예정]")


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
        search_prompt()
    elif choice == "5":
        show_detail()
    elif choice == "6":
        manage_favorite()
    elif choice == "7":
        show_favorites()
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 올바른 번호를 선택해주세요.")