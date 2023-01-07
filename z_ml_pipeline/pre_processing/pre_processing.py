from abc import ABC, abstractmethod
from enum import Enum

__all__ = [
    "PreProcessingTypes",
    "IUniverseSelection",
    "SelectByExclusion",
    "SelectByInclusion",
    "IMissingData",
    "ForwardFill",
    "TrendSeasonality",
    "IOutliers",
    "Clipping",
]


class PreProcessingTypes(Enum):
    SELECTION_BY_EXCLUSION = "select_by_exclusion"
    SELECTION_BY_INCLUSION = "select_by_inclusion"
    FORWARD_FILL = "forward_fill"
    TREND_SEASONALITY = "trend_seasonality"
    CLIPPING = "clipping"

    ########################   PRE-PROCESSING   #############################


class IUniverseSelection(ABC):
    """Represents the interface for dealing with universe selection"""

    @abstractmethod
    def select_assets(
        self, universe: list[str], user_assets: list[str]
    ) -> (list[str] | None):
        """Filter overall available assets using some criteria"""

    def check_sublist(self, universe: list[str], user_assets: list[str]) -> bool:
        if not all(x in universe for x in user_assets):
            return False
        return True


class SelectByExclusion(IUniverseSelection):
    def select_assets(
        self, universe: list[str], user_assets: list[str]
    ) -> (list[str] | None):

        if not self.check_sublist(universe, user_assets):
            raise Exception("ERROR: check your list!")

        print("selected asset universe:")
        return list(set(universe) - set(user_assets))


class SelectByInclusion(IUniverseSelection):
    def select_assets(self, universe: list[str], user_assets: list[str]) -> list[str]:
        if not self.check_sublist(universe, user_assets):
            raise Exception("ERROR: check your list!")
        print("selected asset universe:")
        return user_assets


class IMissingData(ABC):
    """Represents the interface for dealing with missing values"""

    @abstractmethod
    def fill_missing_data(self) -> str:
        """Fill missing values of asset"""


class ForwardFill(IMissingData):
    def fill_missing_data(self) -> str:
        return "Forward Fill method"


class TrendSeasonality(IMissingData):
    def fill_missing_data(self) -> str:
        return "Trend and Seasonality method"


class IOutliers(ABC):
    """Represents the interface for dealing with outliers"""

    @abstractmethod
    def deal_with_outliers(self) -> str:
        """Deal with outlier of asset"""


class Clipping(IOutliers):
    def deal_with_outliers(self) -> str:
        return "Clipping method"


# class PreProcessingBuilder:
#     def build(
#         self,
#         asset_selection: IUniverseSelection,
#         missing_data: IMissingData,
#         outliers: IOutliers,
#     ):
#         print("\nStarting pre-processing step...")
#         print(f"asset_selection with: {asset_selection.select_assets()}")
#         print(f"missing data with: {missing_data.fill_missing_data()}")
#         print(f"outliers with: {outliers.deal_with_outliers()}")
#         print("done")
