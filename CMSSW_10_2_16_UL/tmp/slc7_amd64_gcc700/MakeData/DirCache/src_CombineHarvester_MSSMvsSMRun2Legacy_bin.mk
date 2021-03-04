ifeq ($(strip $(PreFitSignalShapes)),)
PreFitSignalShapes := self/src/CombineHarvester/MSSMvsSMRun2Legacy/bin
PreFitSignalShapes_files := $(patsubst src/CombineHarvester/MSSMvsSMRun2Legacy/bin/%,%,$(foreach file,PreFitSignalShapes.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/MSSMvsSMRun2Legacy/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/MSSMvsSMRun2Legacy/bin/$(file). Please fix src/CombineHarvester/MSSMvsSMRun2Legacy/bin/BuildFile.))))
PreFitSignalShapes_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/MSSMvsSMRun2Legacy/bin/BuildFile
PreFitSignalShapes_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools CombineHarvester/CombinePdfs CombineHarvester/MSSMvsSMRun2Legacy
PreFitSignalShapes_PACKAGE := self/src/CombineHarvester/MSSMvsSMRun2Legacy/bin
ALL_PRODS += PreFitSignalShapes
PreFitSignalShapes_INIT_FUNC        += $$(eval $$(call Binary,PreFitSignalShapes,src/CombineHarvester/MSSMvsSMRun2Legacy/bin,src_CombineHarvester_MSSMvsSMRun2Legacy_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
PreFitSignalShapes_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,PreFitSignalShapes,src/CombineHarvester/MSSMvsSMRun2Legacy/bin))
endif
ifeq ($(strip $(etFES)),)
etFES := self/src/CombineHarvester/MSSMvsSMRun2Legacy/bin
etFES_files := $(patsubst src/CombineHarvester/MSSMvsSMRun2Legacy/bin/%,%,$(foreach file,etFES.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/MSSMvsSMRun2Legacy/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/MSSMvsSMRun2Legacy/bin/$(file). Please fix src/CombineHarvester/MSSMvsSMRun2Legacy/bin/BuildFile.))))
etFES_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/MSSMvsSMRun2Legacy/bin/BuildFile
etFES_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools CombineHarvester/CombinePdfs CombineHarvester/MSSMvsSMRun2Legacy
etFES_PACKAGE := self/src/CombineHarvester/MSSMvsSMRun2Legacy/bin
ALL_PRODS += etFES
etFES_INIT_FUNC        += $$(eval $$(call Binary,etFES,src/CombineHarvester/MSSMvsSMRun2Legacy/bin,src_CombineHarvester_MSSMvsSMRun2Legacy_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
etFES_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,etFES,src/CombineHarvester/MSSMvsSMRun2Legacy/bin))
endif
ifeq ($(strip $(MorphingMSSMvsSM)),)
MorphingMSSMvsSM := self/src/CombineHarvester/MSSMvsSMRun2Legacy/bin
MorphingMSSMvsSM_files := $(patsubst src/CombineHarvester/MSSMvsSMRun2Legacy/bin/%,%,$(foreach file,MorphingMSSMvsSM.cpp,$(eval xfile:=$(wildcard src/CombineHarvester/MSSMvsSMRun2Legacy/bin/$(file)))$(if $(xfile),$(xfile),$(warning No such file exists: src/CombineHarvester/MSSMvsSMRun2Legacy/bin/$(file). Please fix src/CombineHarvester/MSSMvsSMRun2Legacy/bin/BuildFile.))))
MorphingMSSMvsSM_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/MSSMvsSMRun2Legacy/bin/BuildFile
MorphingMSSMvsSM_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools CombineHarvester/CombinePdfs CombineHarvester/MSSMvsSMRun2Legacy
MorphingMSSMvsSM_PACKAGE := self/src/CombineHarvester/MSSMvsSMRun2Legacy/bin
ALL_PRODS += MorphingMSSMvsSM
MorphingMSSMvsSM_INIT_FUNC        += $$(eval $$(call Binary,MorphingMSSMvsSM,src/CombineHarvester/MSSMvsSMRun2Legacy/bin,src_CombineHarvester_MSSMvsSMRun2Legacy_bin,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_BIN),bin,$(SCRAMSTORENAME_LOGS)))
MorphingMSSMvsSM_CLASS := BINARY
else
$(eval $(call MultipleWarningMsg,MorphingMSSMvsSM,src/CombineHarvester/MSSMvsSMRun2Legacy/bin))
endif
ALL_COMMONRULES += src_CombineHarvester_MSSMvsSMRun2Legacy_bin
src_CombineHarvester_MSSMvsSMRun2Legacy_bin_parent := CombineHarvester/MSSMvsSMRun2Legacy
src_CombineHarvester_MSSMvsSMRun2Legacy_bin_INIT_FUNC += $$(eval $$(call CommonProductRules,src_CombineHarvester_MSSMvsSMRun2Legacy_bin,src/CombineHarvester/MSSMvsSMRun2Legacy/bin,BINARY))
