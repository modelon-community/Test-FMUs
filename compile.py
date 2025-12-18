from pymodelica import compile_fmu
from pathlib import Path
import shutil

FMUOUTPUTDIR = Path("FMUs")

def compile_model(model_name: str, target: str, version: str, compiler_options: dict):
    compiler_options = {
        "generate_runtime_option_parameters": False
    }

    compile_to = FMUOUTPUTDIR / version / target / (model_name.replace(".", "_") + ".fmu")
    compile_fmu(
        model_name,
        ["testModels"],
        target = "me",
        version = "2.0",
        compiler_options = compiler_options,
        compile_to = str(compile_to),
    )

for model_name in [
    "testModels.noStateAssertFailureFunctionLocalVariable",
    "testModels.noStateAssertFailureFunctionOutputVariable",
]:
    compiler_options = {
        "generate_runtime_option_parameters": False
    }

    compile_model(model_name,
                  target = "me",
                  version = "2.0",
                  compiler_options = compiler_options
                  )

# Zip up all the FMUs
shutil.make_archive("FMUs", format = "zip", root_dir = FMUOUTPUTDIR)
