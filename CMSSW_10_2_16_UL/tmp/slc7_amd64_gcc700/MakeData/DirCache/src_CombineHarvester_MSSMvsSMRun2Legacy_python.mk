ifeq ($(strip $(PyCombineHarvesterMSSMvsSMRun2Legacy)),)
PyCombineHarvesterMSSMvsSMRun2Legacy := self/src/CombineHarvester/MSSMvsSMRun2Legacy/python
src_CombineHarvester_MSSMvsSMRun2Legacy_python_parent := 
ALL_PYTHON_DIRS += $(patsubst src/%,%,src/CombineHarvester/MSSMvsSMRun2Legacy/python)
PyCombineHarvesterMSSMvsSMRun2Legacy_files := $(patsubst src/CombineHarvester/MSSMvsSMRun2Legacy/python/%,%,$(wildcard $(foreach dir,src/CombineHarvester/MSSMvsSMRun2Legacy/python ,$(foreach ext,$(SRC_FILES_SUFFIXES),$(dir)/*.$(ext)))))
PyCombineHarvesterMSSMvsSMRun2Legacy_LOC_USE := self  
PyCombineHarvesterMSSMvsSMRun2Legacy_PACKAGE := self/src/CombineHarvester/MSSMvsSMRun2Legacy/python
ALL_PRODS += PyCombineHarvesterMSSMvsSMRun2Legacy
PyCombineHarvesterMSSMvsSMRun2Legacy_INIT_FUNC        += $$(eval $$(call PythonProduct,PyCombineHarvesterMSSMvsSMRun2Legacy,src/CombineHarvester/MSSMvsSMRun2Legacy/python,src_CombineHarvester_MSSMvsSMRun2Legacy_python,1,1,$(SCRAMSTORENAME_PYTHON),$(SCRAMSTORENAME_LIB),,))
else
$(eval $(call MultipleWarningMsg,PyCombineHarvesterMSSMvsSMRun2Legacy,src/CombineHarvester/MSSMvsSMRun2Legacy/python))
endif
ALL_COMMONRULES += src_CombineHarvester_MSSMvsSMRun2Legacy_python
src_CombineHarvester_MSSMvsSMRun2Legacy_python_INIT_FUNC += $$(eval $$(call CommonProductRules,src_CombineHarvester_MSSMvsSMRun2Legacy_python,src/CombineHarvester/MSSMvsSMRun2Legacy/python,PYTHON))
