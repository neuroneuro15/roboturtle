from setuptools import setup

setup(
    name='roboturtle',
    version='0.1',
    packages=['roboturtle'],
    url='http://www.github.com/erfindergarden/roboturtle',
    license='',
    author='Nicholas A. Del Grosso',
    author_email='delgrosso.nick@gmail.com',
    description='',
    requires=['warnings', 'pyglet', 'click'],
    entry_points={'gui_scripts': ['roborotate=roboturtle.rotation_timing:run'],
                  'console_scripts':
                      [
                        'roboserver=roboturtle.roboserver:start_roboserver',
                        'turtleserver=roboturtle.roboserver:start_turtleserver'
                      ]
                  },
)
