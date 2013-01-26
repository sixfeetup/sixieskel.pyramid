from .api import TemplateAPI

def register_api(event):
    """Registers an 'api' variable for all templates.

    This function is called by Pyramid at configuration
    time. This will register the api variable so that
    individual views don't have to worry.
    """
    event['api'] = TemplateAPI()
