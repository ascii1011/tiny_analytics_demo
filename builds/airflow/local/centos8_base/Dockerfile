FROM centos:8

LABEL name="cent8py310_base" \
      build-date="2022-10-01"

ENV PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin \
    LANGUAGE=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8 \
    LC_CTYPE=en_US.UTF-8 \
    LC_MESSAGES=en_US.UTF-8

RUN echo "Switch epel mirrorlist" \
    && sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-* \
    && sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*

RUN echo "Applying epel-release-..." \
    && yum -y install epel-release \
    && yum -y update

RUN dnf -y install wget sudo yum-utils make gcc openssl-devel bzip2-devel libffi-devel zlib-devel sqlite-devel
RUN cd /tmp \
    && wget https://www.python.org/ftp/python/3.10.7/Python-3.10.7.tgz \
    && tar xzf Python-3.10.7.tgz \
    && cd Python-3.10.7 \
    && sudo ./configure --with-system-ffi --with-computed-gotos --enable-loadable-sqlite-extensions \
    && sudo make -j ${nproc} \
    && sudo make altinstall \
    && sudo rm -f Python-3.10.7.tgz \
    && sudo rm -rf Python-3.10.7
RUN pip3.10 install --upgrade pip

RUN pip3.10 -V \
    && python3.10 -V
    
