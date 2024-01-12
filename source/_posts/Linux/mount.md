---
toc: true
url: mount
covercopy: <a href="https://pixabay.com/photos/hard-drive-disk-hardware-data-hard-607461/">© bohed</a>
priority: 10000
date: 2022-09-14 14:17:31
title: "Disk Mount and Manage in Linux"
ytitle: "Disk Mount and Manage in Linux"
description: "Disk Mount and Manage in Linux"
excerpt: "Disk mount in Linux refers to the process of making a file system available for the operating system to access on a particular directory. This is done by mounting the file system on a directory, which makes it accessible to the system and its users. <a title='GhatGPT'>Who said this?</a>"
tags: [Linux, Scripting, bash, CLI Tools, Disk, System]
category: [Linux, System]
cover: "https://cdn.pixabay.com/photo/2015/01/22/07/03/hard-drive-607461_1280.jpg"
thumbnail: "https://cdn.pixabay.com/photo/2015/01/22/07/03/hard-drive-607461_1280.jpg"
---


## Mount the disk

if the name of your drive you want to mount is `/dev/sda2`. And you want to mount it as `/media/Side`, the quickest way is:

```bash
sudo mkdir /media/Side
sudo mount /dev/sda2 /media/Side
```

## Check the drive list and find it

`df -h` could view all hard drive storage information
`fdisk -l`  could print more detailed partition drives

```bash
sudo fdisk -l
```

As you can see the basic information belowe. This Disk as 3.7 TiB in total but was splited into four partitions

<pre>
Disk /dev/sda: 3.7 TiB, 4000787030016 bytes, 7814037168 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 4096 bytes
I/O size (minimum/optimal): 4096 bytes / 4096 bytes
Disklabel type: gpt
Disk identifier: 01EA470B-E7C7-4AB8-BCE5-88319B2E0C64

Device          Start        End    Sectors  Size Type
/dev/sda1        2048     264191     262144  128M Microsoft reserved
/dev/sda2      264192 3894284119 3894019928  1.8T Microsoft basic data
/dev/sda3  3894284288 3895334911    1050624  513M EFI System
/dev/sda4  3895334912 7814035455 3918700544  1.8T Linux filesystem
</pre>


we can also use `sudo parted -l` to print partitions, only ([phoenixnap, 2020](https://phoenixnap.com/kb/linux-create-partition)):
<pre>
Model: ATA ST4000DM004-2CV1 (scsi)
Disk /dev/sda: 4001GB
Sector size (logical/physical): 512B/4096B
Partition Table: gpt
Disk Flags:

Number  Start   End     Size    File system  Name                          Flags
 1      1049kB  135MB   134MB                Microsoft reserved partition  msftres
 2      135MB   1994GB  1994GB  ntfs         Basic data partition          msftdata
 3      1994GB  1994GB  538MB   fat32        EFI System Partition          boot, esp
 4      1994GB  4001GB  2006GB  ext4
</pre>

And you can see that half of it, 1.8 TiB was given Linux system and another half was given Windows System.




## Windows ntf disk in Linux


<pre>
mkdir: cannot create directory 'ken': Read-only file system
</pre>


```bash
sudo ntfsfix /dev/sda2
```

<pre>
Mounting volume... OK
Processing of $MFT and $MFTMirr completed successfully.
Checking the alternate boot sector... OK
NTFS volume version is 3.1.
NTFS partition /dev/sda2 was processed successfully.
</pre>

You may need to reboot and re-mount to work



## Mount online Web sever

> The "sshfs" command in Linux is used to mount a remote file system on a local machine over an SSH connection. It allows users to securely access and manipulate files on a remote machine as if they were on the local machine. The command syntax typically involves specifying the remote host and directory to mount, as well as the local directory to mount it to. 
> © ChatGPT

```bash
sudo apt-get install sshfs
sudo mkdir /mnt/Ken_lap
sudo chmod 777 /mnt/Ken_lap
sshfs Karroben@192.168.1.110:/mnt/8A26661926660713/ /mnt/Ken_lap
```










<style>
pre {
  background-color:#38393d;
  color: #5fd381;
}
</style>
