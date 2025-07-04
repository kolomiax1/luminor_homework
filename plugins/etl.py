import importlib
from typing import Any

from helpers.config import load_config


class ComponentFactory:
    """Factory class for creating components dynamically."""

    @classmethod
    def create_component(cls, config: dict) -> Any:
        module_path, class_name = config["location"].rsplit(".", 1)

        module = importlib.import_module(module_path)
        component_class = getattr(module, class_name)

        params = config.get("parameters")
        component = component_class(params) if params else component_class()

        for sub_name, sub_config in config.get("components", {}).items():
            sub_component = cls.create_component(sub_config)
            setattr(component, sub_name, sub_component)

        return component


class ETL:

    def __init__(self, config):
        self.config = config

        self.__build_components()

    def __build_components(self):
        for comp_name, comp_conf in self.config["components"].items():
            comp = ComponentFactory.create_component(comp_conf)
            setattr(self, comp_name, comp)

    @classmethod
    def from_yaml(cls, yaml_path: str) -> "ETL":
        return cls(load_config(yaml_path))

    def run(self):
        print(f"Starting {self.config['etl_name'] }ETL run")

        with self.extractor as extractor:
            extractor.connect()

            data = extractor.extract()

        with self.loader as loader:
            loader.connect()
            loader.load(data)

        print(f"{self.config['etl_name']} ETL run success")
