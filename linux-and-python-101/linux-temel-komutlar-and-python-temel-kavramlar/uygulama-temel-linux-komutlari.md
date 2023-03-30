---
cover: >-
  https://images.unsplash.com/photo-1581261946248-3f8d138d74dc?crop=entropy&cs=srgb&fm=jpg&ixid=MnwxOTcwMjR8MHwxfHNlYXJjaHw0fHxmYXN0fGVufDB8fHx8MTY4MDE2OTczNA&ixlib=rb-4.0.3&q=85
coverY: -229
---

# 🚀 Uygulama: Temel linux komutları

| Print working directory                                               | pwd                                        |
| --------------------------------------------------------------------- | ------------------------------------------ |
| Change your directory as /usr/                                        | cd /usr/                                   |
| Change your directory as parent directory                             | cd ..                                      |
| List all file in /usr directory                                       | ls –a /usr                                 |
| List hidden file and the detailed specifications  of /usr directory   | ls –al /usr                                |
| Create  folder1 and folder 2 into your home directory                 | mkdir folder1 folder2                      |
| Create  folder1 and folder 2 into your home directory                 | mkdir folder1 folder2                      |
| Create folder3 into folder1                                           | mkdir folder1/folder3                      |
| Create  file1.txt and file2.txt into folder1                          | touch folder1/file1.txt folder1/file2.txt  |
| Create file3.txt into folder3                                         | touch folder3/file3.txt                    |
| Create soft link link\_file1 for file1.txt                            | ln –s file1.txt link\_file1                |
| Delete file1.txt                                                      | rm –f file.txt                             |
| Delete folder1                                                        | rm –r folder1                              |
| Delete  link\_file1                                                   | rm –rf link\_file1                         |
| Show content of /etc/passwd                                           | cat /etc/passwd                            |
| Copy  /etc/rc.d directory into your home directory                    | cp /etc/rc.d  /root/.                      |
| Move rc.d file into folder2                                           | mv rc.d /folder2/.                         |
| Rename rc.d file as renamed\_rc.d                                     | mv rc.d renamed\_rc.d                      |
| Change renamed\_rc.d permissions as rwxr-xr-x                         | chmod 755 renamed\_rc.d                    |
| Show disk usage info                                                  | df                                         |
| Show current running process                                          | ps                                         |
| Show all process                                                      | top                                        |
| Run firefox and kill the process                                      | kill 2051                                  |
