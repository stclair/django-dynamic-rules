
from dynamic_rules.sites import site

__all__ = ('site',)

VERSION = "0.1.3"

def autodiscover():
    from autoload import autodiscover as discover
    discover("dynamic_actions")