from pathlib import Path

from fmgraphics.assets import Face
from fmgraphics.image import Image
import lxml.etree


class BaseAssetTest:
    cls: Image
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
