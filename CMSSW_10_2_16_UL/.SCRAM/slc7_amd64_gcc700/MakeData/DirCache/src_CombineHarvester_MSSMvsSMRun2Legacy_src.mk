ifeq ($(strip $(CombineHarvester/MSSMvsSMRun2Legacy)),)
ALL_COMMONRULES += src_CombineHarvester_MSSMvsSMRun2Legacy_src
src_CombineHarvester_MSSMvsSMRun2Legacy_src_parent := CombineHarvester/MSSMvsSMRun2Legacy
src_CombineHarvester_MSSMvsSMRun2Legacy_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_CombineHarvester_MSSMvsSMRun2Legacy_src,src/CombineHarvester/MSSMvsSMRun2Legacy/src,LIBRARY))
CombineHarvesterMSSMvsSMRun2Legacy := self/CombineHarvester/MSSMvsSMRun2Legacy
CombineHarvester/MSSMvsSMRun2Legacy := CombineHarvesterMSSMvsSMRun2Legacy
CombineHarvesterMSSMvsSMRun2Legacy_files := $(patsubst src/CombineHarvester/MSSMvsSMRun2Legacy/src/%,%,$(wildcard $(foreach dir,src/CombineHarvester/MSSMvsSMRun2Legacy/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
CombineHarvesterMSSMvsSMRun2Legacy_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/MSSMvsSMRun2Legacy/BuildFile
CombineHarvesterMSSMvsSMRun2Legacy_LOC_FLAGS_CXXFLAGS   := -fno-guess-branch-probability -fno-devirtualize -fno-tree-forwprop
CombineHarvesterMSSMvsSMRun2Legacy_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools HiggsAnalysis/CombinedLimit
CombineHarvesterMSSMvsSMRun2Legacy_EX_LIB   := CombineHarvesterMSSMvsSMRun2Legacy
CombineHarvesterMSSMvsSMRun2Legacy_EX_USE   := $(foreach d,$(CombineHarvesterMSSMvsSMRun2Legacy_LOC_USE),$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
CombineHarvesterMSSMvsSMRun2Legacy_PACKAGE := self/src/CombineHarvester/MSSMvsSMRun2Legacy/src
ALL_PRODS += CombineHarvesterMSSMvsSMRun2Legacy
CombineHarvesterMSSMvsSMRun2Legacy_CLASS := LIBRARY
CombineHarvester/MSSMvsSMRun2Legacy_forbigobj+=CombineHarvesterMSSMvsSMRun2Legacy
CombineHarvesterMSSMvsSMRun2Legacy_INIT_FUNC        += $$(eval $$(call Library,CombineHarvesterMSSMvsSMRun2Legacy,src/CombineHarvester/MSSMvsSMRun2Legacy/src,src_CombineHarvester_MSSMvsSMRun2Legacy_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
