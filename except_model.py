class ExceptionHandler:
    def __init__(self, local_count_exception):
        self.tree_exception = dict()
        self.count_exception = local_count_exception
        self.second_box_exception = []

    def create(self, children_name_exception):
        self.tree_exception[children_name_exception] = set()

    def put_exception(self, children_name_exception, parent_name_exception=[]):
        self.tree_exception[children_name_exception].update(str(parent_name_exception))

    def find_relation(self, exception_names):
        self.second_box_exception.append(exception_names[0])
        exceptions_failed = []
        for exception_children_name in exception_names[1:]:
            for element_second_box_exception in self.second_box_exception:
                if element_second_box_exception in self.tree_exception[exception_children_name]:
                    exceptions_failed.append(exception_children_name)
            self.second_box_exception.append(exception_children_name)
        for exception_failed in exceptions_failed:
            print(exception_failed)

    def key_board_input_exceptions(self):
        for _ in range(self.count_exception):
            cmd_add_exception = input()
            if ':' in cmd_add_exception:
                children_name_exception, parent_name_exception = cmd_add_exception.split(':')
                children_name_exception = children_name_exception.rstrip()
                parent_name_exception = parent_name_exception.lstrip()
                self.create(children_name_exception)
                self.put_exception(children_name_exception, parent_name_exception)
            else:
                self.create(cmd_add_exception)

    def key_board_input_requests(self):
        count_request = int(input())
        exception_name = []
        for _ in range(count_request):
            exception_name.append(input())
        self.find_relation(exception_name)


count_exception = int(input())
obj_tree_exception = ExceptionHandler(count_exception)

obj_tree_exception.key_board_input_exceptions()
obj_tree_exception.key_board_input_requests()