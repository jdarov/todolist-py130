from todo import Todo

class TodoList:

    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title
    
    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError("todo must be of the type Todo class")
        self._todos.append(todo)

        return self
    
    def first(self):
        if self._todos:
            return self._todos[0]
        raise IndexError("TodoList is empty")
    
    def last(self):
        if self._todos:
            return self._todos[-1]
        raise IndexError("TodList is empty")
    
    def todo_at(self, index):
        return self._todos[index]
    
    def mark_done_at(self, index):
        self._todos[index].done = True
        return self
    
    def mark_undone_at(self, index):
        self._todos[index].done = False
        return self
    
    def mark_all_done(self):
        self.each(lambda todo: setattr(todo, 'done', True))
    def mark_all_undone(self):
        self.each(lambda todo: setattr(todo, 'done', False))

    def all_done(self):
        return all(todo.done for todo in self._todos)
    
    def remove_at(self, index):
        del self._todos[index]

    
    def to_list(self):
        return self._todos.copy()
    
    def each(self, callback):
        for todo in self._todos:
            callback(todo)

    def select(self, callback):
        new_list = TodoList(self.title)

        for todo in filter(callback, self._todos):
            new_list.add(todo)
        return new_list
    
    def find_by_title(self, title):
        return [todo for todo in self._todos if todo.title == title][0]
    
    def done_todos(self):
        return self.select(lambda todo: todo.done)
    def undone_todos(self):
        return self.select(lambda todo: not todo.done)
    
    def mark_done(self, title):
        self.find_by_title(title).done = True
    
    def __str__(self):
        return (
            f"---- {self.title} ----\n" + 
            '\n'.join(str(todo) for todo in self._todos)
                )
    
    def __len__(self):
        return len(self._todos)
    
