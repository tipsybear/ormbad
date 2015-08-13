# ormbad.version
# Helper module for ORMBad version information
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Thu Aug 13 12:38:42 2015 -0400
#
# Copyright (C) 2015 Tipsy Bear Studios
# For license information, see LICENSE.txt
#
# ID: version.py [] benjamin@bengfort.com $

"""
Helper module for ORMBad version information.
"""

##########################################################################
## Versioning
##########################################################################

__version_info__ = {
    'major': 0,
    'minor': 1,
    'micro': 0,
    'releaselevel': 'final',
    'serial': 0,
}


def get_version(short=False):
    """
    Returns the version from the version info.
    """
    assert __version_info__['releaselevel'] in ('alpha', 'beta', 'final')
    vers = ["%(major)i.%(minor)i" % __version_info__, ]
    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final' and not short:
        vers.append('%s%i' % (__version_info__['releaselevel'][0],
                              __version_info__['serial']))
    return ''.join(vers)
