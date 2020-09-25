class TreeClass:
    def __init__(self, arg1):
        self.tree_classes = dict()
        self.count_classes = arg1
        self.answer = ''

    def create(self, children_name_class):
        self.tree_classes[children_name_class] = set()

    def put_class(self, children_name_class, ls_parents_class = []):
        self.tree_classes[children_name_class].update(ls_parents_class)

    def get_information(self, parent_class_name, children_class_name):
        self.answer = 'No'
        self.find_realation(parent_class_name, children_class_name)
        return self.answer

    def find_realation(self, parent_class_name, children_class_name):
        try:
            ls_parents = self.tree_classes[children_class_name]
            if parent_class_name == children_class_name or parent_class_name in ls_parents:
                self.answer = 'Yes'
                return
            for parent in ls_parents:
                self.find_realation(parent_class_name, parent)
                if self.answer == 'Yes':
                    return
        except:
            return

    def key_board_input_classes(self):
        for _ in range(count_class):
            cmd_add_class = input()
            if ':' in cmd_add_class:
                children_name_class, string_parents_name = cmd_add_class.split(':')
                children_name_class = children_name_class.rstrip()
                ls_parents_name = (string_parents_name.rstrip()).split()
                obj_tree_class.create(children_name_class)
                obj_tree_class.put_class(children_name_class, ls_parents_name)
            else:
                obj_tree_class.create(cmd_add_class)

    def key_board_input_requests(self):
        count_request = int(input())
        for _ in range(count_request):
            parent_class_name, children_class_name = input().split()
            print(self.get_information(parent_class_name, children_class_name))


count_class = int(input())
obj_tree_class = TreeClass(count_class)

obj_tree_class.key_board_input_classes()
obj_tree_class.key_board_input_requests()
