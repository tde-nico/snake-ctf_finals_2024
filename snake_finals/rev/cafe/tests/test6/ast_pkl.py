Module(
    body=[
        ImportFrom(
            module='dill._dill',
            names=[
                alias(name='_create_type')],
            level=0),
        ImportFrom(
            module='dill._dill',
            names=[
                alias(name='_load_type')],
            level=0),
        Assign(
            targets=[
                Name(id='_var0', ctx=Store())],
            value=Call(
                func=Name(id='_load_type', ctx=Load()),
                args=[
                    Constant(value='type')],
                keywords=[])),
        Assign(
            targets=[
                Name(id='_var1', ctx=Store())],
            value=Call(
                func=Name(id='_load_type', ctx=Load()),
                args=[
                    Constant(value='object')],
                keywords=[])),
        ImportFrom(
            module='dill._dill',
            names=[
                alias(name='_create_function')],
            level=0),
        ImportFrom(
            module='dill._dill',
            names=[
                alias(name='_create_code')],
            level=0),
        Assign(
            targets=[
                Name(id='_var2', ctx=Store())],
            value=Call(
                func=Name(id='_create_code', ctx=Load()),
                args=[
                    Constant(value=b'\x02\x01'),
                    Constant(value=3),
                    Constant(value=0),
                    Constant(value=0),
                    Constant(value=3),
                    Constant(value=3),
                    Constant(value=3),
                    Constant(value=b'\x95\x00U\x02R\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00S\x015\x01\x00\x00\x00\x00\x00\x00U\x00l\x01\x00\x00\x00\x00\x00\x00\x00\x00g\x00'),
                    Tuple(elts=(<ast.Constant object at 0x7f3976e92a70>, <ast.Constant object at 0x7f3976e92ad0>), ctx=Load()),
                    Tuple(elts=(<ast.Constant object at 0x7f3976e92bc0>, <ast.Constant object at 0x7f3976e92c20>), ctx=Load()),
                    Tuple(elts=(<ast.Constant object at 0x7f3976e92d10>, <ast.Constant object at 0x7f3976e92d70>, <ast.Constant object at 0x7f3976e92c20>), ctx=Load()),
                    Constant(value='/app/server.py'),
                    Constant(value='__init__'),
                    Constant(value='EnsuringRichCafè.__init__'),
                    Constant(value=14),
                    Constant(value=b"\x80\x00\xd8\x15\x1a\x97\\\x91\\\xa0'\xd3\x15*\x88\x04\x8d\n"),
                    Constant(value=b''),
                    Tuple(elts=(), ctx=Load()),
                    Tuple(elts=(), ctx=Load())],
                keywords=[])),
        Assign(
            targets=[
                Name(id='_var3', ctx=Store())],
            value=Call(
                func=Name(id='_create_function', ctx=Load()),
                args=[
                    Name(id='_var2', ctx=Load()),
                    Dict(
                        keys=[
                            Constant(value='__name__')],
                        values=[
                            Constant(value='__main__')]),
                    Constant(value='__init__'),
                    Constant(value=None),
                    Constant(value=None)],
                keywords=[])),
        Assign(
            targets=[
                Name(id='_var4', ctx=Store())],
            value=Name(id='_var3', ctx=Load())),
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='_var4', ctx=Load()),
                    attr='__setstate__'),
                args=[
                    Tuple(elts=(<ast.Dict object at 0x7f3976e937f0>, <ast.Dict object at 0x7f3976e93a00>), ctx=Load())],
                keywords=[])),
        Assign(
            targets=[
                Name(id='_var5', ctx=Store())],
            value=Call(
                func=Name(id='_create_code', ctx=Load()),
                args=[
                    Constant(value=b'\x02\x01\x08\x01T\x01z\x02'),
                    Constant(value=2),
                    Constant(value=0),
                    Constant(value=0),
                    Constant(value=4),
                    Constant(value=5),
                    Constant(value=3),
                    Constant(value=b'\x95\x00S\x01S\x00K\x00n\x02U\x00R\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00[\x04\x00\x00\x00\x00\x00\x00\x00\x00R\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00S\x025\x01\x00\x00\x00\x00\x00\x00-\x00\x00\x00U\x01-\x00\x00\x00U\x00l\x04\x00\x00\x00\x00\x00\x00\x00\x00[\n\x00\x00\x00\x00\x00\x00\x00\x00R\r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00U\x02R\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00U\x00R\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x005\x01\x00\x00\x00\x00\x00\x00R\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x005\x00\x00\x00\x00\x00\x00\x00S\x035\x02\x00\x00\x00\x00\x00\x00n\x03U\x03S\x04S\x05-\x08\x00\x00:\x02\x00\x00$\x00'),
                    Tuple(elts=(<ast.Constant object at 0x7f3976ec0220>, <ast.Constant object at 0x7f3976ec0280>, <ast.Constant object at 0x7f3976ec02e0>, <ast.Constant object at 0x7f3976ec0340>, <ast.Constant object at 0x7f3976ec03a0>, <ast.Constant object at 0x7f3976ec0400>), ctx=Load()),
                    Tuple(elts=(<ast.Constant object at 0x7f3976ec0490>, <ast.Constant object at 0x7f3976e92c20>, <ast.Constant object at 0x7f3976ec0550>, <ast.Constant object at 0x7f3976ec05b0>, <ast.Constant object at 0x7f3976ec0610>, <ast.Constant object at 0x7f3976ec0670>, <ast.Constant object at 0x7f3976ec06d0>, <ast.Constant object at 0x7f3976ec0730>, <ast.Constant object at 0x7f3976ec0790>), ctx=Load()),
                    Tuple(elts=(<ast.Constant object at 0x7f3976e92d10>, <ast.Constant object at 0x7f3976ec0880>, <ast.Constant object at 0x7f3976ec0490>, <ast.Constant object at 0x7f3976ec08e0>), ctx=Load()),
                    Constant(value='/app/server.py'),
                    Constant(value='__check__'),
                    Constant(value='EnsuringRichCafè.__check__'),
                    Constant(value=17),
                    Constant(value=b'\x80\x00\xdb\x08\x16\xd8\x15\x19\x97Z\x91Z\xa4%\xa7-\xa1-\xb0\x08\xd3"9\xd1\x159\xb8E\xd1\x15A\x88\x04\x8c\n\xdc\r\x10\x8f^\x89^\x98G\x9fN\x99N\xa84\xaf:\xa9:\xd3\x1c6\xd7\x1c=\xd1\x1c=\xd3\x1c?\xc0\x18\xd3\rJ\x88\x01\xe0\x0f\x10\x901\x98\x03\x918\x89|\xd0\x08\x1b'),
                    Constant(value=b''),
                    Tuple(elts=(), ctx=Load()),
                    Tuple(elts=(), ctx=Load())],
                keywords=[])),
        Assign(
            targets=[
                Name(id='_var6', ctx=Store())],
            value=Call(
                func=Name(id='_create_function', ctx=Load()),
                args=[
                    Name(id='_var5', ctx=Load()),
                    Dict(
                        keys=[
                            Constant(value='__name__')],
                        values=[
                            Constant(value='__main__')]),
                    Constant(value='__check__'),
                    Constant(value=None),
                    Constant(value=None)],
                keywords=[])),
        Assign(
            targets=[
                Name(id='_var7', ctx=Store())],
            value=Name(id='_var6', ctx=Load())),
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='_var7', ctx=Load()),
                    attr='__setstate__'),
                args=[
                    Tuple(elts=(<ast.Dict object at 0x7f3976ec1210>, <ast.Dict object at 0x7f3976ec1360>), ctx=Load())],
                keywords=[])),
        Assign(
            targets=[
                Name(id='_var8', ctx=Store())],
            value=Call(
                func=Name(id='_load_type', ctx=Load()),
                args=[
                    Constant(value='int')],
                keywords=[])),
        Assign(
            targets=[
                Name(id='_var9', ctx=Store())],
            value=Call(
                func=Name(id='_load_type', ctx=Load()),
                args=[
                    Constant(value='bytes')],
                keywords=[])),
        Assign(
            targets=[
                Name(id='_var10', ctx=Store())],
            value=Call(
                func=Name(id='_create_type', ctx=Load()),
                args=[
                    Name(id='_var0', ctx=Load()),
                    Constant(value='EnsuringRichCafè'),
                    Tuple(elts=(<ast.Name object at 0x7f3976e91f00>,), ctx=Load()),
                    Dict(
                        keys=[
                            Constant(value='__module__'),
                            Constant(value='__firstlineno__'),
                            Constant(value='__init__'),
                            Constant(value='__check__'),
                            Constant(value='__static_attributes__'),
                            Constant(value='__doc__'),
                            Constant(value='__slotnames__')],
                        values=[
                            Constant(value='__main__'),
                            Constant(value=13),
                            Name(id='_var4', ctx=Load()),
                            Name(id='_var7', ctx=Load()),
                            Tuple(elts=(<ast.Constant object at 0x7f3976e92c20>, <ast.Constant object at 0x7f3976ec0610>), ctx=Load()),
                            Constant(value=None),
                            List(elts=[], ctx=Load())])],
                keywords=[])),
        Assign(
            targets=[
                Name(id='_var11', ctx=Store())],
            value=Call(
                func=Name(id='setattr', ctx=Load()),
                args=[
                    Name(id='_var10', ctx=Load()),
                    Constant(value='__qualname__'),
                    Constant(value='EnsuringRichCafè')],
                keywords=[])),
        Assign(
            targets=[
                Name(id='_var12', ctx=Store())],
            value=Call(
                func=Name(id='_var10', ctx=Load()),
                args=[],
                keywords=[])),
        Expr(
            value=Call(
                func=Attribute(
                    value=Name(id='_var12', ctx=Load()),
                    attr='__setstate__'),
                args=[
                    Dict(
                        keys=[
                            Constant(value='agent')],
                        values=[
                            Constant(value=b'\xf5\xb2\tI\x8b\xfa\xd6P')])],
                keywords=[])),
        Assign(
            targets=[
                Name(id='result', ctx=Store())],
            value=Name(id='_var12', ctx=Load()))],
    type_ignores=[])