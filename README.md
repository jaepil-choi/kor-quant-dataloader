# kor-quant-dataloader (kqdl)

## Overview
`kor-quant-dataloader` (kqdl)는 `pykrx`와 같은 서드파티 라이브러리를 위한 wrapper로서, 한국 주식 시장에 중점을 둔 퀀트 리서치를 위해 설계되었습니다. 이 라이브러리는 금융 데이터의 로딩 및 처리 과정을 간소화하여, 상장 폐지 주식을 포함한 포괄적인 데이터셋을 제공합니다. 이를 통해 생존 편향을 제거하고, 다양한 분석 요구에 맞는 데이터 형식을 지원합니다.

`kor-quant-dataloader` (kqdl) is designed as a wrapper for third-party libraries such as `pykrx`, specifically created for quantitative research focused on the Korean stock market. The library simplifies the process of loading and processing financial data, offering a comprehensive dataset that includes data for delisted stocks. This approach effectively eliminates survivorship bias and supports various data formats to meet diverse analytical requirements.

## Features
- **시작 및 종료 날짜, 유니버스 선택**: 사용자가 지정한 시작 및 종료 날짜와 주식 유니버스를 선택하여, 해당 설정에 기반한 데이터셋을 검색할 수 있습니다.
- **생존 편향 없는 데이터 포함**: 상장 폐지 주식 데이터 포함.
- **다양한 데이터 형식 지원**: 전통적 분석을 위한 와이드 포맷 및 ML 기반 접근을 위한 멀티 인덱스 포맷 지원.
- **공휴일 처리 옵션**: 데이터셋에서 공휴일 제외.

- **Flexible Date Range and Customizable Universe**: Users can specify start and end dates and select a specific universe of stocks, enabling them to retrieve datasets based on these settings.
- **Survivorship Bias-Free**: Includes data for delisted stocks.
- **Various Data Formats**: Supports wide format for traditional analysis and multi-index format for ML-based approaches.
- **Holiday Handling**: Option to exclude holidays from the dataset.

## Installation

**Note**: `kor-quant-dataloader` is currently under development and has not yet been deployed to PyPI. As such, it cannot be installed via `pip` at this moment. This section will be updated once the package is available on PyPI.

To keep informed about the release and availability of `kor-quant-dataloader` on PyPI, you can watch or star the repository on GitHub for updates.

- Required Dependency
    - `pykrx`

## Quick Start
```python
import kor_quant_dataloader as kqdl

universe = ['000020', '005930']  # 예시 주식 코드들, None으로 설정 시 모든 가능한 주식이 자동으로 선택됩니다.

loader = kqdl.DataLoader(
    source='pykrx',
    start_date='2023-12-01',
    end_date='2023-12-10',
    universe=universe,
    remove_holidays=True,
)

data = '종가'  # str로 주어질 시 wide format 반환
data = ['종가', '시가총액', 'BPS']  # list로 주어질 시 multi-index format 반환

df = loader.get_data(data=data, download=False)
```

## Usage
`kor-quant-dataloader` 사용법은 간단합니다. 데이터 선택, 데이터 형식 지정 등의 다양한 옵션을 통해 사용자의 분석 요구에 맞춘 데이터셋을 쉽게 얻을 수 있습니다.

Using `kor-quant-dataloader` is straightforward. Users can easily obtain datasets tailored to their analytical needs with options like data selection and data format specification.

## Upcoming Features

**Korean:**
- `kqdl.show_catalog()`를 통해 사용 가능한 data source 및 데이터 조회.
- 로컬 데이터 저장 지원으로 보다 효율적인 데이터 로딩 지원.
- 분기별 재무제표 등 특정 데이터에 대한 forward-filling와 같은 데이터 처리 옵션.
- `FinanceDataReader` 및 `OpenDartReader`와 같은 다른 서드파티 라이브러리에 대한 향후 지원.
- 유동성 상위 100, 500, 1000, 2000 종목과 같은 사전 계산된 유니버스 제공으로 보다 현실적인 전략 탐색 지원.

**English:**
- Display of available data sources and queryable data through `kqdl.show_catalog()`.
- Support for local data storage to enhance efficient data loading.
- Data processing options such as forward-filling for specific datasets like quarterly financial statements.
- Future support for additional third-party libraries, including `FinanceDataReader` and `OpenDartReader`.
- Provision of pre-calculated universes based on liquidity, such as the top 100, 500, 1000, 2000 stocks, to support more realistic strategy exploration.

## Contributing
`kor_quant_dataloader`에 기여하는 것을 환영합니다. 기여 방법에 대한 지침은 `CONTRIBUTING.md` 파일을 참조해 주세요.
Contributions to `kor_quant_dataloader` are welcome! Please refer to the `CONTRIBUTING.md` file for guidelines on how to contribute.

## License
`kor-quant-dataloader`는 MIT 라이선스에 따라 제공되며, 라이선스 파일에서 확인할 수 있습니다.
`kor-quant-dataloader` is MIT licensed, as found in the LICENSE file.
