class KeyboardAction:
    def __init__(self, action):
        self._action = action

    def send_keys(self, text):
        self._action.key_action.send_keys(text)
        self._action.perform()

    def shortcut(self, keys):
        for key in keys:
            self._action.key_action.key_down(key)
        for key in keys:
            self._action.key_action.key_up(key)
        self._action.perform()

