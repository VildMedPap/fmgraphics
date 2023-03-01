import pytest
from pathlib import Path

from fmgraphics import Image


class TestImage:
    def test_image_key(self):
        # Given
        filepath = Path("./12345678.png")
        asset = "faces"

        # When
        image = Image(filepath, asset)

        # Then
        assert image.key == "12345678"

    def test_image_repr(self):
        # Given
        filepath = Path("./12345678.png")
        asset = "faces"

        # When
        image = Image(filepath, asset)

        # Then
        assert repr(image) == "Image(key=12345678)"

    def test_xml_path_not_implemented_error(self):
        # Given
        filepath = Path("./images/123.png")
        asset = "faces"

        # When
        image = Image(filepath, asset)

        # Then
        with pytest.raises(NotImplementedError):
            image._xml_path
