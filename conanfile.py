from conans import ConanFile, CMake, tools
import os

class LadspaConan(ConanFile):
    name = "ladspa"
    version = "1.13"
    description = "LADSPA is a standard that allows software audio processors and effects to "
    "be plugged into a wide range of audio synthesis and recording packages."
    url = "https://github.com/conan-multimedia/ladspa"
    homepage = "http://www.ladspa.org/"
    license = "LGPLv2_1"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    source_subfolder = "source_subfolder"

    def source(self):
        url_ = "http://www.ladspa.org/download/{name}_sdk_{version}.tgz"
        tools.get(url_.format(name=self.name, version=self.version))
        os.rename("%s_sdk"%(self.name), self.source_subfolder)


    def build(self):
        pass

    def package(self):
        if tools.os_info.is_linux:
            with tools.chdir(self.source_subfolder):
                self.copy("ladspa.h", dst="include", src="%s/src"%(os.getcwd()))

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)