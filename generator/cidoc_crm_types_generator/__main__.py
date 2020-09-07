import logging
from argparse import ArgumentParser
from pathlib import Path
from urllib.request import urlopen

from rdflib import Graph

from cidoc_crm_types_generator.ecrm_owl_parser import EcrmOwlParser
from cidoc_crm_types_generator.py_generator import PyGenerator

ROOT_DIR_PATH = Path(__file__).parent.parent.parent.absolute()


class Main:
    __GENERATOR_CLASSES = (PyGenerator,)

    def __configure_logging(self, args):
        args_dict = args.__dict__

        if args_dict.get("debug", False):
            logging_level = logging.DEBUG
        elif args_dict.get("logging_level") is not None:
            logging_level = getattr(logging, args["logging_level"].upper())
        else:
            logging_level = logging.INFO
        logging.basicConfig(
            format="%(asctime)s:%(module)s:%(lineno)s:%(name)s:%(levelname)s: %(message)s",
            level=logging_level,
        )
        self.__logger = logging.getLogger(self.__class__.__name__)

    def __download_ecrm_owl(self, ecrm_owl_url: str) -> Path:
        ecrm_owl_file_path = ROOT_DIR_PATH / "generator" / "data" / "ecrm.owl"
        if ecrm_owl_file_path.is_file():
            self.__logger.info(
                "%s already exists, skipping download", ecrm_owl_file_path
            )
            return ecrm_owl_file_path
        self.__logger.info("downloading %s to %s", ecrm_owl_url, ecrm_owl_file_path)
        try:
            f = urlopen(ecrm_owl_url)
            ecrm_owl = f.read()
        finally:
            f.close()
        with open(ecrm_owl_file_path, "w+b") as ecrm_owl_file:
            ecrm_owl_file.write(ecrm_owl)
        self.__logger.info("downloaded %s to %s", ecrm_owl_url, ecrm_owl_file_path)
        return ecrm_owl_file_path

    def main(self):
        args = self.__parse_args()

        self.__configure_logging(args)

        ecrm_owl_file_path = self.__download_ecrm_owl(ecrm_owl_url=args.ecrm_owl_url)
        ecrm_owl_graph = Graph()
        ecrm_owl_graph.parse(source=str(ecrm_owl_file_path), format="xml")

        ecrm_owl = EcrmOwlParser().parse(ecrm_owl_graph)

        generator_kwds = args.__dict__.copy()
        for key in ("debug", "ecrm_owl_url", "logging_level", "output_dir_path"):
            try:
                generator_kwds.pop(key)
            except KeyError:
                pass

        try:
            output_dir_path = args.output_dir_path
        except AttributeError:
            output_dir_path = None
        if output_dir_path is not None:
            output_dir_path = Path(output_dir_path)

        generators = []
        if args.__dict__.get("generator_class") is not None:
            generators.append(
                args.generator_class(
                    output_dir_path=output_dir_path
                    if output_dir_path is not None
                    else ROOT_DIR_PATH / args.generator_class.language(),
                    **generator_kwds
                )
            )
        else:
            # Run all generators
            for generator_class in self.__GENERATOR_CLASSES:
                generators.append(
                    generator_class(
                        output_dir_path=output_dir_path / generator_class.language()
                        if output_dir_path is not None
                        else ROOT_DIR_PATH / generator_class.language(),
                        **generator_kwds
                    )
                )

        for generator in generators:
            generator.generate(ecrm_owl=ecrm_owl)

    def __parse_args(self):
        def add_global_arguments(arg_parser: ArgumentParser):
            arg_parser.add_argument(
                "--debug", action="store_true", help="turn on debugging"
            )
            arg_parser.add_argument(
                "--ecrm-owl-url",
                default="https://raw.githubusercontent.com/erlangen-crm/ecrm/master/ecrm_current.owl",
            )
            arg_parser.add_argument(
                "--logging-level",
                help="set logging-level level (see Python logging module)",
            )
            arg_parser.add_argument(
                "-o", "--output-dir-path", help="directory path to write output to"
            )

        arg_parser = ArgumentParser()
        add_global_arguments(arg_parser)
        subparsers = arg_parser.add_subparsers()
        for generator_class in self.__GENERATOR_CLASSES:
            generator_subparser = subparsers.add_parser(
                "gen-" + generator_class.language()
            )
            generator_subparser.set_defaults(generator_class=generator_class)
            add_global_arguments(generator_subparser)

        return arg_parser.parse_args()


assert __name__ == "__main__"
Main().main()
