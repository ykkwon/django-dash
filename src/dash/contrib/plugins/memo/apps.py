__title__ = 'dash.contrib.plugins.memo.apps'
__author__ = 'Artur Barseghyan <artur.barseghyan@gmail.com>'
__copyright__ = 'Copyright (c) 2013-2015 Artur Barseghyan'
__license__ = 'GPL 2.0/LGPL 2.1'
__all__ = ('Config',)

try:
    from django.apps import AppConfig

    class Config(AppConfig):
        name = 'dash.contrib.plugins.memo'
        label = 'dash_contrib_plugins_memo'

except ImportError:
    pass
