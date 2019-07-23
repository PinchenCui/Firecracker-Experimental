# Firecracker-Examples
Create a basic customized Firecracker MicroVM.

* Official Firecracker Documents: https://github.com/firecracker-microvm/firecracker
* Build CoreOS kernel from Source: https://gist.github.com/dm0-/1f656b68491cd22e65ae0f33d4f1dd25
* CoreOS developer container image: https://github.com/BugRoger/coreos-developer-docker
* Customize kernel and rootfs for Firecracker: https://github.com/firecracker-microvm/firecracker/blob/master/docs/rootfs-and-kernel-setup.md

# Usage
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

# Misc
