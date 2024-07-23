import itertools
import os
import sys
import functools
import collections
import re

_uname_cache = None

_ver_output = re.compile(r'(?:([\w ]+) ([\w.]+) '
                         r'.*'
                         r'\[.* ([\d.]+)\])')

_WIN32_SERVER_RELEASES = {
    (5, 2): "2003Server",

    (6, 0): "2008Server",
    (6, 1): "2008ServerR2",
    (6, 2): "2012Server",
    (6, 3): "2012ServerR2",
    (6, None): "post2012ServerR2",
}

_WIN32_CLIENT_RELEASES = {
    (5, 0): "2000",
    (5, 1): "XP",
    (5, 2): "2003Server",
    (5, None): "post2003",

    (6, 0): "Vista",
    (6, 1): "7",
    (6, 2): "8",
    (6, 3): "8.1",
    (6, None): "post8.1",

    (10, 0): "10",
    (10, None): "post10",
}

def system():
    ":/"
    return uname().system

def _unknown_as_blank(val):
    ":/"
    return '' if val == 'unknown' else val

def _node(default=''):
    ":/"
    try:
        import socket
    except ImportError:
        return default
    try:
        return socket.gethostname()
    except OSError:
        return default

def _syscmd_ver(system='', release='', version='',

               supported_platforms=('win32', 'win16', 'dos')):
    ":/"
    if sys.platform not in supported_platforms:
        return system, release, version

    import subprocess
    for cmd in ('ver', 'command /c ver', 'cmd /c ver'):
        try:
            info = subprocess.check_output(cmd,
                                           stdin=subprocess.DEVNULL,
                                           stderr=subprocess.DEVNULL,
                                           text=True,
                                           encoding="locale",
                                           shell=True)
        except (OSError, subprocess.CalledProcessError) as why:
            continue
        else:
            break
    else:
        return system, release, version

    info = info.strip()
    m = _ver_output.match(info)
    if m is not None:
        system, release, version = m.groups()
        if release[-1] == '.':
            release = release[:-1]
        if version[-1] == '.':
            version = version[:-1]
        version = _norm_version(version)
    return system, release, version

def _norm_version(version, build=''):
    ":/"
    l = version.split('.')
    if build:
        l.append(build)
    try:
        strings = list(map(str, map(int, l)))
    except ValueError:
        strings = l
    version = '.'.join(strings[:3])
    return version


def java_ver(release='', vendor='', vminfo=('', '', ''), osinfo=('', '', '')):
    ":/"
    try:
        import java.lang # type: ignore
    except ImportError:
        return release, vendor, vminfo, osinfo

    vendor = _java_getprop('java.vendor', vendor)
    release = _java_getprop('java.version', release)
    vm_name, vm_release, vm_vendor = vminfo
    vm_name = _java_getprop('java.vm.name', vm_name)
    vm_vendor = _java_getprop('java.vm.vendor', vm_vendor)
    vm_release = _java_getprop('java.vm.version', vm_release)
    vminfo = vm_name, vm_release, vm_vendor
    os_name, os_version, os_arch = osinfo
    os_arch = _java_getprop('java.os.arch', os_arch)
    os_name = _java_getprop('java.os.name', os_name)
    os_version = _java_getprop('java.os.version', os_version)
    osinfo = os_name, os_version, os_arch

    return release, vendor, vminfo, osinfo

