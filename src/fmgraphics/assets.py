"""Asset types."""

from pathlib import Path

from fmgraphics import Image


class Face(Image):
    """Class representing a face asset in Football Manager graphics."""

    def __init__(self, filepath: Path):
        """Initialize the Face class.

        Parameters
        ----------
        filepath : Path
            The path to the image file.
        """
        super().__init__(filepath, asset="face")

    @property
    def _xml_path(self) -> str:
        """Return the path in the Football Manager graphics directory structure."""
        return f"graphics/pictures/person/{self.key}/portrait"
