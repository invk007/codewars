from collections import Counter


def count_effect(word: str) -> int:
    counter = Counter(word.lower())
    if (
        counter['c'] >= 1
        and counter['t'] >= 1
        and counter['e'] // 2 >= 1
        and counter['f'] // 2 >= 1
    ):
        return min(
            counter['c'], counter['t'], counter['e'] // 2, counter['f'] // 2
        )
    return 0


if __name__ == '__main__':
    assert count_effect('Effect') == 1
    assert count_effect('efect') == 0
    assert count_effect('eeeefffeeeccct') == 1
    assert count_effect('eeffcccctt') == 1
    assert count_effect('tteeeeeeeeeefffffffc') == 1
