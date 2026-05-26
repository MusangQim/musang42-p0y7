from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex0.factory import CreatureFactory
from ex2.strategy import BattleStrategy
from typing import Tuple, List


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved\n")
    for i in range(len(opponents)):
        for j in range(i+1, len(opponents)):
            factory_a, strategy_a = opponents[i]
            factory_b, strategy_b = opponents[j]
            creature_a = factory_a.create_base()
            creature_b = factory_b.create_base()
            print("* Battle *")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print(" now fight!")
            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except Exception as e:
                print(F"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    flame_fac = FlameFactory()
    aqua_fac = AquaFactory()
    heal_fac = HealingCreatureFactory()
    transf_fac = TransformCreatureFactory()
    normal = NormalStrategy()
    defense = DefensiveStrategy()
    aggress = AggressiveStrategy()
    # --- TOURNAMENT 0 ---
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    battle([
        (flame_fac, normal),
        (heal_fac, defense)
    ])
    # --- TOURNAMENT 1 ---
    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([
        (flame_fac, aggress),
        (heal_fac, defense)
    ])
    # --- TOURNAMENT 2 ---
    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([
        (aqua_fac, normal),
        (heal_fac, defense),
        (transf_fac, aggress)
    ])


if __name__ == "__main__":
    main()
