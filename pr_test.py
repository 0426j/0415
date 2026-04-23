# # 1. 대표의 원본 저장소를 로컬로 클론:
# #    git clone https://github.com/zoecodes-dev/project-main.git

# # 2. 작업 시작 전, 기준이 되는 develop 브랜치로 이동 및 최신화:
# #    git switch develop
# #    git pull origin develop

# # 3. 나만의 작업 브랜치 생성 (develop에서 뻗어 나오기):
# #    git switch -c feature-mytask

# # 4. VS Code에서 파일 수정 및 저장(Ctrl+S) 후 커밋:
# #    git add .
# #    git commit -m "수정 내용 상세 기술"

# # 5. 원본 저장소의 내 브랜치로 전송:
# #    git push origin feature-mytask

# ######################################

# 1. GitHub 웹 접속 -> 내가 방금 푸시한 브랜치의 [Compare & pull request] 클릭
# 2. 대상 브랜치 설정 확인:
#    - base: develop (받는 쪽)
#    - compare: feature-mytask (보내는 쪽 / 내 브랜치)
# 3. 변경 내용 작성 후 [Create pull request] 클릭
# 4. 대표(관리자)가 검토 후 Merge 하면 작업 완료