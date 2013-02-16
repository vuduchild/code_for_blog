import unittest
from mock import patch
from multi_platform.mac_funcs import is_mac_kernel_ver_good

FAKE_MAC_OS_UNAME_KERNEL_10_3_0 = ('Darwin', 'phantom', '10.3.0',
                                   'Darwin Kernel Version 10.3.0: Sat Aug 25 00:48:52 PDT 2012;' +
                                   'root:xnu-2050.18.24~1/RELEASE_X86_64', 'x86_64')
FAKE_MAC_OS_UNAME_KERNEL_11_0_0 = ('Darwin', 'phantom', '11.0.0',
                                   'Darwin Kernel Version 11.0.0: Sat Aug 25 00:48:52 PDT 2012;' +
                                   'root:xnu-2050.18.24~1/RELEASE_X86_64', 'x86_64')
FAKE_MAC_OS_UNAME_KERNEL_12_2_0 = ('Darwin', 'phantom', '12.2.0',
                                   'Darwin Kernel Version 12.2.0: Sat Aug 25 00:48:52 PDT 2012;' +
                                   'root:xnu-2050.18.24~1/RELEASE_X86_64', 'x86_64')

class TestMacKernelVersion(unittest.TestCase):
#pylint: disable=R0904

    @patch('multi_platform.mac_funcs.get_os_uname')
    def test_is_mac_kernel_ver_good_returns_false_when_ver_lower_than_min(self, os_uname_mock):
        os_uname_mock.return_value = FAKE_MAC_OS_UNAME_KERNEL_10_3_0
        self.assertFalse(is_mac_kernel_ver_good())

    @patch('multi_platform.mac_funcs.get_os_uname')
    def test_is_mac_kernel_ver_good_returns_true_when_ver_equals_min(self, os_uname_mock):
        os_uname_mock.return_value = FAKE_MAC_OS_UNAME_KERNEL_11_0_0
        self.assertTrue(is_mac_kernel_ver_good())

    @patch('multi_platform.mac_funcs.get_os_uname')
    def test_is_mac_kernel_ver_good_returns_true_when_ver_above_min(self, os_uname_mock):
        os_uname_mock.return_value = FAKE_MAC_OS_UNAME_KERNEL_12_2_0
        self.assertTrue(is_mac_kernel_ver_good())