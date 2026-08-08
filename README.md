# 나만의 프롬프트 관리 프로그램

Python으로 제작한 **콘솔 기반 프롬프트 관리 프로그램**입니다.

생성형 AI를 사용하면서 쌓이는 다양한 프롬프트를 카테고리별로 관리하고, 필요한 프롬프트를 검색하거나 즐겨찾기로 관리할 수 있도록 제작했습니다.

## 주요 기능

* 프롬프트 추가
* 프롬프트 목록 조회
* 카테고리별 조회
* 프롬프트 검색
* 프롬프트 상세 보기
* 즐겨찾기 추가 및 해제
* 즐겨찾기 목록 조회
* 프로그램 실행 중 데이터 관리

## 실행 방법

### 1. Python 버전 확인

Python 3.10 이상이 설치되어 있는지 확인합니다.

```bash
python --version
```

### 2. 프로그램 실행

프로젝트 폴더에서 다음 명령어를 실행합니다.

```bash
python main.py
```

## 메뉴 구성

프로그램을 실행하면 다음 메뉴가 표시됩니다.

```text
=== 나만의 프롬프트 관리 ===

1. 프롬프트 추가
2. 프롬프트 목록
3. 카테고리별 조회
4. 프롬프트 검색
5. 프롬프트 상세 보기
6. 즐겨찾기 관리
7. 즐겨찾기 목록
0. 종료
```

## 카테고리

프롬프트는 다음 카테고리로 관리할 수 있습니다.

| 카테고리   | 설명                          |
| ------ | --------------------------- |
| 텍스트 생성 | 글 작성, 요약, 답변 등 텍스트 생성용 프롬프트 |
| 이미지 생성 | AI 이미지 제작을 위한 프롬프트          |
| 영상 생성  | AI 영상 제작을 위한 프롬프트           |
| 페르소나   | AI의 역할과 전문성을 설정하는 프롬프트      |
| 자동화    | 반복 작업 및 업무 자동화를 위한 프롬프트     |
| 기타     | 위 카테고리에 포함되지 않는 프롬프트        |

## 데이터 구조

프롬프트 데이터는 Python의 **리스트와 딕셔너리**를 사용하여 관리합니다.

각 프롬프트는 다음 정보를 포함합니다.

* 제목
* 내용
* 카테고리
* 즐겨찾기 여부

현재 버전에서는 데이터를 별도의 파일이나 데이터베이스에 저장하지 않으며, 프로그램을 종료하면 실행 중 추가·변경한 데이터가 초기화됩니다.

## 기본 제공 프롬프트

프로그램 실행 시 이전 미션에서 작성한 프롬프트가 기본 데이터로 등록되어 있습니다.

* 교육생 문의사항 응대 봇
* Tripmind AI 광고 - 지친 여행자 탈출
* 핵심 쏙쏙 회의록 요약

## 프로젝트 구조

```text
prompt-manager/
├── main.py       # 프롬프트 관리 프로그램
├── README.md     # 프로젝트 설명 및 사용 방법
└── .gitignore    # Git 관리에서 제외할 파일 설정
``` 

## 개발 환경

* Python 3.10 이상
* Visual Studio Code
* Git
* GitHub

## 프로젝트 실행 및 주요 화면

### 1. GitHub 프로젝트 구조

GitHub 저장소에서 프로젝트 파일과 README를 확인할 수 있습니다.

![GitHub 프로젝트 구조]

<img width="1192" height="946" alt="01_github" src="https://github.com/user-attachments/assets/57f0cba2-d228-479e-8ef6-108485130525" />



### 2. 프로그램 실행

`python main.py` 명령어를 통해 프로그램을 실행합니다.

![프로그램 실행]

<img width="333" height="210" alt="02_main" src="https://github.com/user-attachments/assets/d7ccac70-ffe5-48a2-9210-b01a7068a50c" />


### 3. 프롬프트 목록 조회

등록된 프롬프트의 제목, 카테고리 및 즐겨찾기 상태를 확인할 수 있습니다.

![프롬프트 목록]

<img width="378" height="157" alt="03_list" src="https://github.com/user-attachments/assets/d0f5821d-1903-47da-96d4-cdfa7591ff53" />


### 4. 프롬프트 검색

검색어를 입력하여 원하는 프롬프트를 검색할 수 있습니다.

![프롬프트 검색]

<img width="380" height="178" alt="04_search" src="https://github.com/user-attachments/assets/283cbb12-2852-4ddc-876a-6b35a2defba5" />



### 5. 즐겨찾기 추가

원하는 프롬프트를 선택하여 즐겨찾기로 추가하거나 해제할 수 있습니다.

![즐겨찾기 추가]

<img width="402" height="179" alt="05_favorite" src="https://github.com/user-attachments/assets/f8c8bff2-b3e9-4b5b-98fb-f85d9160a263" />


### 6. 즐겨찾기 목록

즐겨찾기로 등록된 프롬프트만 별도로 확인할 수 있습니다.

![즐겨찾기 목록]

<img width="273" height="129" alt="06_favorites" src="https://github.com/user-attachments/assets/5d634aa4-7b1c-4d71-99d0-66a2accbd4f7" />



### 7. 프롬프트 추가 기능 구현

`add_prompt()` 함수를 통해 제목, 내용, 카테고리를 입력받고 새로운 프롬프트를 리스트에 추가하도록 구현했습니다.

![프롬프트 추가 코드]

<img width="688" height="613" alt="07_add_prompt" src="https://github.com/user-attachments/assets/c68ec27a-6bc3-493e-bc7b-9e173edb8702" />



### 8. 메뉴 출력 기능 구현

`show_menu()` 함수를 통해 프로그램의 주요 기능을 메뉴 형태로 출력하도록 구현했습니다.

![메뉴 출력 코드]

<img width="690" height="557" alt="08_show_menu" src="https://github.com/user-attachments/assets/9fc5c17d-c7f6-4ef3-bc60-396ed988e42a" />


## 프로젝트 목적

이 프로젝트를 통해 Python의 기본 문법을 활용하여 실제 동작하는 프로그램을 구현하고, Git과 GitHub를 이용하여 코드의 변경 이력을 관리하는 방법을 학습하는 것을 목표로 합니다.