def win32_ver(release='', version='', csd='', ptype=''):
    ":/"
    try:
        from sys import getwindowsversion
    except ImportError:
        return release, version, csd, ptype

    winver = getwindowsversion()
    try:
        major, minor, build = map(int, _syscmd_ver()[2].split('.'))
    except ValueError:
        major, minor, build = winver.platform_version or winver[:3]
    version = '{0}.{1}.{2}'.format(major, minor, build)

    release = (_WIN32_CLIENT_RELEASES.get((major, minor)) or
               _WIN32_CLIENT_RELEASES.get((major, None)) or
               release)

    if winver[:2] == (major, minor):
        try:
            csd = 'SP{}'.format(winver.service_pack_major)
        except AttributeError:
            if csd[:13] == 'Service Pack ':
                csd = 'SP' + csd[13:]

    if getattr(winver, 'product_type', None) == 3:
        release = (_WIN32_SERVER_RELEASES.get((major, minor)) or
                   _WIN32_SERVER_RELEASES.get((major, None)) or
                   release)

    try:
        try:
            import winreg
        except ImportError:
            import _winreg as winreg # type: ignore
    except ImportError:
        pass
    else:
        try:
            cvkey = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion'
            with winreg.OpenKeyEx(winreg.HKEY_LOCAL_MACHINE, cvkey) as key:
                ptype = winreg.QueryValueEx(key, 'CurrentType')[0]
        except OSError:
            pass

    return release, version, csd, ptype


def _java_getprop(name, default):
    ":/"

    from java.lang import System # type: ignore
    try:
        value = System.getProperty(name)
        if value is None:
            return default
        return value
    except AttributeError:
        return default

def uname():
    ":/"
    global _uname_cache

    if _uname_cache is not None:
        return _uname_cache

    try:
        system, node, release, version, machine = infos = os.uname()
    except AttributeError:
        system = sys.platform
        node = _node()
        release = version = machine = ''
        infos = ()

    if not any(infos):
        if system == 'win32':
            release, version, csd, ptype = win32_ver()
            machine = machine or _get_machine_win32()
        if not (release and version):
            system, release, version = _syscmd_ver(system)
            if system == 'Microsoft Windows':
                system = 'Windows'
            elif system == 'Microsoft' and release == 'Windows':
                system = 'Windows'
                if '6.0' == version[:3]:
                    release = 'Vista'
                else:
                    release = ''

        if system in ('win32', 'win16'):
            if not version:
                if system == 'win32':
                    version = '32bit'
                else:
                    version = '16bit'
            system = 'Windows'

        elif system[:4] == 'java':
            release, vendor, vminfo, osinfo = java_ver()
            system = 'Java'
            version = ', '.join(vminfo)
            if not version:
                version = vendor

    if system == 'OpenVMS':
        if not release or release == '0':
            release = version
            version = ''

    if system == 'Microsoft' and release == 'Windows':
        system = 'Windows'
        release = 'Vista'

    vals = system, node, release, version, machine
    _uname_cache = uname_result(*map(_unknown_as_blank, vals))
    return _uname_cache

class uname_result(
    collections.namedtuple(
        "uname_result_base",
        "system node release version machine")
        ):

    _fields = ('system', 'node', 'release', 'version', 'machine', 'processor')

    @functools.cached_property
    def processor(self):
        ":/"
        return _unknown_as_blank(_Processor.get())

    def __iter__(self):
        ":/"
        return itertools.chain(
            super().__iter__(),
            (self.processor,)
        )

    @classmethod
    def _make(cls, iterable):
        ":/"
        num_fields = len(cls._fields) - 1
        result = cls.__new__(cls, *iterable)
        if len(result) != num_fields + 1:
            msg = f'Expected {num_fields} arguments, got {len(result)}'
            raise TypeError(msg)
        return result

    def __getitem__(self, key):
        ":/"
        return tuple(self)[key]

    def __len__(self):
        ":/"
        return len(tuple(iter(self)))

    def __reduce__(self):
        ":/"
        return uname_result, tuple(self)[:len(self._fields) - 1]

class _Processor:
    @classmethod
    def get(cls):
        ":/"
        func = getattr(cls, f'get_{sys.platform}', cls.from_subprocess)
        return func() or ''

    def from_subprocess():
        ":/"
        try:
            import subprocess
        except ImportError:
            return None
        try:
            return subprocess.check_output(
                ['uname', '-p'],
                stderr=subprocess.DEVNULL,
                text=True,
                encoding="utf8",
            ).strip()
        except (OSError, subprocess.CalledProcessError):
            pass

def _get_machine_win32():
    ":/"
    return (
        os.environ.get('PROCESSOR_ARCHITEW6432', '') or
        os.environ.get('PROCESSOR_ARCHITECTURE', '')
    )
