class MouseAction:
    def __init__(self, action):
        self._action = action
        self.location = {"x": 0, "y": 0}

    def move_to(self, ms, x, y):
        self._action.pointer_action.source.create_pointer_move(ms, x, y)
        self._action.perform()

    def click(self, element=None):
        self._action.pointer_action.click(element=element)
        self._action.perform()

    def right_click(self, element=None):
        self._action.pointer_action.context_click(element)
        self._action.perform()

    def hold(self, element=None):
        self._action.pointer_action.click_and_hold(element)
        self._action.perform()

    def release(self):
        self._action.pointer_action.release()
        self._action.perform()
