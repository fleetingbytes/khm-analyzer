from pytest import mark

from .conftest import CLI_FLAG_FOR_XML_DOWNLOAD

xml_download = mark.skipif(
    f"not config.getoption('{CLI_FLAG_FOR_XML_DOWNLOAD}')",
    reason=f"Use {CLI_FLAG_FOR_XML_DOWNLOAD} to run these tests",
)
