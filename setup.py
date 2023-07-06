from cx_Freeze import setup, Executable

base = None    

executables = [Executable("ui.py", base=base)]

packages = ["idna","sys","os","fpdf","PyQt6","pandas","numpy"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "CS DGA6100",
    options = options,
    version = "0.1",
    description = 'DGA Interpretation Software by Centurion Scientific',
    executables = executables
)