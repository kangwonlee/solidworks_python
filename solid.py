import pathlib
import win32com.client

# Connect to the SolidWorks application
swApp = win32com.client.Dispatch("SldWorks.Application")

# Open a new part document
swModel = swApp.NewDocument("Part", 0, 0, 0)

# Create a new sketch plane
swSketchPlane = swModel.SketchManager.InsertSketch(True)

# Get the sketch object
swSketch = swModel.SketchManager.ActiveSketch

# Draw a circle in the sketch
swCircle = swSketch.CreateCircle(0, 0, 0, 0.01)

# Exit the sketch
swModel.ClearSelection2(True)
swModel.SketchManager.InsertSketch(False)

# Create an extruded boss feature from the sketch
swExtrude = swModel.FeatureManager.FeatureExtrusion2(True, False, False, 0, 0, 0.01, 0.01, False, False, False, False, 0, 0, False, False, False, False, True, True, True, 0, 0, False)


folder = pathlib.Path(__file__).parent()

# Save the document
swModel.SaveAs(str(folder/"MyPart.SLDPRT"))

