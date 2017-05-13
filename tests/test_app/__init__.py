from pyramid.config import Configurator


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('cornice')
    config.include('tests.test_app.app')
    return config.make_wsgi_app()


if __name__ == '__main__':
    main({})
