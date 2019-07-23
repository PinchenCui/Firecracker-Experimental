# Firecracker-Examples
Create a basic customized Firecracker MicroVM.

* 1. Official Firecracker Documents: https://github.com/firecracker-microvm/firecracker
* 2. Build CoreOS kernel from Source: https://gist.github.com/dm0-/1f656b68491cd22e65ae0f33d4f1dd25
* 3. CoreOS developer container image: https://github.com/BugRoger/coreos-developer-docker
* 4. Customize kernel and rootfs for Firecracker: https://github.com/firecracker-microvm/firecracker/blob/master/docs/rootfs-and-kernel-setup.md

# Run Firecracker MicroVM
* Get all the needed files:
```
git clone https://github.com/PinchenCui/Firecracker-Examples.git
cd Firecracker-Examples.git
./getFiles.sh
```
* In first terminal:
```
sudo ./socket.sh
```
* In second terminal:
```
sudo ./setup.sh
```
* Firecracker MicroVM will be started in the first terminal.

# Build CoreOS Kernel From Source
- Get and run the CoreOS developer container:
```
sudo docker pull bugroger/coreos-developer:2135.5.0
sudo docker run -it bugroger/coreos-developer:2135.5.0 /bin/bash
```
- Get and Compile the CoreOS kernel in this container:
```
emerge-gitclone
emerge -gKv bootengine coreos-sources dracut
update-bootengine -o /usr/src/linux/bootengine.cpio
echo 'CONFIG_INITRAMFS_SOURCE="bootengine.cpio"' | cat \
    /var/lib/portage/coreos-overlay/sys-kernel/coreos-modules/files/amd64_defconfig-4.19 \
    - > /usr/src/linux/.config
make vmlinux
```

# Minimum Kernel
- Firecracker uses vmlinux as the bootable kernel file. As introduced in the link 4, this file can be generated by using command in Linux kernel source directory:
```
make vmlinux
```
- This step needs to asscociates with a compliation configuration file, which is included in this repo. 
  * CoreOS.conf is the config file for CoreOS compliation.
  * kernel.conf is the config file for native Linux.
  * Using CoreOS.conf with CoreOS kernel source, a 500MB kernel can be generated.
  * Using kernel.conf with Linux kernel source, a 22MB minimum kernel can be generated.

- Since the two file are not aligned, and all the configurations are not in same order, diff.py is created to compare two configuration files. 
  * Total 867 entries are different.
