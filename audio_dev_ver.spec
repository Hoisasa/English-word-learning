# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['audio_dev_ver.py'],
    pathex=[],
    binaries=[],
    datas=[('images', 'images'), ('audiofiles', 'audiofiles'), ('db_test.json', '.'), ('python_gui.py', '.'), ('python_gui2.py', '.'), ('grouping_main.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PySide6'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='audio_dev_ver',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['images\\unolingo_P64_icon.ico'],
)
