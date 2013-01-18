from templer.core.base import BaseTemplate
from templer.core.vars import EASY, EXPERT, StringVar, BooleanVar

basic_vars = [
        StringVar(
            'version',
            'Version',
            default='0.1',
            modes=(EASY, EXPERT)
        ),
        StringVar(
            'package_name',
            'Enter the package name',
            modes=(EASY, EXPERT)
        ),
        StringVar(
            'description',
            'Enter the package description',
            modes=(EXPERT,)
        ),
        StringVar(
            'author',
            'Author(s)',
            default='Six Feet Up, Inc.',
            modes=(EASY, EXPERT)
        ),
        StringVar(
            'author_email',
            'Author emails',
            default='info@sixfeetup.com',
            modes=(EASY, EXPERT)
        ),
        StringVar(
            'url',
            'URL',
            default='http://www.sixfeetup.com',
            modes=(EASY, EXPERT)
        ),
        StringVar(
            'keywords',
            'Keywords',
            default='web pyramid',
            modes=(EXPERT,)
        ),
        BooleanVar(
            'include_debug_bar',
            'Include Pyramid Debug Bar?',
            default=False,
            modes=(EASY, EXPERT)
        ),
        StringVar(
            'extends_package',
            'Extend existing package',
            default='',
            modes=(EASY, EXPERT)
        ),
    ]


class SixieBasePyramid(BaseTemplate):
    _template_dir = "templates/base"
    summary = "Sixie default base Pyramid package"
    help = "A basic, no-frills Pyramid package."
    category = "Six Feet Up"
    vars = basic_vars
    use_cheetah = True


class SixieAlchemyPyramid(BaseTemplate):
    _template_dir = "templates/alchemy"
    summary = "Sixie Pyramid/SQLAlchemy package"
    help = "A Pyramid package including SQLAlchemy scaffolding."
    category = "Six Feet Up"
    vars = basic_vars
    use_cheetah = True


class SixieZodbPyramid(BaseTemplate):
    _template_dir = "templates/zodb"
    summary = "Sixie Pyramid/ZODB package"
    help = "A Pyramid package including ZODB scaffolding."
    category = "Six Feet Up"
    vars = basic_vars
    use_cheetah = True
