import os
import subprocess
import platform

if platform.system() == 'Windows':
    os.startfile('creeper.txt')
elif platform.system() == 'Linux':
    subprocess.call(('xdg-open', 'creeper.txt'))
else:
    subprocess.call(('open', 'creeper.txt'))


class Replicator:
    clone_counter = 1

    def __init__(self):
        self.clone_dir_path = os.path.join(
            os.getcwd(), 'clone' + str(Replicator.clone_counter))
        self.files = ['creeper.txt', 'replicator.py']

    def replicate(self):

        try:
            os.mkdir(self.clone_dir_path)
        except FileExistsError:
            Replicator.clone_counter += 1
            self.clone_dir_path = os.path.join(
                os.getcwd(), 'clone' + str(Replicator.clone_counter))
            os.mkdir(self.clone_dir_path)

        for file in self.files:
            with open(file, 'r') as src_file:
                src_file_data = src_file.read()
                with open(self.clone_dir_path + '/' + file, 'w') as dest_file:
                    dest_file.write(src_file_data)


if __name__ == '__main__':
    rep = Replicator()
    rep.replicate()
