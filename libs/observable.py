class Observable(object):
    def __init__(self, on_val_change=None):
        self._val, self._onv_val_change = '', on_val_change

    @property
    def message(self):
        return self._val

    @message.setter
    def message(self, value):
        if self._onv_val_change:
            self._onv_val_change(self._val, value)
        self._val = value