"""
Utility functions for working with reStructuredText.
"""
import os
import os.path

from docutils import core
from docutils.writers.html4css1 import Writer, HTMLTranslator


def iteritems(filename):
    with open(filename) as f:
        for line in f:
            try:
                reference_name, hyperlink_target = line.split(":")
            except ValueError:
                # the line has multiple ":" in it; probably an external link
                continue
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


def rst_to_html(rst_string, settings=None):
    """Convert a string written in reStructuredText to an HTML string.

    :param rst_string:
        A string that holds the contents of a reStructuredText document.

    :param settings:
        Optional. A dictionary which overrides the default settings.

        For a list of the possible keys and values, see
        http://docutils.sourceforge.net/docs/user/config.html.

        To log the values used, pass in ``'dump_settings': 'yes'``.
    """
    writer = Writer()
    writer.translator_class = HTMLTranslator
    if settings is None:
        settings = {
            # Include a time/datestamp in the document footer.
            'datestamp': '%Y-%m-%d %H:%M UTC',
            # Recognize and link to standalone PEP references (like "PEP 258").
            'pep_references': 1,
            # Do not report any system messages.
            'report_level': 'none',
            # Recognize and link to standalone RFC references (like "RFC 822").
            'rfc_references': 1,
        }
    return core.publish_string(rst_string, writer=writer,
                               settings_overrides=settings)
