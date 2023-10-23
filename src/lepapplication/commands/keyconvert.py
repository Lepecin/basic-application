def data_to_args(**data: str) -> list[str]:
    return ["--" + key + "=" + value for key, value in data.items()]
