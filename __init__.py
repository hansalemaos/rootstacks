import os
import re
import stat

from reggisearch import search_values


def set_read_write(path):
    os.chmod(path, stat.S_IWRITE)


def set_read_only(path):
    os.chmod(path, stat.S_IREAD)


def root_bluestacks(make_read_only=False):
    di = search_values(
        mainkeys=r"HKEY_LOCAL_MACHINE\SOFTWARE\BlueStacks_nxt", subkeys="UserDefinedDir"
    )
    bstconfigpath = di[r"HKEY_LOCAL_MACHINE\SOFTWARE\BlueStacks_nxt"]["UserDefinedDir"]
    bstconfigpath = os.path.normpath(os.path.join(bstconfigpath, "bluestacks.conf"))
    with open(bstconfigpath, mode="rb") as f:
        data = f.read()

    datanew = re.sub(rb'(root[^\n\r"\']+=")\d+("\s*[\r\n])', rb"\g<1>1\g<2>", data)
    set_read_write(path=bstconfigpath)
    with open(bstconfigpath, mode="wb") as f:
        f.write(datanew)
    if make_read_only:
        set_read_only(bstconfigpath)



