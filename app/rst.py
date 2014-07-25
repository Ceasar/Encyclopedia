import os
import os.path


def iteritems(filename):
    with open(filename) as f:
        for line in f:
            reference_name, hyperlink_target = line.split(":")
            # strip the leading ".. _" from the reference_name
            reference_name = reference_name[4:]
            yield reference_name, hyperlink_target.strip()


def get_hyperlink_target(index, reference_name):
    hyperlink_target = index[reference_name]
    if hyperlink_target.endswith("_"):
        while hyperlink_target.endswith("_"):
            reference_name = hyperlink_target[:-1].replace("`", "")
            hyperlink_target = index[reference_name]
        return os.path.splitext(hyperlink_target)[0]
    else:
        return hyperlink_target
