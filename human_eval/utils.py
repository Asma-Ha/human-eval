def check_transformed(check, entry_point) :
    import inspect
    failures = []

    #source_lines = inspect.getsource(check).splitlines()
    source_lines = check.splitlines()
    assert_lines = [line.strip() for line in source_lines if 'assert' in line]
    for assert_line in assert_lines :
        try :
            #assert_line_exec = assert_line.replace("candidate", entry_point)
            exec(assert_line, {"candidate": entry_point})
            #exec(assert_line_exec)
        except AssertionError :
            assert_data = assert_line.replace(" ", "").split("candidate")[1]
            failures.append(assert_data)
    print(failures)
    return failures