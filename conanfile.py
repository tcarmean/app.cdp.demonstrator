from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, cmake_layout, CMakedeps

class Demonstrator(ConanFile):
    name = "demonstrator"
    version = "0.1"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    requires = "module_a/0.1", "module_b/0.1"
    exports_sources = "CMakeLists.txt", "src/*", "include/*"

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.set_name("Demonstrator")
        self.cpp_info.set_version("0.1")
        self.cpp_info.set_description("A simple demonstrator")
        self.cpp_info.set_license("MIT")
        self.cpp_info.set_url("https://github.com/tcarmean/app.cdp.demonstrator")
