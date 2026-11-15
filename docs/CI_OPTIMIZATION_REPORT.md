# CI/CD 최적화 전후 비교 리포트

## 목적

Reusable Workflow, Composite Action, Matrix 확장, pip 캐시, 변경 파일 기반 선택적 배포를 적용하고 실행 효율을 비교한다.

## 최적화 전 기준선

기존 워크플로 실행 기록: [Run #9](https://github.com/hyyeyu/school/actions/runs/43717765967)

| 항목 | 관측 결과 |
|---|---:|
| Build job | 약 9초 (13:12:17~13:12:26 UTC) |
| Lint 단계 | 약 0초 후 실패 |
| 전체 파이프라인 | Lint 실패로 완료되지 않음 |
| 실패 원인 | `scripts/build.py` import 정렬 위반 (Ruff I001) |

기존 실행은 Lint 실패로 테스트·배포가 끝나지 않았으므로 전체 파이프라인의 최적화 전 완료 시간으로 사용할 수 없다. 이 기준선에서 전체 CI 개선률을 계산하지 않는다.

## 최적화 적용 내용

| 영역 | 기존 | 최적화 후 |
|---|---|---|
| Matrix | 3 OS × 3 Python = 9 조합 | 3 OS × 4 Python = 12 조합 |
| 공통 설정 | 워크플로마다 반복 | Composite Action으로 공통화 |
| Lint/Test 정의 | 단일 CI 파일 | Reusable Workflow로 분리 |
| 패키지 설치 | 매번 네트워크 설치 | setup-python pip cache |
| 실행 범위 | 모든 Push/PR에서 빌드·검사 | 변경 경로에 따라 필요한 작업만 실행 |
| 배포 | main Push 후 테스트 통과 | main Push + 사이트 변경 + Build/Quality 성공 |

## 캐시 전후 측정 방법

[Cache Performance Benchmark](../.github/workflows/cache-benchmark.yml)를 GitHub Actions에서 수동 실행한다.

1. Cold job: pip 캐시를 사용하지 않고 Ruff를 설치한 시간을 측정한다.
2. Warm job: pip 캐시를 준비한 뒤 캐시를 이용한 Ruff 재설치 시간을 측정한다.
3. Report job: 두 시간을 비교해 개선률을 계산하고 Markdown 리포트를 아티팩트로 업로드한다.

개선률 계산식:

`(캐시 미사용 시간 - 캐시 사용 시간) / 캐시 미사용 시간 × 100`

측정 결과는 Actions 실행의 `cache-performance-report` 아티팩트에서 확인한다.

## 결과 기입

| 측정 항목 | 결과 |
|---|---|
| Cold install | Benchmark 실행 후 자동 기록 |
| Warm install | Benchmark 실행 후 자동 기록 |
| 설치 시간 개선률 | Benchmark 실행 후 자동 계산 |
| 전체 CI 시간 | 동일한 변경 범위의 성공한 실행 3회 이상 평균 비교 권장 |

> 주의: 패키지 설치 시간 개선률은 전체 CI 시간 개선률과 다르다. 전체 CI 개선률은 동일한 OS, Python 버전, 변경 파일 범위에서 캐시 전후를 각각 여러 번 실행해 비교해야 한다. 측정하지 않은 수치를 임의로 기입하지 않는다.
