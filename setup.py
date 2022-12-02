import cx_Freeze

executables = [cx_Freeze.Executable('dino.py')]

cx_Freeze.setup(
    name="dino game",
    options={'build_exe': {'package':['pygame'],
                           'include_files':['imagens', 'sons']}},

    executable = executables

)