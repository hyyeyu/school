# 크리에이터 레이트 계산기

## 프로젝트 소개

이 저장소는 한국 인플루언서와 광고주를 위한 광고 단가 계산기 MVP의 기획 문서와 정적 프로토타입을 담고 있습니다.

사용자는 플랫폼, 팔로워 수, 평균 조회수, 참여율, 콘텐츠 형식, 광고 사용권, 독점 조건 등을 입력하면 적정 광고 단가 범위와 기본 제안가를 산출할 수 있습니다. 결과는 단순한 숫자 제시가 아니라 계산 근거, 신뢰도, 조정 요소를 함께 보여 주어 협상 시작점을 설명 가능하게 합니다.

## 핵심 목표

- 인플루언서가 자신의 광고 단가를 객관적으로 가늠할 수 있게 한다.
- 광고주가 여러 크리에이터의 견적을 같은 기준으로 비교할 수 있게 한다.
- 팔로워 수만이 아니라 실제 조회수, 참여율, 콘텐츠 조건을 반영한다.
- 결과를 협상용 견적으로 이해할 수 있도록 범위와 설명을 함께 제공한다.

## 현재 저장소 상태

이 프로젝트는 완전한 애플리케이션 프레임워크가 아니라, 제품 기획 문서와 정적 HTML 프로토타입으로 구성된 MVP 작업물입니다.

- 문서 기반 요구사항: [PRD.md](PRD.md)
- 와이어프레임/시뮬레이션: [wireframe.html](wireframe.html)
- 발표 자료: [creator-rate-presentation.md](creator-rate-presentation.md), [presentation.html](presentation.html)

현재 저장소는 정적 HTML 프로토타입과 이를 검증·배포하는 Python 기반 GitHub Actions CI를 사용합니다. 별도의 애플리케이션 서버나 패키지 매니저는 필요하지 않습니다.

## MVP 기능 요약

- 플랫폼 선택: Instagram, YouTube, TikTok, blog
- 콘텐츠 형식 선택: 피드 게시물, 릴스/숏폼, 스토리, 롱폼, 블로그 글
- 기본 입력: 팔로워 수, 조회수, 좋아요 수, 댓글 수
- 광고 조건 입력: 카테고리, 제작 난이도, 사용권, 독점 여부, 수정 횟수 등
- 결과 표시: 권장 견적 범위, 기본 제안가, 예상 도달 규모, 영향력 등급, 신뢰도, 계산 근거
- 공유/복사: URL 요약, 복사, 브라우저 인쇄 또는 PDF 저장 지원

## 계산 원칙

본 프로젝트는 단일 시장 가격을 고정값으로 판단하지 않고, 수치 기반의 설명 가능한 추정을 사용합니다.

- 참여율과 조회율을 반영해 영향력 점수를 산출한다.
- 카테고리, 콘텐츠 형식, 제작 난이도, 2차 활용권, 독점권을 가산 요소로 반영한다.
- 결과는 권장 견적 범위와 함께 제시하며, 실제 거래가는 캠페인 조건에 따라 달라질 수 있음을 안내한다.
- 입력값이 부족하거나 비현실적일 경우 신뢰도와 경고를 함께 표시한다.

## 문서 구조

- [PRD.md](PRD.md): 제품 범위, 사용자 흐름, 비기능 요구사항, 계산 모델을 정의하는 공식 문서
- [wireframe.html](wireframe.html): 모바일 우선 반응형 계산 폼과 결과 화면을 보여주는 정적 프로토타입
- [creator-rate-presentation.md](creator-rate-presentation.md): 프로젝트 발표용 마크다운 원본
- [presentation.html](presentation.html): 브라우저에서 바로 확인 가능한 발표 결과물

## 로컬 실행

이 저장소는 정적 HTML 중심 구조라 별도 설치 과정이 필요하지 않습니다. 브라우저에서 [wireframe.html](wireframe.html)을 직접 열면 프로토타입을 확인할 수 있습니다.

필요한 경우 저장소 폴더에서 다음 명령으로 로컬 웹 서버를 실행할 수 있습니다.

```bash
python -m http.server 8000
```

그다음 브라우저에서 `http://localhost:8000/wireframe.html`로 접속하면 됩니다.

## 오픈소스 참여 안내

프로젝트에 참여하기 전에 아래 문서를 확인해 주세요.

- [기여 가이드](CONTRIBUTING.md): 이슈 작성, 개발 확인, 커밋 및 Pull Request 절차
- [행동 강령](CODE_OF_CONDUCT.md): 커뮤니티에서 지켜야 할 상호 존중 원칙
- [MIT 라이선스](LICENSE): 사용, 수정 및 배포 조건

## CI/CD (GitHub Actions)

[.github/workflows/ci.yml](.github/workflows/ci.yml)은 다음 파이프라인을 자동 실행합니다.

1. **Build**: Python 표준 라이브러리로 `wireframe.html`을 `dist/index.html`로 패키징하고 아티팩트를 업로드합니다.
2. **Test**: Build 아티팩트를 다운로드한 뒤 Ruff 정적 검사와 Python `unittest` 스모크 테스트를 실행합니다.
3. **Deploy**: `main` 브랜치에 Push된 변경이 Build와 모든 Matrix 테스트를 통과하면 GitHub Pages로 배포합니다.

테스트 Matrix는 Ubuntu, Windows, macOS와 Python 3.11, 3.12, 3.13 조합(총 9개 환경)입니다.

### 로컬 CI 실행

```bash
python scripts/build.py
python -m pip install ruff
ruff check scripts tests
python -m unittest discover -s tests -v
```

### GitHub Pages 및 Secrets 설정

- 저장소 **Settings → Pages → Build and deployment → Source**를 **GitHub Actions**로 설정해야 배포할 수 있습니다.
- 외부 배포 모니터 알림을 사용할 경우 **Settings → Secrets and variables → Actions → New repository secret**에서 `DEPLOYMENT_WEBHOOK_URL`을 등록합니다. 이 값은 배포 후 알림 단계에만 환경 변수로 전달되며 로그에 출력하지 않습니다. 등록하지 않아도 GitHub Pages 배포는 진행됩니다.
- 현재 프로토타입에는 외부 API 키가 필요하지 않으므로 불필요한 비밀정보를 추가하지 않습니다.

## 주의 사항

- 계산 결과는 참고용 권장 견적이며, 시장 가격의 보장값이 아닙니다.
- 개인정보를 수집하지 않는 MVP를 우선합니다.
- 사용자에게 보여지는 문구는 한국어를 기본으로 하며, 필요한 경우 영어 용어만 예외적으로 사용합니다.
- 입력값과 계산 로직은 테스트 가능한 순수 함수 형태로 분리하는 방향을 목표로 합니다.

## 관련 문서

- [PRD.md](PRD.md)
- [AGENTS.md](AGENTS.md)
- [creator-rate-presentation.md](creator-rate-presentation.md)
- [wireframe.html](wireframe.html)
