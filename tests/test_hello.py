import hello


def test_says_world():
    print('Omerta says helloo')
    assert hello.say_what() == 'world'
