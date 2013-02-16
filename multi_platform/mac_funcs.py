import os

def is_mac_kernel_ver_good():
    min_ker_version = (11, 0, 0)
    kernel_version_str = os.uname()[2]
    kernel_version_tpl = tuple(int(num) for num in kernel_version_str.split('.'))
    if kernel_version_tpl >= min_ker_version:
        return True
    else:
        return False