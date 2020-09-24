#файловое чтение
# class TreeClass:
#     def __init__(self, arg1):
#         self.tree_classes = dict()
#         self.count_classes = arg1
#         self.answer = ''
#
#     def create(self, children_name):
#         self.tree_classes['children ' + children_name] = set()
#
#     def put_class(self, children_name_class, ls_parents_class=[]):
#         self.tree_classes['children ' + children_name_class].update(ls_parents_class)
#         # for pr_name_class in ls_parents_class:
#         #     keys_tree_classes = self.tree_classes.keys()
#         #
#         #     for key_tree_class in keys_tree_classes:
#         #         if pr_name_class in key_tree_class:
#         #             self.tree_classes['children ' + children_name_class].update(ls_parents_class)
#         #             break
#                 # if pr_name_class not in key_tree_class: #find key_class
#                 #     self.create(pr_name_class)
#                 # elif pr_name_class in key_tree_class:
#                 #     self.tree_classes['parent ' + pr_name_class].update(children_name_class)
#
#     # def put_class(self, str_attrs):
#     #     if len(str_attrs) != 1:
#     #         children_name_class, _, *parent_class_names = str_attrs.split()
#     #         self.create(children_name_class)
#     #         for parent_name_class in parent_class_names:
#     #             self.create(parent_name_class)
#     #             # keys_tree_classes = self.tree_classes.keys()
#     #             # for key_tree_class in keys_tree_classes:
#     #             #     if parent_name_class in key_tree_class:
#     #             #         self.tree_classes['parent ' + parent_name_class].update(children_name_class)
#     #     else:
#     #         self.create(str_attrs)
#
#     # def get_information(self, parent_class_name, children_class_name):
#     #     if parent_class_name == children_class_name:
#     #         return "No"
#     #     for key_tree_classes, value_tree_classes in self.tree_classes.items():
#     #         if children_class_name in key_tree_classes:
#     #             if parent_class_name not in key_tree_classes and self.tree_classes[key_tree_classes].issuperset(parent_class_name):
#     #                 return "Yes"
#     #             else:
#     #                 count_parents = 0
#     #                 flag = False
#     #                 for grand_parent in value_tree_classes:
#     #                     if not self.tree_classes['children ' + grand_parent]:
#     #                         count_parents += 1
#     #                         continue
#     #                     if count_parents == len(self.tree_classes[children_class_name]):
#     #                         flag = True
#     #                         break
#     #                     else:
#     #                         count_parents += 1
#     #                         self.get_information(parent_class_name, grand_parent)
#     #                         if self.get_information(parent_class_name, grand_parent) None:
#     #
#     #                         return self.get_information(parent_class_name, grand_parent)
#     #     return "No"
#
#     def get_information(self, parent_class_name, children_class_name):
#         self.answer = 'No'
#         if not (parent_class_name == children_class_name):
#             self.find_realation(parent_class_name, children_class_name)
#         return self.answer
#
#     def find_realation(self, parent_class_name, children_class_name):
#         try:
#             ls_parents = self.tree_classes['children ' + children_class_name]
#             if parent_class_name in ls_parents:
#                 self.answer = 'Yes'
#                 return
#             for parent in ls_parents:
#                 self.find_realation(parent_class_name, parent)
#                 if self.answer == 'Yes':
#                     return
#         except KeyError:
#             return
#
# f = open("cmds.txt", "r")
#
# count_class = int(f.readline())
# obj_tree_class = TreeClass(count_class)
# for _ in range(count_class):
#     cmd_add_class = f.readline()
#     if len(cmd_add_class) > 3:
#         cmd_add_class = cmd_add_class.split(':')
#         children_name = cmd_add_class[0][0]
#         parents_name = cmd_add_class[1].split()
#         obj_tree_class.create(children_name)
#         obj_tree_class.put_class(children_name, parents_name)
#     else:
#         obj_tree_class.create(cmd_add_class.rstrip('\n'))
#
# count_request = int(f.readline())
# for _ in range(count_request):
#     parent_class_name, children_class_name = (f.readline()).split(
#     print(obj_tree_class.get_information(parent_class_name, children_class_name))
# f.close()

class TreeClass :
    def __init__ ( self , arg_count_classes ) :
        self.tree_classes = dict()
        self.count_classes = arg_count_classes
        self.answer = ''

    def create ( self , children_name ) :
        self.tree_classes['children ' + children_name] = set ( ) #добавляем новый класс с пустым списком родителей

    def put_class ( self , children_name_class , ls_parents_class=[] ) :
        self.tree_classes['children ' + children_name_class].update ( ls_parents_class ) #добавляем новый класс с списком родителей ls_parents_class 

    def get_information ( self , parent_class_name , children_class_name ) :
        self.answer = 'No' #изначально предполагаются что классы передаваемые через атрибуты функции не связаны
        self.find_realation ( parent_class_name , children_class_name ) #функция поиска связи между классами
        return self.answer #возвращаем ответ

    def find_realation ( self , parent_class_name , children_class_name ) :
        #готовимся поймать исключение
        try :
            ls_parents = self.tree_classes['children ' + children_class_name] #вытаскиваем значение(список родителей) по ключу (имени дочернего класса)
            if parent_class_name == children_class_name or parent_class_name in ls_parents : #первое условие для случая A A, второе если в списке родителей есть наш родитель
                self.answer = 'Yes' #меняем на да, теперь выходим из рекурсии
                return
            for parent in ls_parents : #проходим по каждому из родителей
                self.find_realation ( parent_class_name , parent ) #начинается рекурсия
                if self.answer == 'Yes' : # если в списке родителей нашли родителя то выходим из рекурсии
                    return
        except :
            return


count_class = int ( input ( ) )
obj_tree_class = TreeClass ( count_class )
for _ in range ( count_class ) :
    cmd_add_class = input ( )
    if len ( cmd_add_class ) > 3 :
        #на случай обработки строки вида A(children) : B C D S R G(parents)
        #ещё примеры
        #G : A
        #A : A
        #G : A C V
        #G : A Q R T B C
        #T : F F
        #G : A Q
        #G : A
        #G : A
        cmd_add_class = cmd_add_class.split ( ':' ) #режим строку по :
        children_name = cmd_add_class[0][0] # берём имя ребёнка
        parents_name = cmd_add_class[1].split ( ) # берём имена родителей
        obj_tree_class.create ( children_name ) #создаём вершину с именем ребёнка
        obj_tree_class.put_class ( children_name , parents_name ) #добавляем в словарь ключ значение
    else :
        #на случай обработки строки вида A
        #ещё примеры
        #E
        #D
        #I
        #O
        #P
        #L
        obj_tree_class.create ( cmd_add_class.rstrip ( '\n' ) ) #создаём вершину с пустым список значений

count_request = int ( input ( ) ) #количетсво запросов
for _ in range ( count_request ) :
    parent_class_name , children_class_name = input ( ).split ( )#делим строку находим родителя и ребёнка
    print ( obj_tree_class.get_information ( parent_class_name , children_class_name ) ) #ищем инфомрацию об отношении между parent_class_name и children_class_name, печатаем ответ
