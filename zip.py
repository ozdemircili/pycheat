# work with a tarball compressed archive file (similar to zip)
# Python module tarfile is better and more flexible than zipfile
# it allows gzip and the even denser bzip2 compression
# tested with Python24       vegaseat     18jan2007
import tarfile
str1 = "If you want breakfast in bed, sleep in the kitchen."
str2 = "Dinner is ready when the smoke alarm goes off."
str3 = "How can I miss you if you won't go away?"
# write test file 1
fout = open("TarTest1.txt", "w")
fout.write(str1)
fout.close()
# write test file 2
fout = open("TarTest2.txt", "w")
fout.write(str2)
fout.close()
# write test file 3
fout = open("TarTest3.txt", "w")
fout.write(str3)
fout.close()
# pick your compression ...
# for uncompressed use file extension .tar and modifier "w"
# for gzip compressed use file extension .tar.gz and modifier "w:gz"
# for bzip2 super compressed use file extension .tar.bz2 and "w:bz2"
# use "w", "w:gz" or "w:bz2" for all file types, including binary files
tar = tarfile.open("TarTest.tar.bz2", "w:bz2")
# turn the three test files into a tar archive
for name in ["TarTest1.txt", "TarTest2.txt", "TarTest3.txt"]:
    tar.add(name)
tar.close()
print '-'*40
# test if the file is a valid tar file
tfilename = "TarTest.tar.bz2"
if tarfile.is_tarfile(tfilename):
    print "%s is a valid tar file" % tfilename
else:
    print "%s is not a valid tar file" % tfilename
print '-'*40
# read the tarfile you just wrote
tar = tarfile.open("TarTest.tar.bz2", "r:bz2")
file_list = []
for file in tar:
    # show filename and size (bytes)
    print "file %s has a size of %d bytes" % (file.name, file.size)
    file_list.append(file.name)
# another way to get the file list
file_list2 = tar.getnames()
print '-'*50
print file_list
print file_list2
print '-'*50
# pick one of the three files in the tar-archive (tarball)
filename = file_list[1]
# decompress the particular file
data = tar.extractfile(filename).read()
# if it's a text file, show contents
if filename.endswith(".txt"):
    print "Content of file %s in the tarball:" % filename
    print data
# write the files out to new files
for fname in tar.getnames():
    # extract/decompress the data of each file
    data = tar.extractfile(fname).read()
    # optionally change the filename
    new_file = "new_" + fname
    print "File %s written!" % new_file
    # write the decompressed data to a file
    fout = open(new_file, "w")
    fout.write(data)
    fout.close()
# done, close the tar file ...
tar.close()
