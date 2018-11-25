ifeq ($(PACKAGE_SET),dom0)
	ifeq ($(DIST),fc29)
		RPM_SPEC_FILES := python-createrepo.spec
	endif
endif

NO_ARCHIVE := 1
