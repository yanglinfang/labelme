# -*- mode: python -*-
# vim: ft=python

import sys
from PyInstaller.utils.hooks import collect_submodules, collect_data_files


sys.setrecursionlimit(5000)  # required on Windows

# Collect numpy submodules to fix "cannot load module more than once" error
numpy_hiddenimports = collect_submodules('numpy')
numpy_datas = collect_data_files('numpy')

a = Analysis(
    ['labelme/__main__.py'],
    pathex=['labelme'],
    binaries=[],
    datas=[
        ('labelme/config/default_config.yaml', 'labelme/config'),
        ('labelme/icons/*', 'labelme/icons'),
        ('labelme/translate/*.qm', 'translate'),
    ] + numpy_datas,
    hiddenimports=numpy_hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
)
pyz = PYZ(a.pure, a.zipped_data)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='labelme',
    debug=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=False,
    icon='labelme/icons/icon.ico',
)
app = BUNDLE(
    exe,
    name='Labelme.app',
    icon='labelme/icons/icon.icns',
    bundle_identifier=None,
    info_plist={'NSHighResolutionCapable': 'True'},
)
