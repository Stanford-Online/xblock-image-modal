FROM stvstnfrd/workbench:latest
MAINTAINER stv <stv@stanford.edu>
ADD . /root/xblock
RUN make -C /root/xblock requirements
ENV HOME /root
