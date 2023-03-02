from pathlib import Path

from fmgraphics.assets import Face, Asset, Logo, Icon, HugeLogo
import lxml.etree
import pytest


class TestAsset:
    def test_asset_key(self):
        # Given
        filepath = Path("./12345678.png")
        asset = "faces"

        # When
        asset = Asset(filepath, asset)

        # Then
        assert asset.key == "12345678"

    def test_asset_repr(self):
        # Given
        filepath = Path("./12345678.png")
        asset = "faces"

        # When
        asset = Asset(filepath, asset)

        # Then
        assert repr(asset) == "Asset(key=12345678)"

    def test_xml_path_not_implemented_error(self):
        # Given
        filepath = Path("./images/123.png")
        asset = "faces"

        # When
        asset = Asset(filepath, asset)

        # Then
        with pytest.raises(NotImplementedError):
            asset._xml_path


class BaseAssetTest:
    cls: Asset
    key: str
    path: Path
    asset: str
    xml_path: str
    repr_: str

    def test_init(self):
        # Given
        filepath = self.path

        # When
        asset = self.cls(filepath)

        # Then
        assert asset.filepath == filepath
        assert asset.asset == self.asset

    def test_xml_path(self):
        # Given
        filepath = self.path

        # When
        asset = self.cls(filepath)

        # Then
        assert asset._xml_path == self.xml_path

    def test_repr(self):
        # Given
        filepath = self.path

        # When
        asset = self.cls(filepath)

        # Then
        assert repr(asset) == self.repr_

    def test_xml(self):
        # Given
        filepath = self.path

        # When
        asset = self.cls(filepath)

        # Then
        assert asset.xml.tag == "record"
        assert asset.xml.attrib["from"] == self.key
        assert asset.xml.attrib["to"] == self.xml_path

    def test_str(self):
        # Given
        filepath = self.path

        # When
        asset = self.cls(filepath)
        xml_str = str(asset)
        xml = lxml.etree.fromstring(xml_str)

        # Then
        assert xml.tag == "record"
        assert xml.attrib["from"] == self.key
        assert xml.attrib["to"] == self.xml_path


class TestFace(BaseAssetTest):
    cls = Face
    key = "123"
    path = Path(f"./{key}.png")
    asset = "face"
    xml_path = f"graphics/pictures/person/{key}/portrait"
    repr_ = f"{asset.title()}(key={key})"


class TestLogo(BaseAssetTest):
    cls = Logo
    key = "123"
    path = Path(f"./{key}.png")
    asset = "logo"
    xml_path = f"graphics/pictures/club/{key}/logo"
    repr_ = f"{asset.title()}(key={key})"


class TestIcon(BaseAssetTest):
    cls = Icon
    key = "123"
    path = Path(f"./{key}.png")
    asset = "icon"
    xml_path = f"graphics/pictures/club/{key}/icon"
    repr_ = f"{asset.title()}(key={key})"


class TestHugeLogo(BaseAssetTest):
    cls = HugeLogo
    key = "123"
    path = Path(f"./{key}.png")
    asset = "huge_logo"
    xml_path = f"graphics/pictures/club/{key}/logo/huge"
    repr_ = f"HugeLogo(key={key})"
