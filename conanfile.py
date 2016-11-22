from conans import ConanFile
from conans.tools import download, check_sha256

class StbImageWriteConan(ConanFile):
    name = "stb_image_write"
    version = "1.02"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/fr00b0/conan-stb_image_write"

    header_file = "stb_image_write.h"
    download_url = "https://raw.githubusercontent.com/nothings/stb/6e4154737c51c1298e35cc6fc387dd365cc32ac9/stb_image_write.h"
    sha256_hash = "036c580e7256758362de81519acaff0cc94c2b860dbf51f36137751a16ab66cf"

    def source(self):
        download(self.download_url, self.header_file)
        check_sha256(self.header_file, self.sha256_hash)

    def build(self):
        pass  # Header only library

    def package(self):
        self.copy(self.header_file, dst="include/stb", src=".")

    def package_info(self):
        pass  # Header only library
