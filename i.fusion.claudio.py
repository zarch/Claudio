#!/usr/bin/env python

############################################################################
#
# MODULE:	i.fusion.brovey
# AUTHOR(S):	Markus Neteler. <neteler itc it>
#               Converted to Python by Glynn Clements
# PURPOSE:	Brovey transform to merge
#                 - LANDSAT-7 MS (2, 4, 5) and pan (high res)
#                 - SPOT MS and pan (high res)
#                 - QuickBird MS and pan (high res)
#
# COPYRIGHT:	(C) 2002-2008 by the GRASS Development Team
#
#		This program is free software under the GNU General Public
#		License (>=v2). Read the file COPYING that comes with GRASS
#		for details.
#
# REFERENCES:
#             (?) Roller, N.E.G. and Cox, S., 1980. Comparison of Landsat MSS
#                and merged MSS/RBV data for analysis of natural vegetation.
#                Proc. of the 14th International Symposium on Remote Sensing
#                of Environment, San Jose, Costa Rica, 23-30 April, pp. 1001-1007.
#
#               for LANDSAT 5: see Pohl, C 1996 and others
#
# TODO:         add overwrite test at beginning of the script
#############################################################################

#%Module
#%  description: Brovey transform to merge multispectral and high-res panchromatic channels
#%  keywords: imagery, fusion, Brovey
#%End
#%Flag
#%  key: l
#%  description: LANDSAT sensor
#%  guisection: Sensor
#%END
#%Flag
#%  key: q
#%  description: QuickBird sensor
#%  guisection: Sensor
#%END
#%Flag
#%  key: s
#%  description: SPOT sensor
#%  guisection: Sensor
#%END
#%option
#% key: ms1
#% type: string
#% gisprompt: old,cell,raster
#% description: Name of input raster map (green: tm2 | qbird_green | spot1)
#% required : yes
#%end
#%option
#% key: ms2
#% type: string
#% gisprompt: old,cell,raster
#% description: Name of input raster map (NIR: tm4 | qbird_nir | spot2
#% required : yes
#%end
#%option
#% key: ms3
#% type: string
#% gisprompt: old,cell,raster
#% description: Name of input raster map (MIR; tm5 | qbird_red | spot3
#% required : yes
#%end
#%option
#% key: pan
#% type: string
#% gisprompt: old,cell,raster
#% description: Name of input raster map (etmpan | qbird_pan | spotpan)
#% required : yes
#%end
#%option
#% key: outputprefix
#% type: string
#% gisprompt: new,cell,raster
#% description: Name for output raster map prefix (e.g. 'brov')
#% required : yes
#%end

from grass.script import core as grass

def main(options, flags):
    """i.fusion.claudio -l -q -s --overwrite ms1=B2@user1 ms2=B3@user1 ms3=asp@user1 pan=B7@user1 outputprefix=aspect
{'outputprefix': 'aspect', 'ms3': 'asp@user1', 'ms2': 'B3@user1', 'ms1': 'B2@user1', 'pan': 'B7@user1'}
{'q': True, 's': True, 'l': True}
    """
    print options
    print flags


if __name__ == "__main__":
    options, flags = grass.parser()
    main(options, flags)
