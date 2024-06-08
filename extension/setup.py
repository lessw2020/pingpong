# (c) Meta Platforms, Inc. and affiliates. 

from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

setup(
    name="cutlass",
    ext_modules=[
        CUDAExtension(
            "cutlass",
            [
                "cutlass_interface.cpp",
                "cutlass_kernel.cu",
            ],
            include_dirs=[
                "/data/users/less/local/cutlass_local/include",
            ],
        )
    ],
    cmdclass={"build_ext": BuildExtension.with_options(no_python_abi_suffix=True)},
)
