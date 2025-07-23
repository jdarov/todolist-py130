import unittest
from to_do_list import Todo, TodoList

class TestTodoList(unittest.TestCase):

    def setUp(self):
        self.todo1 = Todo("Buy Milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Todays Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_length(self):
        self.assertEqual(3, len(self.todos))

    def test_to_list(self):
        self.assertEqual([self.todo1, self.todo2, self.todo3], self.todos._todos)

    def test_first(self):
        self.assertEqual(self.todo1, self.todos.first())

    def test_last(self):
        self.assertEqual(self.todo3, self.todos.last())

    def test_all_done(self):
        self.todos.mark_all_done()
        self.assertTrue(self.todos.all_done())
    
    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add(1)
    
    def test_todo_at(self):
        self.assertEqual(self.todo2, self.todos.todo_at(1))
        with self.assertRaises(IndexError):
            self.todos.todo_at(4)

    def test_mark_done_at(self):
        self.todos.mark_done_at(1)

        self.assertTrue(self.todo2)

        with self.assertRaises(IndexError):
            self.todos.mark_done_at(5)
    
    def test_mark_undone_at(self):
        self.todos.mark_undone_at(0)
        self.todos.mark_undone_at(1)
        self.todos.mark_undone_at(2)

        self.assertFalse(self.todo2.done)

        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(5)
    
    def test_mark_all_done(self):
        self.todos.mark_all_done()
        self.assertTrue(self.todos.all_done())

    def test_remove_at(self):
        self.test_todos = self.todos

        self.test_todos.remove_at(0)
        self.test_todos.remove_at(0)
        self.test_todos.remove_at(0)
        self.assertFalse(self.test_todos._todos)

    def test_str(self):
        expected_string = (
            f"---- Todays Todos ----\n"
            f"{self.todo1}\n"
            f"{self.todo2}\n"
            f"{self.todo3}"
        )

        self.assertEqual(expected_string, str(self.todos))
    def test_str_done_todo(self):
        self.todos.mark_all_done()
        expected_string = (
            f"[X] Buy Milk"
        )
        self.assertEqual(expected_string, str(self.todo1))

    def test_str_all_done_todos(self):
        self.todos.mark_all_done()
        expected_string = (
            f"---- Todays Todos ----\n"
            f"[X] Buy Milk\n"
            f"[X] Clean room\n"
            f"[X] Go to the gym"
        )
        self.assertEqual(expected_string, str(self.todos))

    def test_each(self):

        self.todos.each(lambda todo: setattr(todo, 'done', True))
        self.assertTrue(self.todos.all_done())
    
    def test_select(self):
        
if __name__ == '__main__':
    unittest.main()