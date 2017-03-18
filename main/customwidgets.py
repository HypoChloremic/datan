from pygubu import BuilderObject, register_widget
from main.googlefinance import matplot


class builder(BuilderObject):
    class_ = matplot


register_widget('customwidgets.matplot', builder,
                'matplot', ('ttk', 'main'))