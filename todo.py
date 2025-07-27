class Todo:

    NOT_DONE_CHAR = ' '
    DONE_CHAR = 'X'
    __slots__ = ('_title', '_done')
    
    def __init__(self, title, done=False):
        self._title = title
        self._done = done
    
    @property
    def title(self):
        return self._title
    @property
    def done(self):
        return self._done
    
    @done.setter
    def done(self, did_complete):
        self._done = did_complete
    
    def __str__(self):
        return f"[{self.DONE_CHAR if self.done else self.NOT_DONE_CHAR}] {self.title}"
    def __repr__(self):
        return f"Todo({self.title}, {self.done})"
    
    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        return (self.title == other.title and self.done == other.done)
    
