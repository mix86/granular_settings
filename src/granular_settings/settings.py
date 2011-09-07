#encoding: utf-8
import glob, os
import traceback

settings_module_path = os.path.abspath(traceback.extract_stack()[-2][0])
settings_dir_path = os.path.splitext(settings_module_path)[0]

project_path = os.path.abspath(traceback.extract_stack()[0][0])
PROJECT_PATH = os.path.split(project_path)[0]
PROJECT = os.path.split(PROJECT_PATH)[-1]

cf = glob.glob(os.path.join(settings_dir_path, '*.conf'))
cf += glob.glob(os.path.join(settings_dir_path, '*.conf.local'))

cf.sort()

for f in cf:
    execfile(os.path.abspath(f))

