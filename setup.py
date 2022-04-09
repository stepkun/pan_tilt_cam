import os
from glob import glob
from setuptools import setup

package_name = 'pan_tilt_cam'

setup(
    name=package_name,
    version='0.0.0',
    # Packages to export
    packages=[package_name],
    py_modules=[],
    # Files we want to install, specifically launch files
    data_files=[
        # Install marker file in the package index
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        # Include our package.xml file
        ('share/' + package_name, ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='stepkun',
    maintainer_email='stephan.kunz@kabelbw.de',
    keywords=['pan', 'tilt', 'camera'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: NGMC-License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='WaveShare Pan-Tilt HAT with Camera package',
    license='NGMC-License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'initial_pos = pan_tilt_cam.initial_pos:main',
            'test = pan_tilt_cam.test:main',
        ],
    },
)
