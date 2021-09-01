
def tab_str(some_str, tab_count):
    return "\t" * tab_count + some_str.replace("\n", "\n" + "\t" * tab_count)
