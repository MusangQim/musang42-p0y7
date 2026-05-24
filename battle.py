from ex0.factory import CreatureFactory, FlameFactory, AquaFactory


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    evolve = factory.create_evolved()
    print(base.describe())
    print(evolve.describe())


def battle(factory_a: CreatureFactory, factory_b: CreatureFactory) -> None:
    play_1 = factory_a.create_base()
    play_2 = factory_b.create_base()
    print(play_1.describe())
    print(play_2.describe())


def main() -> None:
    flame = FlameFactory()
    aqua = AquaFactory()

    print("Testing factory")
    test_factory(flame)

    print("Testing factory")
    test_factory(aqua)


if __name__ == "__main__":
    main()
