from ..common import agent


def validate_result(claim: str) -> str:
    """Check a claim against existing knowledge."""
    return agent.chat(
        f"Does the following claim contradict known results? {claim}"
    )


if __name__ == "__main__":
    example = "Our method outperforms all others on dataset XYZ."
    print(validate_result(example))
