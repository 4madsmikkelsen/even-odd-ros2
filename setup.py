from setuptools import setup, find_packages

package_name = 'evenodd'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='student@student.com',
    description='ROS2 even odd publisher subscriber package',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_node = evenodd.publisher_node:main',
            'subscriber_node = evenodd.subscriber_node:main',
        ],
    },
)
