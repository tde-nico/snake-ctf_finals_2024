 17           RESUME                   0

 18           LOAD_CONST               1 (0)
              LOAD_CONST               0 (None)
              IMPORT_NAME              0 (hashlib)
              STORE_FAST               2 (hashlib)

 19           LOAD_FAST                0 (self)
              LOAD_ATTR                2 (agent)
              LOAD_GLOBAL              4 (bytes)
              LOAD_ATTR                7 (fromhex + NULL|self)
              LOAD_CONST               2 ('eb000b')
              CALL                     1
              BINARY_OP                0 (+)
              LOAD_FAST                1 (nonce)
              BINARY_OP                0 (+)
              LOAD_FAST                0 (self)
              STORE_ATTR               4 (magic)

 20           LOAD_GLOBAL             10 (int)
              LOAD_ATTR               13 (from_bytes + NULL|self)
              LOAD_FAST                2 (hashlib)
              LOAD_ATTR               15 (sha256 + NULL|self)
              LOAD_FAST                0 (self)
              LOAD_ATTR                8 (magic)
              CALL                     1
              LOAD_ATTR               17 (digest + NULL|self)
              CALL                     0
              LOAD_CONST               3 ('little')
              CALL                     2
              STORE_FAST               3 (n)

 22           LOAD_FAST                3 (n)
              LOAD_CONST               4 (2)
              LOAD_CONST               5 (160)
              BINARY_OP                8 (**)
              COMPARE_OP               2 (<)
              RETURN_VALUE
