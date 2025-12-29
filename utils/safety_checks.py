import os


def require_env(vars_required: list):
    missing = [v for v in vars_required if not os.getenv(v)]

    if missing:
        raise EnvironmentError(
            f"Missing required ENV variables: {', '.join(missing)}"
        )


def optional_env(var: str):
    return os.getenv(var)
