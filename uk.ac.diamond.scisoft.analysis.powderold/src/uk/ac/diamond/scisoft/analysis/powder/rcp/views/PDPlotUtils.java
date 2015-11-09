package uk.ac.diamond.scisoft.analysis.powder.rcp.views;

import java.util.List;

import org.eclipse.dawnsci.analysis.api.dataset.IDataset;
import org.eclipse.dawnsci.analysis.dataset.impl.Dataset;
import org.eclipse.dawnsci.analysis.dataset.impl.DatasetFactory;
import org.eclipse.dawnsci.plotting.api.IPlottingSystem;
import org.eclipse.ui.IViewPart;
import org.eclipse.ui.IWorkbenchPage;

public class PDPlotUtils {
	
	/**
	 * This is a temporary wrapper to get away from the former PlotView class.
	 * This is relying on names of the datasets being set correctly, which I
	 * think is foolish. TODO: We need a better solution 
	 */
	public static IDataset[] getDataForPlot(List<IDataset> inData) {
		IDataset intensity = null;
		IDataset x = null;
		for (IDataset currData : inData) {
			if (currData.getName().equals("Intensity"))
				intensity = currData;
			else if (currData.getName().equals("D_space")) {
				x = DatasetFactory.createRange(currData.getSize(), Dataset.INT32);
			} else {
				x = currData;
			}
		}
		return new IDataset[]{x, intensity};
	}

}
