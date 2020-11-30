class ExceptionHandler:
    def __init__(self, local_count_exception):
        self.tree_exception = dict()
        self.count_exception = local_count_exception

    def create(self, children_name_exception):
        self.tree_exception[children_name_exception] = set()

    def put_exception(self, children_name_exception, parent_name_exception = []):
        self.tree_exception[children_name_exception].update(parent_name_exception)

    def find_parents(self, exception_name, ls_parents_exception = set()):
        local_parents_exception = self.tree_exception[exception_name]
        if len(local_parents_exception) > 0:
            ls_parents_exception = ls_parents_exception.union(local_parents_exception)
            for parent_exception in local_parents_exception:
                ls_parents_exception = self.find_parents(parent_exception).union(ls_parents_exception)
        return ls_parents_exception

    def find_relation(self, exception_names):
        second_box_exception = set()
        ls_answers = []
        second_box_exception.add(exception_names[0])
        for exception_name in exception_names[1:]:
            if (len(set(second_box_exception) & set(self.tree_exception[exception_name])) > 0) or \
                    len(set(second_box_exception) & set([exception_name])) > 0:
                if exception_name not in ls_answers:
                    ls_answers.append(exception_name)
            elif len(set(second_box_exception) & self.find_parents(exception_name)) > 0:
                if exception_name not in ls_answers:
                    ls_answers.append(exception_name)

            second_box_exception.add(exception_name)
        return ls_answers

    def printing_exception_failed(self, ls_exceptions_failed):
        for exception_failed in ls_exceptions_failed:
            print(exception_failed)

    def key_board_input_exceptions(self):
        for _ in range(self.count_exception):
            cmd_add_exception = input()
            if ':' in cmd_add_exception:
                children_name_exception, parent_name_exception = cmd_add_exception.split(':')
                children_name_exception = children_name_exception.rstrip()
                parent_name_exception = (parent_name_exception.lstrip()).split()
                self.create(children_name_exception)
                self.put_exception(children_name_exception, parent_name_exception)
            else:
                self.create(cmd_add_exception)

    def key_board_input_requests(self):
        count_request = int(input())
        exception_name = []
        ls_result = []

        for _ in range(count_request):
            exception_name.append(input())
        ls_result = self.find_relation(exception_name)
        self.printing_exception_failed(ls_result)


count_exception = int(input())
obj_tree_exception = ExceptionHandler(count_exception)

obj_tree_exception.key_board_input_exceptions()
obj_tree_exception.key_board_input_requests()
