from setuptools import setup

package_name = 'CIT_DAR'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
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
			'tips = CIT_DAR.tips:main',
			'send = CIT_DAR.send:main',
        ],
    },
)
