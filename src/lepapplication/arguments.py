import argparse


def get_args() -> tuple[str, dict[str, str]]:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "command",
        type=str,
        help="The command to execute.",
    )

    option, unknown = parser.parse_known_args()

    for arg in unknown:
        if arg.startswith(("-", "--")):
            parser.add_argument(
                arg.split("=")[0],
                type=str,
            )

    data = parser.parse_args(unknown).__dict__

    return option, data
