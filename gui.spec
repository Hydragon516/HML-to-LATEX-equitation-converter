# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['gui.py'],
             pathex=['C:\\Users\\nicet\\OneDrive\\바탕 화면\\hml-equation-parser-master'],
             binaries=[],
             datas=[('./hml_equation_parser/config.json', './hml_equation_parser'),
                    ('./hml_equation_parser/convertMap.json', './hml_equation_parser')
                    ],
             hiddenimports=["hml_equation_parser.__init__",
                            "hml_equation_parser.hmlParser",
                            "hml_equation_parser.hulkEqParser",
                            "hml_equation_parser.hulkReplaceMethod"
                            ],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
