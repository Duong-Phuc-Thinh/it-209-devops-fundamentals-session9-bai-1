# BÁO CÁO KIỂM TRA DOCKER ENGINE VÀ CONTAINER HELLO-WORLD

- **Mục tiêu**: Kiểm tra kết nối tới Docker Daemon không cần quyền sudo và khởi chạy container đầu tiên.
- **Đường dẫn bài tập**: `homework/session_09/ex1/`

## Lệnh: `docker version`
**Mục đích**: Kiểm tra phiên bản Docker CLI và Server Daemon

```text
Client: Docker Engine - Community
 Version:           24.0.7
 API version:       1.43
 Go version:        go1.20.10
 Git commit:        afdd53b
 Built:             Thu Oct 26 09:08:01 2023
 OS/Arch:           linux/amd64
 Context:           default

Server: Docker Engine - Community
 Engine:
  Version:          24.0.7
  API version:      1.43 (minimum version 1.12)
  Go version:       go1.20.10
  Git commit:       311b9ff
  Built:            Thu Oct 26 09:08:01 2023
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.24
  GitCommit:        61f9fd88f79f081414d6fa3bdee3c0808a011e3f
 runc:
  Version:          1.1.9
  GitCommit:        v1.1.9-0-gccaecfc
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```

## Lệnh: `docker info`
**Mục đích**: Kiểm tra cấu hình chi tiết hệ thống Docker Engine

```text
Client:
 Context:    default
 Debug Mode: false

Server:
 Containers: 1
  Running: 0
  Paused: 0
  Stopped: 1
 Images: 1
 Server Version: 24.0.7
 Storage Driver: overlay2
  Backing Filesystem: extfs
  Supports d_type: true
  Using metacopy: false
 Logging Driver: json-file
 Cgroup Driver: systemd
 Cgroup Version: 2
 Plugins:
  Volume: local
  Network: bridge host ipvlan macvlan null overlay
  Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
 Swarm: inactive
 Runtimes: io.containerd.runc.v2 runc
 Default Runtime: runc
 Init Binary: docker-init
 containerd version: 61f9fd88f79f081414d6fa3bdee3c0808a011e3f
 runc version: v1.1.9-0-gccaecfc
 init version: de40ad0
 Security Options:
  apparmor
  seccomp
   Profile: builtin
  cgroupns
 Kernel Version: 5.15.0-89-generic
 Operating System: Ubuntu 22.04.3 LTS
 OSType: linux
 Architecture: x86_64
 CPUs: 4
 Total Memory: 7.68GiB
 Name: ubuntu-docker-node
 ID: 3dfb868a-24cb-4a64-9b21-42db9d7bb3d1
 Docker Root Dir: /var/lib/docker
 Debug Mode: false
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
 Live Restore Enabled: false
```

## Lệnh: `docker run hello-world`
**Mục đích**: Khởi chạy container kiểm tra Hello-World

```text
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
7190e5904de1: Pulling fs layer
7190e5904de1: Verifying Checksum
7190e5904de1: Download complete
7190e5904de1: Pull complete
Digest: sha256:d58e752213a51785838f9eed2b7a498fa1cb320f7ab2911f6ed24d2d465f9a66
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

## Kết luận
- **Trạng thái**: THÀNH CÔNG (PASS)
- Docker Daemon đang hoạt động tốt và user hiện tại có quyền gọi Docker CLI không cần sudo.
- Đã kéo image và thực thi container `hello-world` thành công.
