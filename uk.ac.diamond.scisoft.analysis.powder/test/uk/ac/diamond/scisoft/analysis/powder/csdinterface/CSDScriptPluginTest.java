package uk.ac.diamond.scisoft.analysis.powder.csdinterface;

import java.util.Map;

import org.junit.Assert;
import org.junit.Test;

public class CSDScriptPluginTest {
	
//	private String getScript(String scriptName) throws IOException {
//		return BundleUtils.getBundleLocation("uk.ac.diamond.scisoft.analysis.powder").getAbsolutePath()
//				+"/test/uk/ac/diamond/scisoft/analysis/powder/test"+scriptName;
//	}
	
	@Test
	public void testCSDCellSearch() {
		//These are values for AABHTZ
		double[] cellLengths = new double[]{11.372, 10.272, 7.359};
		double[] cellAngles = new double[]{108.75, 71.07, 96.16};
		
		CSDPython csdCS = new CSDPython(0, cellLengths, cellAngles);
		Map<String, Object> results = csdCS.run();
		
		Assert.assertTrue(results.size() >= 4);
		
		
	}

}
