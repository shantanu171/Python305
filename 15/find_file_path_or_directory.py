import os.path
for file in [__file__, os.path.dirname(__file__),'/','./broken_link']:
    print('file : ',file)
    print('Absolute : ',os.path.isabs(file))
    print('Is file? : ',os.path.isfile(file))
    print('Is dir? : ',os.path.isdir(file))
    print('Is link? : ',os.path.islink(file))
    print('exixts : ',os.path.exists(file))
    print('link exixts : ',os.path.lexists(file))