from typing import Any

from .. import Command, namespaces

class install_egg_info(namespaces.Installer, Command):
    description: str
    user_options: Any
    install_dir: Any
    def initialize_options(self) -> None: ...
    source: Any
    target: Any
    outputs: Any
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def get_outputs(self): ...
    def copytree(self): ...
