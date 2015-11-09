package uk.ac.diamond.scisoft.analysis.powder.csdinterface;

import java.util.Map;

import org.dawnsci.python.rpc.AnalysisRpcPythonPyDevService;
import org.dawnsci.python.rpc.PythonRunScriptService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class CSDPython {
	
	private static final Logger logger = LoggerFactory.getLogger(CSDPython.class);
	private AnalysisRpcPythonPyDevService pyDevRpcService;
	private PythonRunScriptService pythonScriptService;
	
	public CSDPython(double[] cellLengths, double[] cellAngles) {
		
		try {
			pyDevRpcService = new AnalysisRpcPythonPyDevService(false);
			pythonScriptService = new PythonRunScriptService(pyDevRpcService);
		} catch (Exception e) {
			logger.error("Cannot start PyDev Python Service", e);
		}
		
		//data should be in the form varName:value
		
		Map<String, Object> results = pythonScriptService.runScript(scriptPath, data);
		
	}
		
		
		
		
		
		
		
		
		
		
		
		
		
//		
//		protected OperationData process(IDataset input, IMonitor monitor) throws OperationException {
//			
//			if (s == null || pythonRunScriptService == null) throw new OperationException(this, "Could not create python interpreter");
//			if (model.getFilePath() == null || model.getFilePath().isEmpty()) throw new OperationException(this, "Path to script not set");
//			
//			Map<String,Object> inputs = packInput(input);
//			
//			try {
//				Map<String, Object> out = pythonRunScriptService.runScript(model.getFilePath(), inputs);
//				return packAndValidateMap(out);
//			} catch (Exception e) {
//				throw new OperationException(this, "Could not run " + model.getFilePath());
//			}
	}
		
