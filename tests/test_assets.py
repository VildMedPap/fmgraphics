from pathlib import Path

from fmgraphics.assets import Face
import lxml.etree


class TestFace:
    def test_init(self):
        # Given
        filepath = Path("./123.png")

        # When
        face = Face(filepath)

        # Then
        assert face.filepath == filepath
        assert face.asset == "face"

    def test_xml_path(self):
        # Given
        filepath = Path("./123.png")

        # When
        face = Face(filepath)

        # Then
        assert face._xml_path == "graphics/pictures/person/123/portrait"

    def test_repr(self):
        # Given
        filepath = Path("./123.png")

        # When
        face = Face(filepath)

        # Then
        assert repr(face) == "Face(key=123)"

    def test_xml(self):
        # Given
        filepath = Path("./123.png")

        # When
        face = Face(filepath)

        # Then
        assert face.xml.tag == "record"
        assert face.xml.attrib["from"] == "123"
        assert face.xml.attrib["to"] == "graphics/pictures/person/123/portrait"

    def test_str(self):
        # Given
        filepath = Path("./123.png")

        # When
        face = Face(filepath)
        xml_str = str(face)
        xml = lxml.etree.fromstring(xml_str)

        # Then
        assert xml.tag == "record"
        assert xml.attrib["from"] == "123"
        assert xml.attrib["to"] == "graphics/pictures/person/123/portrait"
