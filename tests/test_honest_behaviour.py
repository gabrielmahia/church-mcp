from church_mcp import server

_fn = lambda name: (getattr(server, name).fn if hasattr(getattr(server, name), "fn") else getattr(server, name))


def test_the_catholic_share_is_not_stated_as_a_third():
    text = str(_fn("catholic_diocese_finder")(None)) + str(_fn("protestant_denomination_guide")())
    assert "~33% of Kenyans are Catholic" not in text and "~47%" not in text
    assert "fifth" in str(_fn("catholic_diocese_finder")(None))
