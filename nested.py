class A:
    def __init__(self) -> None:
        self.var=1
    class B:
        def __init__(self,ref) -> None:
            ref.var=20
    b=B(self)
a=A()
print(a.var)