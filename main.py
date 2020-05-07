import os, sys
from global_constants import DB_NAME


if not os.path.exists(DB_NAME):
    sys.exit("ERROR: No database detected. Please execute setup.py first!")


from peewee import *



def main():
    import mgr.mgr_voices

if __name__ == '__main__':
	main()