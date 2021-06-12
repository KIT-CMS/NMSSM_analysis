date=2021_06_09
tag=HIG-20-014_limitplots


mkdir -p /etpwww/web/rschmieder/public_html/${date}/${tag}
cp -r  /work/rschmieder/plot_repo_janek_limits/HIG-20-014/plots/limits/combined/all/*.{pdf,png} /etpwww/web/rschmieder/public_html/${date}/${tag}/.
python webgallery/gallery.py /etpwww/web/rschmieder/public_html/${date}/${tag} --metadata nmssm 
