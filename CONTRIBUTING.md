# 기여 가이드

이 문서는 `hyyeyu/school` 저장소에 기능을 추가하거나 버그를 수정할 때 사용하는 브랜치, 커밋, Pull Request 및 리뷰 규칙을 정의합니다.

## 1. Feature Branch 전략

`main` 브랜치에 직접 커밋하지 않고 작업 단위별 브랜치를 생성합니다.

```bash
git switch main
git pull origin main
git switch -c feature/<기능명>
```

브랜치 이름은 목적을 드러내도록 작성합니다.

- `feature/<name>`: 신규 기능
- `fix/<name>`: 버그 수정
- `docs/<name>`: 문서 변경
- `refactor/<name>`: 동작을 바꾸지 않는 구조 개선
- `test/<name>`: 테스트 추가 및 수정

## 2. Conventional Commits

모든 커밋 메시지는 다음 형식을 따릅니다.

```text
<type>(<scope>): <짧은 설명>
```

권장 type:

| Type | 사용 목적 |
| --- | --- |
| `feat` | 사용자 기능 추가 |
| `fix` | 버그 수정 |
| `docs` | 문서 변경 |
| `refactor` | 내부 구조 개선 |
| `test` | 테스트 추가 또는 수정 |
| `style` | 기능에 영향이 없는 서식 변경 |
| `chore` | 도구 및 저장소 설정 변경 |

예시: `docs(repo): add contribution workflow guide`

## 3. Pull Request 작성

작업 브랜치를 원격 저장소에 push한 뒤 `main`을 대상으로 PR을 생성합니다.

PR 본문에는 다음 내용을 포함합니다.

- 변경 목적과 배경
- 핵심 변경 사항
- 실행하거나 확인한 테스트와 결과
- 관련 Issue 링크
- UI 변경이 있다면 전후 스크린샷

작업이 완료되지 않았다면 Draft PR로 생성합니다. PR 제목도 Conventional Commits 형식을 권장합니다.

## 4. 코드 리뷰 기준

리뷰 의견은 근거와 개선 방향을 함께 제시하고 다음 태그를 사용합니다.

- `[MUST]`: 병합 전에 반드시 수정해야 하는 오류, 회귀 위험, 보안 또는 데이터 정확성 문제
- `[SHOULD]`: 유지보수성, 가독성, 사용성 향상을 위해 수정을 권장하는 사항

리뷰어는 변경된 코드와 관련 테스트를 확인하고, 문제가 없으면 승인하거나 추가 의견을 남깁니다. 작성자는 피드백을 반영한 뒤 리뷰어에게 재검토를 요청합니다.

## 5. 병합 전 체크리스트

- [ ] 기능별 브랜치에서 작업했는가?
- [ ] 커밋 메시지가 Conventional Commits 형식인가?
- [ ] PR 목적, 변경 사항, 테스트 결과를 작성했는가?
- [ ] 관련 동작을 직접 확인했는가?
- [ ] 모든 `[MUST]` 의견을 해결했는가?
- [ ] 필요한 문서와 화면 설명을 업데이트했는가?
