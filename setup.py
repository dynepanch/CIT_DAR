from setuptools import setup
import os
from glob import glob

package_name = 'cit_dar'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ken Inaba',
    maintainer_email='jiandaoye293@gmail.com',
    description='repository for univesity homework',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
			'tips = cit_dar.tips:main',
			'send = cit_dar.send:main',
        ],
    },
)
