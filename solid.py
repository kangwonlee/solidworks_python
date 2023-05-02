import pathlib
import win32com.client

# Connect to the SolidWorks application
swApp = win32com.client.Dispatch("SldWorks.Application")

# Open a new part document
swModel = swApp.NewDocument("Part", 0, 0, 0)

# Get the active sketch
swSketch = swModel.SketchManager.ActiveSketch

# Create a new sketch circle
swCircle = swSketch.CreateCircle(0, 0, 0, 0.01)

# Create an extruded boss feature from the sketch
swExtrude = swModel.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.01, 0.01, False, False, False, False, 0, 0, False, False, False, False, True, True, True, 0, 0, False)


folder = pathlib.Path(__file__).parent()

# Save the document
swModel.SaveAs(str(folder/"MyPart.SLDPRT"))

