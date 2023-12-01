.PHONY: all toc

TOC := $(shell find . -name "*toc.yml" -print -quit)
# Default target
all: toc

toc:
	@echo "Creating notebooks as specified by " $(TOC)
	@for FILENAME in $$(yq e '.[] | .. | .file?' $(TOC) | grep -v "null"); do \
		DIR=$$(dirname $$FILENAME); \
		TITLE="$${FILENAME##*/}"; \
		mkdir -p $${DIR}; \
		if [ ! -f $${FILENAME}.ipynb ]; then \
			echo "{\"cells\":[{\"cell_type\":\"markdown\",\"id\":\"c8127f84-6227-4932-98da-dc745c2818e9\",\"metadata\":{},\"source\":[\"# $${TITLE}\"]}],\"metadata\":{},\"nbformat\":4,\"nbformat_minor\":5}" >> $${FILENAME}.ipynb; \
			echo "created" $${FILENAME}.ipynb; \
		fi; \
	done
	@echo "Done!"
		
clean:
	@read -p "Are you sure you want to delete all the notebook files in your OPE book specified by your table of contents?(y/n)" ANSWER; \
	if [[ $$ANSWER == "y" ]]; then \
		echo "Deleting notebooks as specified by" $(TOC); \
		deleted_dir=""; \
		for FILENAME in $$(yq e '.[] | .. | .file?' $(TOC) | grep -v "null"); do \
			DIR=$$(dirname $$FILENAME); \
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
