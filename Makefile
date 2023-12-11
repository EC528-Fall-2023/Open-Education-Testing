SHELL := /bin/bash
.PHONY: help build pub clean
DIR=$(shell pwd -P)
NAME=$(shell basename ${DIR})

OUTDIR=${DIR}
CNTDIR=content

.PHONY: all jb build fixlinks images pub clean

all: build

jb:
	# -v verbose
	# -all re-build all pages not just changed pages
	# -W make warning treated as errors
	# -n nitpick generate warnings for all missing links
	# --keep-going despite -W don't stop delay errors till the end
	jupyter-book build -v --all -n --keep-going --path-output ${OUTDIR} --config ${PWD}/${CNTDIR}/${NAME}_config.yml --toc ${PWD}/${CNTDIR}/${NAME}_toc.yml ${CNTDIR}

images: jb
	-mkdir -p ${OUTDIR}/_build/html/images
	cp -r ${CNTDIR}/images/* ${OUTDIR}/_build/html/images

fixlinks: images
	./fixlinks.sh ${OUTDIR}/_build/html

build: ## build the book
build: fixlinks

pub:
	ghp-import -n -p --prefix=${NAME} -f ${OUTDIR}/_build/html
	@./ghp-nojekyll.sh
	@echo "Published to:"
	@./ghp-url.sh ${NAME}

clean:
	${RM} -r  ${OUTDIR}

help:
# http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
	@grep -E '^[a-zA-Z0-9_%/-]+:.*?## .*$$' $(MAKEFILE_LIST) |  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

TOC=./content/${NAME}_toc.yml
# make toc creates the manifest specified in your table of contents such that every file has
# a corresponding .ipynb file at the corresponding path with the title of the file in a 
# jupyter markdown cell as starter. If the file already exists, nothing is done.
toc:
	@echo "Creating notebooks as specified by " $(TOC)
	@for FILENAME in $$(yq e '.[] | .. | .file?' $(TOC) | grep -v "null"); do \
		FN=./content/$${FILENAME}; \
		DIR=$$(dirname $$FN); \
		IMG_DIR=$${DIR}/images; \
		TITLE="$${FILENAME##*/}"; \
		mkdir -p $${DIR}; \
		mkdir -p $${IMG_DIR}; \
		if [ ! -f $${FN}.ipynb ]; then \
			echo "{\"cells\":[{\"cell_type\":\"markdown\",\"id\":\"c8127f84-6227-4932-98da-dc745c2818e9\",\"metadata\":{},\"source\":[\"# $${TITLE}\"]}],\"metadata\":{},\"nbformat\":4,\"nbformat_minor\":5}" >> $${FN}.ipynb; \
			echo "created" $${FN}.ipynb; \
		fi; \
	done
	@echo "Done!"
		
clean_toc:
	@read -p "Are you sure you want to delete all the notebook files in your OPE book specified by your table of contents?(y/n)" ANSWER; \
	if [[ $$ANSWER == "y" ]]; then \
		echo "Deleting notebooks as specified by" $(TOC); \
		deleted_dir=""; \
		for FILENAME in $$(yq e '.[] | .. | .file?' $(TOC) | grep -v "null"); do \
			FN=./content/$${FILENAME}; \
			DIR=$$(dirname $$FN); \
			if [[ $$deleted_dir  != $${DIR} ]]; then \
				rm -rf $${DIR}; \
				deleted_dir=$${DIR}; \
				echo "deleted" $${DIR}; \
			fi; \
		done; \
		echo "Done!"; \
	else \
		echo "Clean canceled."; \
	fi
