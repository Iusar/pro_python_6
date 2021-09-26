import unittest
import code_for_testing as cft


class TestSomething(unittest.TestCase):

    def setup(self):
        print("method setup")

    def teardown(self):
        print("method teardown")

    # Поиск имени человека по номеру документа
    def test_find_client_name(self):
        self.func_result = cft.find_client_name(cft.documents, '11-2')
        self.assertEqual('Геннадий Покемонов', self.func_result)

    # Поиск номера полки по номеру документа
    def test_find_shelf_no(self):
        self.func_result = cft.find_shelf_no(cft.directories, '11-2')
        self.assertEqual(self.func_result, '1')

    # Вывести список всех документов
    @unittest.skip("demonstrating skipping")
    def test_print_all_docs(self):
        self.assertListEqual(cft.print_all_docs(cft.documents),
                             [{'name': 'Василий Гупкин', 'number': '2207 876234', 'type': 'passport'},
                              {'name': 'Геннадий Покемонов', 'number': '11-2', 'type': 'invoice'},
                              {'name': 'Аристарх Павлов', 'number': '10006', 'type': 'insurance'}])

    # Добавить новый документ в каталог
    def test_add_new_doc(self):
        new_documents = cft.add_new_doc(cft.documents, cft.directories, 'passport', '5546 8848', 'Василий Пупкин', '3')[
            1].get('3')
        # [1] - второй результат ретёрна функции add_new_doc, .get('3') - третья полка[0]
        self.assertListEqual(new_documents, cft.directories.get('3'))

    # Проверка удаления по номеру документа 'name': 'Аристарх Павлов', 'number': '10006'
    def test_delete_doc(self):
        # Результат фунции delete_doc - documents
        self.new_docs = cft.delete_doc(cft.documents, cft.directories, '10006')[0]
        # Результат фунции delete_doc - directories
        self.new_dirs = cft.delete_doc(cft.documents, cft.directories, '10006')[1]
        # Ищем результат в документах - documents
        for line in self.new_docs:
            self.assertNotEqual('Аристарх Павлов', line.get('name'), 'empty')
        # Ищем результат в директориях - documents
        for line in self.new_dirs.values():
            self.assertNotIn('10006', line, 'founded')


if __name__ == '__main__':
    TestSomething.test_find_client_name()
    TestSomething.test_delete_doc()
