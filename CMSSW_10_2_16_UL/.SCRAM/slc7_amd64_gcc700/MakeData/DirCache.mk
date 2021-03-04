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
ifeq ($(strip $(CombineHarvester/CombinePdfs)),)
ALL_COMMONRULES += src_CombineHarvester_CombinePdfs_src
src_CombineHarvester_CombinePdfs_src_parent := CombineHarvester/CombinePdfs
src_CombineHarvester_CombinePdfs_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_CombineHarvester_CombinePdfs_src,src/CombineHarvester/CombinePdfs/src,LIBRARY))
CombineHarvesterCombinePdfs := self/CombineHarvester/CombinePdfs
CombineHarvester/CombinePdfs := CombineHarvesterCombinePdfs
CombineHarvesterCombinePdfs_files := $(patsubst src/CombineHarvester/CombinePdfs/src/%,%,$(wildcard $(foreach dir,src/CombineHarvester/CombinePdfs/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
CombineHarvesterCombinePdfs_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombinePdfs/BuildFile
CombineHarvesterCombinePdfs_LOC_FLAGS_CXXFLAGS   := -fno-guess-branch-probability -fno-devirtualize -fno-tree-forwprop
CombineHarvesterCombinePdfs_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy CombineHarvester/CombineTools HiggsAnalysis/CombinedLimit
CombineHarvesterCombinePdfs_EX_LIB   := CombineHarvesterCombinePdfs
CombineHarvesterCombinePdfs_EX_USE   := $(foreach d,$(CombineHarvesterCombinePdfs_LOC_USE),$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
CombineHarvesterCombinePdfs_PACKAGE := self/src/CombineHarvester/CombinePdfs/src
ALL_PRODS += CombineHarvesterCombinePdfs
CombineHarvesterCombinePdfs_CLASS := LIBRARY
CombineHarvester/CombinePdfs_forbigobj+=CombineHarvesterCombinePdfs
CombineHarvesterCombinePdfs_INIT_FUNC        += $$(eval $$(call Library,CombineHarvesterCombinePdfs,src/CombineHarvester/CombinePdfs/src,src_CombineHarvester_CombinePdfs_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
ifeq ($(strip $(HiggsAnalysis/CombinedLimit)),)
ALL_COMMONRULES += src_HiggsAnalysis_CombinedLimit_src
src_HiggsAnalysis_CombinedLimit_src_parent := HiggsAnalysis/CombinedLimit
src_HiggsAnalysis_CombinedLimit_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_HiggsAnalysis_CombinedLimit_src,src/HiggsAnalysis/CombinedLimit/src,LIBRARY))
HiggsAnalysisCombinedLimit := self/HiggsAnalysis/CombinedLimit
HiggsAnalysis/CombinedLimit := HiggsAnalysisCombinedLimit
HiggsAnalysisCombinedLimit_files := $(patsubst src/HiggsAnalysis/CombinedLimit/src/%,%,$(wildcard $(foreach dir,src/HiggsAnalysis/CombinedLimit/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
HiggsAnalysisCombinedLimit_BuildFile    := $(WORKINGDIR)/cache/bf/src/HiggsAnalysis/CombinedLimit/BuildFile
HiggsAnalysisCombinedLimit_LOC_LIB   := Smatrix
HiggsAnalysisCombinedLimit_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt boost_program_options boost_filesystem
HiggsAnalysisCombinedLimit_LCGDICTS  := x 
HiggsAnalysisCombinedLimit_PRE_INIT_FUNC += $$(eval $$(call LCGDict,HiggsAnalysisCombinedLimit,src/HiggsAnalysis/CombinedLimit/src/classes.h,src/HiggsAnalysis/CombinedLimit/src/classes_def.xml,$(SCRAMSTORENAME_LIB),$(GENREFLEX_ARGS) --fail_on_warnings,))
HiggsAnalysisCombinedLimit_EX_LIB   := HiggsAnalysisCombinedLimit
HiggsAnalysisCombinedLimit_EX_USE   := $(foreach d,$(HiggsAnalysisCombinedLimit_LOC_USE),$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
HiggsAnalysisCombinedLimit_PACKAGE := self/src/HiggsAnalysis/CombinedLimit/src
ALL_PRODS += HiggsAnalysisCombinedLimit
HiggsAnalysisCombinedLimit_CLASS := LIBRARY
HiggsAnalysis/CombinedLimit_forbigobj+=HiggsAnalysisCombinedLimit
HiggsAnalysisCombinedLimit_INIT_FUNC        += $$(eval $$(call Library,HiggsAnalysisCombinedLimit,src/HiggsAnalysis/CombinedLimit/src,src_HiggsAnalysis_CombinedLimit_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
ifeq ($(strip $(CombineHarvester/CombineTools)),)
ALL_COMMONRULES += src_CombineHarvester_CombineTools_src
src_CombineHarvester_CombineTools_src_parent := CombineHarvester/CombineTools
src_CombineHarvester_CombineTools_src_INIT_FUNC := $$(eval $$(call CommonProductRules,src_CombineHarvester_CombineTools_src,src/CombineHarvester/CombineTools/src,LIBRARY))
CombineHarvesterCombineTools := self/CombineHarvester/CombineTools
CombineHarvester/CombineTools := CombineHarvesterCombineTools
CombineHarvesterCombineTools_files := $(patsubst src/CombineHarvester/CombineTools/src/%,%,$(wildcard $(foreach dir,src/CombineHarvester/CombineTools/src ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
CombineHarvesterCombineTools_BuildFile    := $(WORKINGDIR)/cache/bf/src/CombineHarvester/CombineTools/BuildFile
CombineHarvesterCombineTools_LOC_FLAGS_CXXFLAGS   := -fno-guess-branch-probability -fno-devirtualize -fno-tree-forwprop
CombineHarvesterCombineTools_SKIP_FILES   := $$(shell make -f ${CMSSW_BASE}/src/CombineHarvester/CombineTools/makeGitVersion)
CombineHarvesterCombineTools_LOC_USE := self  root rootmath roofit roostats histfactory libxml2 vdt python boost_program_options boost_filesystem boost_python boost_regex rootpy HiggsAnalysis/CombinedLimit
CombineHarvesterCombineTools_EX_LIB   := CombineHarvesterCombineTools
CombineHarvesterCombineTools_EX_USE   := $(foreach d,$(CombineHarvesterCombineTools_LOC_USE),$(if $($(d)_EX_FLAGS_NO_RECURSIVE_EXPORT),,$d))
CombineHarvesterCombineTools_PACKAGE := self/src/CombineHarvester/CombineTools/src
ALL_PRODS += CombineHarvesterCombineTools
CombineHarvesterCombineTools_CLASS := LIBRARY
CombineHarvester/CombineTools_forbigobj+=CombineHarvesterCombineTools
CombineHarvesterCombineTools_INIT_FUNC        += $$(eval $$(call Library,CombineHarvesterCombineTools,src/CombineHarvester/CombineTools/src,src_CombineHarvester_CombineTools_src,$(SCRAMSTORENAME_BIN),,$(SCRAMSTORENAME_LIB),$(SCRAMSTORENAME_LOGS)))
endif
