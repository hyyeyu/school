# 크리에이터 레이트 계산기

## 프로젝트 소개

이 저장소는 한국 인플루언서와 광고주를 위한 광고 단가 계산기 MVP의 기획 문서와 정적 프로토타입을 담고 있습니다.

사용자는 플랫폼, 팔로워 수, 평균 조회수, 참여율, 콘텐츠 형식, 광고 사용권, 독점 조건 등을 입력하면 적정 광고 단가 범위와 기본 제안가를 산출할 수 있습니다. 결과는 단순한 숫자 제시가 아니라 계산 근거, 신뢰도, 조정 요소를 함께 보여 주어 협상 시작점을 설명 가능하게 합니다.

## 현재 저장소 상태

이 프로젝트는 제품 기획 문서와 정적 HTML 프로토타입으로 구성된 MVP입니다.

- [PRD.md](PRD.md): 제품 요구사항
- [wireframe.html](wireframe.html): 반응형 프로토타입
- [presentation.html](presentation.html): 발표 자료

## 로컬 실행

브라우저에서 `wireframe.html`을 직접 열거나 다음 명령으로 서버를 실행합니다.

```bash
python -m http.server 8000
```

접속 주소: `http://localhost:8000/wireframe.html`

## CI/CD 최적화

GitHub Actions는 Build, 품질 검사, 선택적 배포를 수행합니다.

- **Reusable Workflow**: `.github/workflows/reusable-python-checks.yml`에서 공통 Lint/Test 단계를 정의합니다.
- **Composite Action**: `.github/actions/python-quality/action.yml`에서 Python 설치, pip 캐시, Ruff 설치를 재사용합니다.
- **Matrix**: Ubuntu, Windows, macOS와 Python 3.11~3.14의 12개 조합을 검사합니다.
- **Cache**: `actions/setup-python`의 pip 캐시를 사용하며 캐시 키는 `pyproject.toml`을 기준으로 합니다.
- **변경 파일 감지**: `dorny/paths-filter`로 사이트·코드·문서 변경을 구분합니다. 사이트 변경이 없으면 Pages 빌드/배포를 생략합니다.
- **배포 조건**: `main` 브랜치 Push이며 사이트 변경, 빌드 성공, Matrix 품질 검사 성공을 모두 만족할 때만 배포합니다.
- **Secrets**: 필요 시 `DEPLOYMENT_WEBHOOK_URL`을 Repository Secret으로 등록합니다. 미등록이어도 기본 배포는 진행됩니다.

### 로컬 검사

```bash
python scripts/build.py
python -m pip install ruff
ruff check scripts tests
python -m unittest discover -s tests -v
```

### 캐시 성능 비교

Actions → **Cache Performance Benchmark** → **Run workflow**를 실행하면 캐시 미사용 설치와 캐시 사용 설치 시간을 별도로 측정하고 개선률을 Markdown 리포트 아티팩트로 생성합니다. 전체 CI 시간과 패키지 설치 시간은 구분해서 해석해야 합니다.

## GitHub Pages

Settings → Pages → Build and deployment → Source를 **GitHub Actions**로 설정해야 합니다.

## 오픈소스 안내

- [기여 가이드](CONTRIBUTING.md)
- [행동 강령](CODE_OF_CONDUCT.md)
- [MIT 라이선스](LICENSE)
