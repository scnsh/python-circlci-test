import pytest

from abc142a import ABC142A


@pytest.mark.parametrize('_input, expected', [
    (["4"], [0.5000000000]),
    (["5"], [0.6000000000]),
    (["1"], [1.0000000000])
])
def test_abc142a(_input, expected):
    instance = ABC142A(_input)
    instance.process()
    for i in range(len(expected)):
        assert float(instance.msg[i]) == pytest.approx(expected[i], 1e-6)
