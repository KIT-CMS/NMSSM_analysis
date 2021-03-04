src_CombineHarvester_MSSMvsSMRun2Legacy_scripts_files := $(filter-out \#% %\#,$(notdir $(wildcard $(foreach dir,$(LOCALTOP)/src/CombineHarvester/MSSMvsSMRun2Legacy/scripts,$(dir)/*))))
$(eval $(call Src2StoreCopy,src_CombineHarvester_MSSMvsSMRun2Legacy_scripts,src/CombineHarvester/MSSMvsSMRun2Legacy/scripts,$(SCRAMSTORENAME_BIN),*))
