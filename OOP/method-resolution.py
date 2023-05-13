class A:
    def do_something(self):
        print("Method defined in: A")


class B(A):
    def do_something(self):
        print("Method defined in: B")
        super().do_something()


class C(A):
    def do_something(self):
        print("Method defined in: C")


class D(B, C):
    # def do_something(self):
    #     print("Method defined in: D")
    pass


thing = D()
# print(D.__mro__)
# print(D.mro())
# print(help(B))
"""
Method resolution order:
 |      D
 |      B
 |      C
 |      A
 |      builtins.object
 ===> super() will return follow this order

"""
thing.do_something()
