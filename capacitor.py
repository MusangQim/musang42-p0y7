from ex1.factory import HealingCreatureFactory, TransformCreatureFactory


def test_heal(factory: HealingCreatureFactory) -> None:
    base = factory.create_base()
    evolve = factory.create_evolved()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())
    print(" evolved:")
    print(evolve.describe())
    print(evolve.attack())
    print(evolve.heal())


def test_transform(factory: TransformCreatureFactory) -> None:
    base = factory.create_base()
    evolve = factory.create_evolved()
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved:")
    print(evolve.describe())
    print(evolve.attack())
    print(evolve.transform())
    print(evolve.attack())
    print(evolve.revert())


def main() -> None:
    print("Testing Creature with healing capability")
    heal_factory = HealingCreatureFactory()
    test_heal(heal_factory)
    print("\nTesting Creature with transform capability")
    transform_factory = TransformCreatureFactory()
    test_transform(transform_factory)


if __name__ == "__main__":
    main()
