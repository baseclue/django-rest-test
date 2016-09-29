import unittest


class DecoratorsTestCase(unittest.TestCase):
    def test_anonymous_decorator(self):

        from rest_tests import RestTests

        @RestTests.anonymous_user.can_create
        class DecoratedTests(RestTests):
            pass

        self.assertEqual(DecoratedTests.anonymous_user.allowed_operations, {'create'})

    def test_multiple_anonymous_decorators(self):

        from rest_tests import RestTests

        @RestTests.anonymous_user.can_create
        @RestTests.anonymous_user.can_retrieve
        class DecoratedTests(RestTests):
            pass

        self.assertEqual(DecoratedTests.anonymous_user.allowed_operations, {'create', 'retrieve'})

    def test_same_class_decorator(self):

        from rest_tests import RestTests, RestUser

        class DecoratedTests(RestTests):
            logged_user = RestUser

        DecoratedTests = DecoratedTests.logged_user.can_create(DecoratedTests)

        self.assertEqual(DecoratedTests.logged_user.allowed_operations, {'create'})

    def test_same_class_user(self):

        from rest_tests import RestTests, RestUser

        class DecoratedTests(RestTests):
            logged_user = RestUser(can_create=True)

        self.assertEqual(DecoratedTests.logged_user.allowed_operations, {'create'})

    def test_decorated_all_users(self):
        from rest_tests import RestTests, RestUser

        class MyTests(RestTests):
            logged_user = RestUser

        @RestTests.all_users.can_create
        class DecoratedTests(MyTests):
            pass

        self.assertEqual(DecoratedTests.anonymous_user.allowed_operations, {'create'})
        self.assertEqual(DecoratedTests.logged_user.allowed_operations, {'create'})

    def test_inheritance_decorator(self):
        from rest_tests import RestTests

        class MyTests(RestTests):
            pass

        @MyTests.anonymous_user.can_create
        class DecoratedTests(RestTests):
            pass

        self.assertEqual(MyTests.anonymous_user.allowed_operations, set())
        self.assertEqual(DecoratedTests.anonymous_user.allowed_operations, {'create'})

    def test_strange_inheritance_decorator(self):
        from rest_tests import RestTests

        class MyTests(RestTests):
            pass

        @RestTests.anonymous_user.can_create
        class DecoratedTests(MyTests):
            pass

        self.assertEqual(MyTests.anonymous_user.allowed_operations, set())
        self.assertEqual(DecoratedTests.anonymous_user.allowed_operations, {'create'})


if __name__ == '__main__':
    unittest.main()
