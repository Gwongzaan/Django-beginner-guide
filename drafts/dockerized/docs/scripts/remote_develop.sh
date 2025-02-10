# remote develop with pycharm
# the jetbrain gateway does not work quite well
# but pycharm has some good features for faster development
# but docker on windows often say "exec <file> : file not found, even though the file does exists
# so develop with pycharm, and use remote server for testing,
# once it is ok, then commit changes
# the virtual environment that pycharm need should be in another folder other than the project folder
apt-get install sshfs
mkdir /mnt/folder_name
sshfs -o allow_other,default_permissions user@server:/path/tofolder /mnt/folder_name

# permanently mounting a remote folder
vim /etc/fstab
# to the bottom, and then paste the following text
sshfs user@server_ip:/path/to/mount /mnt/server_folder