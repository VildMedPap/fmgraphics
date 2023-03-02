"""Asset types."""

from pathlib import Path

from lxml.etree import Element, tostring


class Asset:
    """A class representing a single asset in the Football Manager graphics."""

    def __init__(self, filepath: Path, asset_category: str, asset: str):
        """Initialize the Asset class.

        Parameters
        ----------
        filepath : Path
            The path to the image file.
        asset_category : str
            The categpry of asset (e.g. club, person, etc.)
        asset : str
            The type of asset (e.g. portrait, logo, icon, etc.)

        """
        self.filepath = filepath
        self.asset_category = asset_category
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
        return f"graphics/pictures/{self.asset_category}/{self.key}/{self.asset}"

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
        super().__init__(filepath, asset_category="person", asset="portrait")


class Logo(Asset):
    """Class representing a logo asset in Football Manager graphics."""

    def __init__(self, filepath: Path):
        """Initialize the Logo class.

        Parameters
        ----------
        filepath : Path
            The path to the image file.
        """
        super().__init__(filepath, asset_category="club", asset="logo")


class LogoIcon(Asset):
    """Class representing an logo icon asset in Football Manager graphics."""

    def __init__(self, filepath: Path):
        """Initialize the Icon class.

        Parameters
        ----------
        filepath : Path
            The path to the image file.
        """
        super().__init__(filepath, asset_category="club", asset="icon")


class LogoHuge(Asset):
    """Class representing a huge logo asset in Football Manager graphics."""

    def __init__(self, filepath: Path):
        """Initialize the HugeLogo class.

        Parameters
        ----------
        filepath : Path
            The path to the image file.
        """
        super().__init__(filepath, asset_category="club", asset="logo/huge")


class KitsHome2D(Asset):
    """Class representing a 2D home kit asset in Football Manager graphics."""

    def __init__(self, filepath: Path):
        """Initialize the KitsHome2D class.

        Parameters
        ----------
        filepath : Path
            The path to the image file.
        """
        super().__init__(filepath, asset_category="team", asset="kits/home")


class KitsAway2D(Asset):
    """Class representing a 2D away kit asset in Football Manager graphics."""

    def __init__(self, filepath: Path):
        """Initialize the KitsAway2D class.

        Parameters
        ----------
        filepath : Path
            The path to the image file.
        """
        super().__init__(filepath, asset_category="team", asset="kits/away")


class KitsThird2D(Asset):
    """Class representing a 2D third kit asset in Football Manager graphics."""

    def __init__(self, filepath: Path):
        """Initialize the KitsThird2D class.

        Parameters
        ----------
        filepath : Path
            The path to the image file.
        """
        super().__init__(filepath, asset_category="team", asset="kits/third")


class KitsHome3D(Asset):
    """Class representing a 3D home kit asset in Football Manager graphics."""

    def __init__(self, filepath: Path):
        """Initialize the KitsHome3D class.

        Parameters
        ----------
        filepath : Path
            The path to the image file.
        """
        super().__init__(filepath, asset_category="team", asset="kit_textures/home")


class KitsAway3D(Asset):
    """Class representing a 3D away kit asset in Football Manager graphics."""

    def __init__(self, filepath: Path):
        """Initialize the KitsAway3D class.

        Parameters
        ----------
        filepath : Path
            The path to the image file.
        """
        super().__init__(filepath, asset_category="team", asset="kit_textures/away")


class KitsThird3D(Asset):
    """Class representing a 3D third kit asset in Football Manager graphics."""

    def __init__(self, filepath: Path):
        """Initialize the KitsThird3D class.

        Parameters
        ----------
        filepath : Path
            The path to the image file.
        """
        super().__init__(filepath, asset_category="team", asset="kit_textures/third")
