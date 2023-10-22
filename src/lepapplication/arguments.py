import argparse


def get_args() -> tuple[str, dict[str, str]]:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "command",
        type=str,
        help="The command to execute.",
    )

    method, unknown = parser.parse_known_args()
    command = method.command

    parser = argparse.ArgumentParser()

    for arg in unknown:
        if arg.startswith(("-", "--")):
            parser.add_argument(
                arg.split("=")[0],
                type=str,
            )

    data = parser.parse_args(unknown).__dict__

    return command, data
