# this was seeded from https://github.com/umsi-mads/education-notebook/blob/master/Makefile
.PHONEY: help build ope root push publish lab nb python-versions distro-versions image-sha clean
.IGNORE: ope root

# see if there is a specified customization in the base settting
SHELL := /bin/bash
# install yq for parsing config.yml and get customized tag for OPE container in same step
# from base/config.yml
CUST := $(shell sudo add-apt-repository ppa:rmescandon/yq && \
	sudo apt update && \
	sudo apt install yq -y && \
	yq eval ".ope.tag" base/config.yml)

# I think bash is failing to intialze at line 1
CUST := ope

# User must specify customization suffix
ifndef CUST
$(error CUST is not set.  You must specify which customized version of the image you want to work with. Eg. make CUST=opf build)
endif


OPE_BOOK := $(shell yq eval ".ope.book" base/config.yml)
# USER id
OPE_UID := $(shell yq eval ".ope.uid" base/config.yml)
# GROUP id
OPE_GID := $(shell yq eval ".ope.gid" base/config.yml)
# GROUP name
OPE_GROUP := $(shell yq eval ".ope.group" base/config.yml)


BASE_REG := $(shell yq eval ".base.registry" base/config.yml)/
BASE_IMAGE := $(shell yq eval ".base.image" base/config.yml)
BASE_TAG := $(shell yq eval ".base.tag" base/config.yml)
DATE_TAG := $(shell date +"%m.%d.%y_%H.%M.%S")

OPE_BOOK_USER := $(shell yq eval ".ope.book_user" base/config.yml)
OPE_BOOK_REG := $(shell yq eval ".ope.book_registry" base/config.yml)/
OPE_BOOK_IMAGE := $(OPE_BOOK_USER)/$(OPE_BOOK)
OPE_BETA_TAG := :beta-$(CUST)
OPE_PUBLIC_TAG := :$(CUST)

BASE_DISTRO_PACKAGES := $(shell yq eval ".distro_pkgs" base/config.yml | sed 's|- ||g')
PYTHON_PREREQ_VERSIONS := $(shell yq eval ".python_prereqs" base/config.yml | sed 's|- ||g')
PYTHON_INSTALL_PACKAGES := $(shell yq eval ".python_pkgs" base/config.yml | sed 's|- ||g')
PIP_INSTALL_PACKAGES := $(shell yq eval ".pip_pkgs" base/config.yml | sed 's|- ||g')

JUPYTER_ENABLE_EXTENSIONS := $(shell yq eval ".jupyter.enable_exts" base/config.yml | sed 's|- ||g')
JUPYTER_DISABLE_EXTENSIONS := $(shell yq eval ".jupyter.disable_exts" base/config.yml | sed 's|- ||g' | tr "'" ' ') 

# expand installation so that the image feels more like a proper UNIX user environment with man pages, etc.
UNMIN := yes

# Common docker run configuration designed to mirror as closely as possible the openshift experience
# if port mapping for SSH access
SSH_PORT := 2222

# we mount here to match openshift
MOUNT_DIR := /opt/app-root/src
HOST_DIR := ${HOME}

# include vars for image tag
TIME ?= 
SIZE ?=

help:
# http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z0-9_%/-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


build: DARGS ?= --build-arg FROM_REG=$(BASE_REG) \
                   --build-arg FROM_IMAGE=$(BASE_IMAGE) \
                   --build-arg FROM_TAG=$(BASE_TAG) \
                   --build-arg OPE_UID=$(OPE_UID) \
                   --build-arg OPE_GID=$(OPE_GID) \
                   --build-arg OPE_GROUP=$(OPE_GROUP) \
                   --build-arg ADDITIONAL_DISTRO_PACKAGES="$(BASE_DISTRO_PACKAGES)" \
                   --build-arg PYTHON_PREREQ_VERSIONS="$(PYTHON_PREREQ_VERSIONS)" \
                   --build-arg PYTHON_INSTALL_PACKAGES="$(PYTHON_INSTALL_PACKAGES)" \
                   --build-arg PIP_INSTALL_PACKAGES="$(PIP_INSTALL_PACKAGES)"
