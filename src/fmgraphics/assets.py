"""Asset types."""

from pathlib import Path

from lxml.etree import Element, tostring


class Asset:
    """A class representing a single asset in the Football Manager graphics."""

    def __init__(self, filepath: Path, asset: str):
        """Initialize the Asset class.

        Parameters
        ----------
        filepath : Path
            The path to the image file.
        asset : str
            The type of asset (e.g. face, logo, kit).

        """
        self.filepath = filepath
        self.asset = asset

    def __repr__(self) -> str:
        """Return a string representation of the Asset class.

        Returns
        -------
        str
            A string representation of the Asset class.

        """
        return f"{self.__class__.__name__}(key={self.key})"

    def __str__(self) -> str:
        """Return a string representation of the xml representation of the Asset class.

        Returns
        -------
        str
            A string representation of the xml representation of the Asset class.

        """
        return tostring(self.xml).decode()

    @property
    def key(self) -> str:
        """Return the key of the image.

        Returns
        -------
        str
            The key of the image.

        """
        return self.filepath.name.split(".")[0]

    @property
    def _xml_key(self) -> str:
        """Return the xml key of the image.

        Returns
        -------
        str
            The xml key of the image.

        """
        return self.key

    @property
    def _xml_path(self) -> str:
        """Return the xml path of the image.

        Returns
        -------
        str
            The xml path of the image.

        """
        raise NotImplementedError

    @property
    def xml(self) -> Element:
        """Return the xml representation of the image.

        Returns
        -------
        Element
            The xml representation of the image.

        """
        record = Element("record")
        record.set("from", self._xml_key)
        record.set("to", self._xml_path)
        return record


class Face(Asset):
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
