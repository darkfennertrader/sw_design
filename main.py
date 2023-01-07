# pylint: disable=unused-import
# pyright: reportUnusedImport=false
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Callable, Protocol

import pandas as pd

from z_ml_pipeline.pre_processing import (
    Clipping,
    ForwardFill,
    IMissingData,
    IOutliers,
    IUniverseSelection,
    SelectByExclusion,
    SelectByInclusion,
    TrendSeasonality,
)


class IPipeline(Protocol):
    def build(self) -> None:
        """Implement the pipeline"""


########################   FEATURE ENGINEERING   ##########################


class FeatEngineeringTypes(Enum):
    MOVING_AVERAGE = "moving_average"
    EXPONENTIAL_MOVING_AVERAGE = "exponential_moving_average"
    GARCH = "Garch"


class ITechnicalIndicator(ABC):
    """Represents the interface for building technical indicators"""

    @abstractmethod
    def technical_indicator(self) -> str:
        """Implement the technical indicator specified by the builder"""


class MovingAverage(ITechnicalIndicator):
    def technical_indicator(self) -> str:
        return "calculating Moving Average"


class ExponentialMovingAverage(ITechnicalIndicator):
    def technical_indicator(self) -> str:
        return "calculating Exponential Moving Average"


class IEconometricModel(ABC):
    """Represents the interface for building econometric models"""

    @abstractmethod
    def econometric_model(self) -> str:
        """Implement the econometric model specified by the builder"""


class Garch(IEconometricModel):
    def econometric_model(self) -> str:
        return "calculating Garch model"


@dataclass
class FeatureEngineeringBuilder:
    technical_indicators = ITechnicalIndicator
    econometric_model = IEconometricModel

    def build(self):
        return "building feature engineering phase"


################################################################################


# @dataclass
# class PipelineBuilder:
#     def build(
#         self,
#         pre_processing: PreProcessingBuilder,
#         feat_engineering: FeatureEngineeringBuilder,
#     ):
#         print("\nbuilding the pipeline")
#         print(f"{pre_processing}")
#         print(f"{feat_engineering}")
#         print("done!")


universe = ["AUDCAD", "EURUSD", "CHN50"]
user_assets = ["CHN50"]

idx = [datetime(2023, 1, 2), datetime(2023, 1, 3), datetime(2023, 1, 4)]
data = {"AUDCAD": [420, 380, 390], "EURUSD": [50, 40, 45], "CHN50": [10, 20, 90]}
df = pd.DataFrame(index=idx, data=data)

print(df)

# UNIVERSE_SELECTION: dict[str, Callable[[], IUniverseSelection]] = {
#     "exclusion": SelectByExclusion,
#     "inclusion": SelectByInclusion,
# }


NISSING_DATA: dict[str, Callable[[], IMissingData]] = {
    "forwardfill": ForwardFill,
    "trendseasonality": TrendSeasonality,
}


OUTLIERS: dict[str, Callable[[], IOutliers]] = {
    "clipping": Clipping,
}


if __name__ == "__main__":

    assets = SelectByExclusion()
    selected_assets = assets.select_assets(universe, user_assets)
    print(selected_assets)
    missing_step = ForwardFill()
    outliers_step = Clipping()

    # pre_processing_step = PreProcessingBuilder().build(
    #     universe, missing_step, outliers_step
    # )

    # pipeline = PipelineBuilder()