build: ## Make the image customized appropriately
	docker build $(DARGS) $(DCACHING) -t $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_BETA_TAG) base


push: DARGS ?=
push: ## push private build
# make dated version
	docker tag  $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_BETA_TAG) $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_BETA_TAG)_$(DATE_TAG)_$(TIME)_$(SIZE)
# push to private image repo
	docker push $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_BETA_TAG)_$(DATE_TAG)_$(TIME)_$(SIZE)
# push to update tip to current version
	docker push $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_BETA_TAG)


pull-beta: DARGS ?=
pull-beta: ## pull most recent private version
	docker pull $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_BETA_TAG)


publish: pull-beta
publish: DARGS ?=
publish: ## publish current private build to public published version
# make dated version
	docker tag $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_BETA_TAG) $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_PUBLIC_TAG)_$(DATE_TAG)_$(TIME)_$(SIZE)
# push to private image repo
	docker push $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_PUBLIC_TAG)_$(DATE_TAG)_$(TIME)_$(SIZE)
# copy to tip version
	docker tag $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_BETA_TAG) $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_PUBLIC_TAG)_$(TIME)_$(SIZE)
# push to update tip to current version
	docker push $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_PUBLIC_TAG)_$(TIME)_$(SIZE)


checksum: ARGS ?= find / -not \( -path /proc -prune \) -not \( -path /sys -prune \) -type f -exec stat -c '%n %a' {} + | LC_ALL=C sort | sha256sum | cut -c 1-64
checksum: DARGS ?= -u 0
checksum: ## start private version  with root shell to do admin and poke around
	@-docker run -i --rm $(DARGS) $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_BETA_TAG) $(ARGS)

run-beta: ARGS ?=
run-beta: DARGS ?= -u $(OPE_UID):$(OPE_GID) -v "${HOST_DIR}":"${MOUNT_DIR}" -v "${SSH_AUTH_SOCK}":"${SSH_AUTH_SOCK}" -v "${SSH_AUTH_SOCK}":"${SSH_AUTH_SOCK}" -e SSH_AUTH_SOCK=${SSH_AUTH_SOCK} -p ${SSH_PORT}:22
run-beta: PORT ?= 8888
run-beta: ## start published version with jupyter lab interface
	docker run -i --rm -p $(PORT):$(PORT) $(DARGS) $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_BETA_TAG) $(ARGS)

show-tag: ARGS ?=
show-tag: DARGS ?=
show-tag: ## tag current private build as beta
	@-echo $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_BETA_TAG)
  

### DEBUG TARGETS

root: ARGS ?= /bin/bash
root: DARGS ?= -u 0
root: ## start private version  with root shell to do admin and poke around
	-docker run -it --rm $(DARGS) $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_BETA_TAG) $(ARGS)

user: ARGS ?= /bin/bash
user: DARGS ?=
user: ## start private version with usershell to poke around
	-docker run -it --rm $(DARGS) $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_BETA_TAG) $(ARGS)


### PUBLIC USAGE TARGETS
pull: 
pull: ## pull most recent public version
	docker pull $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_PUBLIC_TAG)_$(TIME)_$(SIZE)

run: pull
run: ARGS ?=
run: DARGS ?= -u $(OPE_UID):$(OPE_GID) -v "${HOST_DIR}":"${MOUNT_DIR}" -v "${SSH_AUTH_SOCK}":"${SSH_AUTH_SOCK}" -v "${SSH_AUTH_SOCK}":"${SSH_AUTH_SOCK}" -e SSH_AUTH_SOCK=${SSH_AUTH_SOCK} -p ${SSH_PORT}:22
run: PORT ?= 8888
run: ## start published version with jupyter lab interface
	docker run -it --rm -p $(PORT):$(PORT) $(DARGS) $(OPE_BOOK_REG)$(OPE_BOOK_IMAGE)$(OPE_PUBLIC_TAG)_$(TIME)_$(SIZE) $(ARGS) 


