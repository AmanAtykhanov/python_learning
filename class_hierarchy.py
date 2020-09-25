class TreeClass:
    def __init__(self, count_classes):
        self.tree_classes = dict()
        self.count_classes = count_classes

    def create(self, children_name_class):
        self.tree_classes[children_name_class] = set()

    def put_class(self, children_name_class, ls_parents_class = []):
        self.tree_classes[children_name_class].update(ls_parents_class)

    def find_relation(self, parent_class_name, children_class_name):
        ls_parents = self.tree_classes[children_class_name]
        if parent_class_name == children_class_name or parent_class_name in ls_parents:
            return 'Yes'
        for parent in ls_parents:
            if self.find_relation(parent_class_name, parent) == 'Yes':
                return 'Yes'
        return 'No'


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
            print(self.find_relation(parent_class_name, children_class_name))
            

count_class = int(input())
obj_tree_class = TreeClass(count_class)

obj_tree_class.key_board_input_classes()
obj_tree_class.key_board_input_requests()
