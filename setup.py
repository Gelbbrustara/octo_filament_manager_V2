# FilamentManager/setup.py
import setuptools

setuptools.setup(
    name="FilamentManager",
    version="1.1",
    url="https://github.com/Gelbbrustara/octo_filament_manager_V2",
    author="Gelbbrustara",
    author_email="peterotzi79@gmail.com",
    description="OctoPrint plugin for managing prints and filament usage.",
packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "OctoPrint>=1.3.12",
    ],
    entry_points={
        "octoprint.plugin": [
            "filament_manager = filament_manager.plugin"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)