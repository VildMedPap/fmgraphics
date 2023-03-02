from pathlib import Path

from fmgraphics.assets import (
    Face,
    FaceIcon,
    Asset,
    Logo,
    LogoIcon,
    LogoHuge,
    KitHome2D,
    KitAway2D,
    KitThird2D,
    KitHome3D,
    KitAway3D,
    KitThird3D,
)
import lxml.etree


class TestAsset:
    def test_asset_key(self):
        # Given
        filepath = Path("./123.png")
        asset_category = ""
        asset = ""

        # When
        asset = Asset(filepath, asset_category, asset)

        # Then
        assert asset.key == "123"

    def test_asset_repr(self):
        # Given
        filepath = Path("./123.png")
        asset_category = ""
        asset = ""

        # When
        asset = Asset(filepath, asset_category, asset)

        # Then
        assert repr(asset) == "Asset(key=123)"

    def test_xml_path_not_implemented_error(self):
        # Given
        filepath = Path("./123.png")
        asset_category = "a"
        asset = "b"

        # When
        asset = Asset(filepath, asset_category, asset)

        # Then
        assert asset._xml_path == f"graphics/pictures/a/123/b"


class BaseAssetTest:
    cls: Asset
    key: str
    path: Path
    asset_category: str
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
    asset_category = "person"
    asset = "portrait"
    xml_path = f"graphics/pictures/{asset_category}/{key}/{asset}"
    repr_ = f"{cls.__name__}(key={key})"


class TestFaceIcon(BaseAssetTest):
    cls = FaceIcon
    key = "123"
    path = Path(f"./{key}.png")
    asset_category = "person"
    asset = "icon"
    xml_path = f"graphics/pictures/{asset_category}/{key}/{asset}"
    repr_ = f"{cls.__name__}(key={key})"


class TestLogo(BaseAssetTest):
    cls = Logo
    key = "123"
    path = Path(f"./{key}.png")
    asset_category = "club"
    asset = "logo"
    xml_path = f"graphics/pictures/{asset_category}/{key}/{asset}"
    repr_ = f"{cls.__name__}(key={key})"


class TestIcon(BaseAssetTest):
    cls = LogoIcon
    key = "123"
    path = Path(f"./{key}.png")
    asset_category = "club"
    asset = "icon"
    xml_path = f"graphics/pictures/{asset_category}/{key}/{asset}"
    repr_ = f"{cls.__name__}(key={key})"


class TestHugeLogo(BaseAssetTest):
    cls = LogoHuge
    key = "123"
    path = Path(f"./{key}.png")
    asset_category = "club"
    asset = "logo/huge"
    xml_path = f"graphics/pictures/{asset_category}/{key}/{asset}"
    repr_ = f"{cls.__name__}(key={key})"


class TestKitHome2D(BaseAssetTest):
    cls = KitHome2D
    key = "123"
    path = Path(f"./{key}.png")
    asset_category = "team"
    asset = "kits/home"
    xml_path = f"graphics/pictures/{asset_category}/{key}/{asset}"
    repr_ = f"{cls.__name__}(key={key})"


class TestKitAway2D(BaseAssetTest):
    cls = KitAway2D
    key = "123"
    path = Path(f"./{key}.png")
    asset_category = "team"
    asset = "kits/away"
    xml_path = f"graphics/pictures/{asset_category}/{key}/{asset}"
    repr_ = f"{cls.__name__}(key={key})"


class TestKitThird2D(BaseAssetTest):
    cls = KitThird2D
    key = "123"
    path = Path(f"./{key}.png")
    asset_category = "team"
    asset = "kits/third"
    xml_path = f"graphics/pictures/{asset_category}/{key}/{asset}"
    repr_ = f"{cls.__name__}(key={key})"


class TestKitHome3D(BaseAssetTest):
    cls = KitHome3D
    key = "123"
    path = Path(f"./{key}.png")
    asset_category = "team"
    asset = "kit_textures/home"
    xml_path = f"graphics/pictures/{asset_category}/{key}/{asset}"
    repr_ = f"{cls.__name__}(key={key})"


class TestKitAway3D(BaseAssetTest):
    cls = KitAway3D
    key = "123"
    path = Path(f"./{key}.png")
    asset_category = "team"
    asset = "kit_textures/away"
    xml_path = f"graphics/pictures/{asset_category}/{key}/{asset}"
    repr_ = f"{cls.__name__}(key={key})"


class TestKitThird3D(BaseAssetTest):
    cls = KitThird3D
    key = "123"
    path = Path(f"./{key}.png")
    asset_category = "team"
    asset = "kit_textures/third"
    xml_path = f"graphics/pictures/{asset_category}/{key}/{asset}"
    repr_ = f"{cls.__name__}(key={key})"
