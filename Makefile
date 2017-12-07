GIT_VERSION = $(shell git describe --always --dirty)
VER_BASE    = 1
VERSION     = 1.0.$(shell echo $$(( $$(git rev-list --all --count) - $(VER_BASE) )))

PROJECT     = chatter
REGISTRY	= echoo.reg.us

build: version.py
	@echo ====================build====================
	python setup.py egg_info --egg-base /tmp sdist

package: build
	@echo ====================package====================
	VERSION=$(VERSION) PROJECT=$(PROJECT) exec ./scripts/package
	docker tag $(PROJECT):$(VERSION) $(REGISTRY)/$(PROJECT):$(VERSION)

test: package
	@echo ====================test====================
	VERSION=$(VERSION) PROJECT=$(PROJECT) exec ./scripts/test

publish: package
	@echo ====================publish====================
	docker push $(REGISTRY)/$(PROJECT):$(VERSION)

clean:
	rm -rf dist
	rm -rf package/${PROJECT}.tar.gz package/requirements.txt package/pip.conf package/main.py

package-clean: clean
	docker images | grep -E "($(PROJECT))" | awk '{print $$3}' | uniq | xargs -I {} docker rmi --force {}

# populate version
ifeq ($(shell test "$$(cat .version 2>/dev/null)" = $(GIT_VERSION) && echo "1" ), )
.PHONY: .version
.version:
	@echo $(GIT_VERSION) >.version
endif

version.py: .version
	@echo "__version__ = '$(VERSION)'\n" >version.py
	@echo "__git__ = '$(GIT_VERSION)'\n" >>version.py