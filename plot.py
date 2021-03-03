import ROOT
import Dumbledraw.dumbledraw as dd
import Dumbledraw.rootfile_parser as rootfile_parser
import Dumbledraw.styles as styles

from array import array
shapefile=ROOT.TFile("/work/rschmieder/nmssm_condor_analysis/sm-htt-analysis/output/ml/parametrized_nn_mH1000/2016_et/fold0_training_dataset.root","READ") 
tree=shapefile.Get("NMSSM")
arrBins=array("d",(60,4000))
histo=ROOT.TH1F("hist","hist",80, 57.5,857.5)

for event in tree:
    histo.Fill(event.NMSSM_light_mass)

def plot(hist):
        width = 600
        plot = dd.Plot([[0.30, 0.28]], "ModTDR", r=0.1, l=0.14, width=width)
        plot.add_hist(hist, "process_name1", "hist")
        plot.setGraphStyle("process_name1",
                "hist",
                fillcolor=0,
                 linecolor=1)
        plot.subplot(0).get_hist("hist")        
        plot.subplot(0).setYlabel("Events")
        plot.subplot(0).setXlabel("\mathrm{h_{S}} (\mathrm{GeV})")
        plot.scaleYLabelSize(0.75)
        plot.scaleXLabelSize(0.75)
        plot.scaleYTitleSize(0.75)
        plot.scaleXTitleSize(0.75)
        procs_to_draw = ["hist"]
        plot.subplot(0).Draw(procs_to_draw)
        #plot.add_legend(width=0.4, height=0.20, pos=3)
       #plot.legend(0).add_entry(0, "process_name1", "hist", 'l')
        #plot.legend(0).Draw()
        plot.DrawCMS(position="outside", preliminary=False, ownwork=True)
        era=2016
        if era == "2016":
                plot.DrawLumi("35.9 fb^{-1} (2016, 13 TeV)", textsize=0.5)
        elif era == "2017":
                plot.DrawLumi("41.5 fb^{-1} (2017, 13 TeV)", textsize=0.5)
        elif era == "2018":
                plot.DrawLumi("59.7 fb^{-1} (2018, 13 TeV)", textsize=0.5)
        else:
                plot.DrawLumi("137.2 fb^{-1} (13 TeV)", textsize=0.5)

        #plot.DrawChannelCategoryLabel("{era}-{channel}-{var}-{cat}".format(era=era,channel=channel, cat=category, nn_cat=nncat,var=variable),textsize=0.03)
        #plot.save("hist_comparison/nn_shapes/{era}_{channel}/ratio_{var}_{cat}_{nn_cat}.png".format(era=era, channel=channel, cat=category, nn_cat=nncat, var=variable))

        plot.save("plots/nmssm_distribution_mH1000.png")

plot(histo)

