from core.Controller import Controller
from core.Core import Core

"""
    Main controller. It will be responsible for program's main screen behavior.
"""


class HomeController(Controller):
    # -----------------------------------------------------------------------
    #        Constructor
    # -----------------------------------------------------------------------
    def __init__(self):
        self.homeView = self.loadView("Home")

    # -----------------------------------------------------------------------
    #        Methods
    # -----------------------------------------------------------------------
    """
        Opens controller according to the option chosen
    """

    def btnClicked(self, caption):
        if caption == "Open Products DB":
            c = Core.openController("show")
            c.main()
        elif caption == "Add products":
            c = Core.openController("add")
            c.main()

    """
        @Override
    """

    def main(self):
        self.homeView.main()