from distutils.version import StrictVersion

import setuptools
import twine
import wheel

if __name__ == '__main__':
    """
    Ensure that all tools are correctly installed. See https://stackoverflow.com/a/26737258
    """
    assert StrictVersion(setuptools.__version__) >= StrictVersion('38.6.0'), 'Please upgrade setuptools. ' \
                                                                             'See https://stackoverflow.com/a/26737258'
    assert StrictVersion(twine.__version__) >= StrictVersion('1.11.0'), 'Please upgrade twine. ' \
                                                                        'See https://stackoverflow.com/a/26737258'
    assert StrictVersion(wheel.__version__) >= StrictVersion('0.31.0'), 'Please upgrade wheel. ' \
                                                                        'See https://stackoverflow.com/a/26737258'
