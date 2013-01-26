from pyramid.threadlocal import get_current_registry


class TemplateAPI(object):
    def __init__(self):
        pass

    @property
    def settings(self):
        """Returns the current thread's settings dictionary."""
        return get_current_registry().settings
