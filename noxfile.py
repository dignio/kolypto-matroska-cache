import nox.sessions


nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ['tests', 'test_redis']


@nox.session()
def tests(session: nox.sessions.Session, redis=None):
    """ Run all tests """
    session.install('poetry')
    session.run('poetry', 'install')

    # Test
    session.run('pytest', 'tests/', '--cov=matroska_cache')


@nox.session()
@nox.parametrize(
    'redis', [
        '4.0.0', '4.0.1', '4.0.2',
        '4.1.0', '4.1.1', '4.1.2', '4.1.3', '4.1.4',
        '4.2.0', '4.2.1', '4.2.2',
        '4.3.0', '4.3.1', '4.3.2', '4.3.3', '4.3.4', '4.3.5', '4.3.6',
        '4.4.0', '4.4.1', '4.4.2', '4.4.4', '4.4.4',
        '4.5.0', '4.5.1', '4.5.2', '4.5.3', '4.5.4', '4.5.5',
        '4.6.0',
        '5.0.0', '5.0.1', '5.0.2', '5.0.3', '5.0.4', '5.0.5', '5.0.6', '5.0.7', '5.0.8',
        '5.0.0', '5.0.1', '5.0.2', '5.0.3', '5.0.4', '5.0.5', '5.0.6', '5.0.7', '5.0.8',
        '5.1.0', '5.1.1',
    ]
)
def test_redis(session, redis):
    tests(session, redis=redis)
