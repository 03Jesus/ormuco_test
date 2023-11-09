# Question B
"""
write a software library that accepts 2 version string as input and
returns whether one is greater than, equal, or less than the other.
As an example: “1.2” is greater than “1.1”.
"""


def compare_versions(version1, version2):
    v1_s = version1.split(".")
    v2_s = version2.split(".")

    for v1, v2 in zip(v1_s, v2_s):
        if int(v1) > int(v2):
            return 1
        elif int(v1) < int(v2):
            return -1

    if len(v1_s) > len(v2_s):
        return 1
    elif len(v1_s) < len(v2_s):
        return -1

    return 0
