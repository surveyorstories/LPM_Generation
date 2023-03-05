"""
Model exported as python.
Name : LPM Processing model
Group :""
With QGIS : 32802
"""

from qgis.core import QgsProcessing
from qgis.core import QgsProcessingAlgorithm
from qgis.core import QgsProcessingMultiStepFeedback
from qgis.core import QgsProcessingParameterVectorLayer
from qgis.core import QgsProcessingParameterField
from qgis.core import QgsProcessingParameterDistance
from qgis.core import QgsProcessingParameterFile
from qgis.core import QgsProcessingParameterString
from qgis.core import QgsExpression
import processing


class LpmProcessingModel(QgsProcessingAlgorithm):

    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterVectorLayer('village_final_shape_file', 'Village Final Shape File', types=[QgsProcessing.TypeVectorPolygon], defaultValue=None))
        self.addParameter(QgsProcessingParameterField('lpm_number_column_choose_your_lpm_no_column_according_to_your_shape_file', 'LPM Number Column (Choose Your LPM NO column according to your shape File)', type=QgsProcessingParameterField.Any, parentLayerParameterName='village_final_shape_file', allowMultiple=False, defaultValue=None))
        self.addParameter(QgsProcessingParameterField('area_in_acres_column_choose_your_acre_column_according_to_your_shape_file', 'Area in Acres Column (Choose Your Acre column according to your shape File)', type=QgsProcessingParameterField.Any, parentLayerParameterName='village_final_shape_file', allowMultiple=False, defaultValue=None))
        self.addParameter(QgsProcessingParameterField('area_in_hectares_column_choose_your_hectares_column_according_to_your_shape_file', 'Area in Hectares Column (Choose Your Hectares column according to your shape File)', type=QgsProcessingParameterField.Any, parentLayerParameterName='village_final_shape_file', allowMultiple=False, defaultValue=None))
        self.addParameter(QgsProcessingParameterDistance('prill_line_length_multi_ring_length', 'Prill Line Length (Multi Ring Length)', parentParameterName='village_final_shape_file', minValue=1, maxValue=20, defaultValue=3))
        self.addParameter(QgsProcessingParameterFile('choose_your_ulpin_layer', 'Choose Your ULPIN Layer', behavior=QgsProcessingParameterFile.File, fileFilter='All Files (*.*)', defaultValue=None))
        self.addParameter(QgsProcessingParameterString('district_name_please_enter_district_name_in_telugu', 'District Name (Please enter District name in Telugu)', multiLine=False, defaultValue=''))
        self.addParameter(QgsProcessingParameterString('mandal_name_please_enter_mandal_name_in_telugu', 'Mandal Name (Please enter Mandal name in Telugu)', multiLine=False, defaultValue=''))
        self.addParameter(QgsProcessingParameterString('village_name_in_telugu_please_enter_your_village_name_in_telugu', 'Village Name in Telugu (Please enter your village name in telugu)', multiLine=False, defaultValue=''))
        self.addParameter(QgsProcessingParameterString('please_enter_7_digit_village_code', 'Please enter 7 Digit village Code ', multiLine=False, defaultValue=''))
        self.addParameter(QgsProcessingParameterString('village_surveyor_name', 'Village Surveyor Name', multiLine=False, defaultValue=''))
        self.addParameter(QgsProcessingParameterFile('polygon_style_file', 'Polygon Style File', optional=True, behavior=QgsProcessingParameterFile.File, fileFilter='All Files (*.*)', defaultValue=None))
        self.addParameter(QgsProcessingParameterFile('exploded_lines_style_file', 'Exploded Lines Style File', optional=True, behavior=QgsProcessingParameterFile.File, fileFilter='All Files (*.*)', defaultValue=None))
        self.addParameter(QgsProcessingParameterFile('final_vertices_style_file', 'Final Vertices Style File', optional=True, behavior=QgsProcessingParameterFile.File, fileFilter='All Files (*.*)', defaultValue=None))
        self.addParameter(QgsProcessingParameterFile('prill_line_style_file', 'Prill Line Style File', optional=True, behavior=QgsProcessingParameterFile.File, fileFilter='All Files (*.*)', defaultValue=None))
        self.addParameter(QgsProcessingParameterFile('choose_your_rlrdlr_form38_resurvey_land_register', 'Choose Your RLR/DLR (Form-38 Resurvey Land Register)', behavior=QgsProcessingParameterFile.File, fileFilter='All Files (*.*)', defaultValue=None))

    def processAlgorithm(self, parameters, context, model_feedback):
        # Use a multi-step feedback, so that individual child algorithm progress reports are adjusted for the
        # overall progress through the model
        feedback = QgsProcessingMultiStepFeedback(40, model_feedback)
        results = {}
        outputs = {}

        # District_name
        alg_params = {
            'NAME': 'District_Name',
            'VALUE': parameters['district_name_please_enter_district_name_in_telugu']
        }
        outputs['District_name'] = processing.run('native:setprojectvariable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(1)
        if feedback.isCanceled():
            return {}

        # LPM_NO
        alg_params = {
            'NAME': 'LPM_NO',
            'VALUE': parameters['lpm_number_column_choose_your_lpm_no_column_according_to_your_shape_file']
        }
        outputs['Lpm_no'] = processing.run('native:setprojectvariable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(2)
        if feedback.isCanceled():
            return {}

        # Polygon spatial index
        alg_params = {
            'INPUT': parameters['village_final_shape_file']
        }
        outputs['PolygonSpatialIndex'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(3)
        if feedback.isCanceled():
            return {}

        # Village_Name
        alg_params = {
            'NAME': 'Village_Name',
            'VALUE': parameters['village_name_in_telugu_please_enter_your_village_name_in_telugu']
        }
        outputs['Village_name'] = processing.run('native:setprojectvariable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(4)
        if feedback.isCanceled():
            return {}

        # Area_in_Acres
        alg_params = {
            'NAME': 'Area_in_Acres',
            'VALUE': parameters['area_in_acres_column_choose_your_acre_column_according_to_your_shape_file']
        }
        outputs['Area_in_acres'] = processing.run('native:setprojectvariable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(5)
        if feedback.isCanceled():
            return {}

        # Mandal_name
        alg_params = {
            'NAME': 'Mandal_Name',
            'VALUE': parameters['mandal_name_please_enter_mandal_name_in_telugu']
        }
        outputs['Mandal_name'] = processing.run('native:setprojectvariable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(6)
        if feedback.isCanceled():
            return {}

        # Ref_Col Calcluation
        alg_params = {
            'FIELD_LENGTH': 10,
            'FIELD_NAME': 'Ref_Col',
            'FIELD_PRECISION': 0,
            'FIELD_TYPE': 1,  # Integer (32 bit)
            'FORMULA': ' attribute( @lpm_number_column_choose_your_lpm_no_column_according_to_your_shape_file)',
            'INPUT': parameters['village_final_shape_file'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Ref_colCalcluation'] = processing.run('native:fieldcalculator', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(7)
        if feedback.isCanceled():
            return {}

        # Save ULPIN Layer to Project Folder
        alg_params = {
            'DATASOURCE_OPTIONS': '',
            'INPUT': QgsExpression(' @choose_your_ulpin_layer ').evaluate(),
            'LAYER_NAME': '',
            'LAYER_OPTIONS': '',
            'OUTPUT': QgsExpression("@project_folder  ||  '\\\\ULPIN.csv'").evaluate(),
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['SaveUlpinLayerToProjectFolder'] = processing.run('native:savefeatures', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(8)
        if feedback.isCanceled():
            return {}

        # Extract vertices
        alg_params = {
            'INPUT': outputs['Ref_colCalcluation']['OUTPUT'],
            'OUTPUT': QgsExpression("@project_folder  || '\\\\Vertices.shp'").evaluate(),
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractVertices'] = processing.run('native:extractvertices', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(9)
        if feedback.isCanceled():
            return {}

        # Boundary
        alg_params = {
            'INPUT': outputs['Ref_colCalcluation']['OUTPUT'],
            'OUTPUT': QgsExpression("@project_folder  || '\\\\Boundary.shp'").evaluate(),
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Boundary'] = processing.run('native:boundary', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(10)
        if feedback.isCanceled():
            return {}

        # Village Surveyor Name
        alg_params = {
            'NAME': 'VS_Name',
            'VALUE': parameters['village_surveyor_name']
        }
        outputs['VillageSurveyorName'] = processing.run('native:setprojectvariable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(11)
        if feedback.isCanceled():
            return {}

        # Area_in_Hectares
        alg_params = {
            'NAME': 'Area_in_Hectares',
            'VALUE': parameters['area_in_hectares_column_choose_your_hectares_column_according_to_your_shape_file']
        }
        outputs['Area_in_hectares'] = processing.run('native:setprojectvariable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(12)
        if feedback.isCanceled():
            return {}

        # Village_code
        alg_params = {
            'NAME': 'Village_Code',
            'VALUE': parameters['please_enter_7_digit_village_code']
        }
        outputs['Village_code'] = processing.run('native:setprojectvariable', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(13)
        if feedback.isCanceled():
            return {}

        # Multi-ring buffer (constant distance)
        alg_params = {
            'DISTANCE': parameters['prill_line_length_multi_ring_length'],
            'INPUT': QgsExpression("@project_folder  || '\\\\Vertices.shp'").evaluate(),
            'OUTPUT': QgsExpression("@project_folder  || '\\\\Multi_Ring.shp'").evaluate(),
            'RINGS': 1,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['MultiringBufferConstantDistance'] = processing.run('native:multiringconstantbuffer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(14)
        if feedback.isCanceled():
            return {}

        # Extract RLR by expression
        alg_params = {
            'EXPRESSION': ' "Field4" != \'4a\'  and\r\n "Field4" != \'Extent\'\r',
            'INPUT': QgsExpression('@choose_your_rlrdlr_form38_resurvey_land_register').evaluate(),
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExtractRlrByExpression'] = processing.run('native:extractbyexpression', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(15)
        if feedback.isCanceled():
            return {}

        # Explode lines
        alg_params = {
            'INPUT': QgsExpression("@project_folder  || '\\\\Boundary.shp'").evaluate(),
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['ExplodeLines'] = processing.run('native:explodelines', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(16)
        if feedback.isCanceled():
            return {}

        # Multiring spatial index
        alg_params = {
            'INPUT': outputs['MultiringBufferConstantDistance']['OUTPUT']
        }
        outputs['MultiringSpatialIndex'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(17)
        if feedback.isCanceled():
            return {}

        # Boundary spatial index
        alg_params = {
            'INPUT': outputs['Boundary']['OUTPUT']
        }
        outputs['BoundarySpatialIndex'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(18)
        if feedback.isCanceled():
            return {}

        # Refactor Exploded Lines
        alg_params = {
            'FIELDS_MAPPING': [{'expression': '"Ref_Col"','length': 10,'name': 'Ref_Col','precision': 0,'sub_type': 0,'type': 2,'type_name': 'integer'},{'expression': 'length3D( $geometry)','length': 10,'name': 'Length','precision': 1,'sub_type': 0,'type': 6,'type_name': 'double precision'}],
            'INPUT': outputs['ExplodeLines']['OUTPUT'],
            'OUTPUT': QgsExpression("@project_folder  || '\\\\Exploded_Lines.shp'").evaluate(),
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['RefactorExplodedLines'] = processing.run('native:refactorfields', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(19)
        if feedback.isCanceled():
            return {}

        # Load Exploded_Lines into project
        alg_params = {
            'INPUT': outputs['RefactorExplodedLines']['OUTPUT'],
            'NAME': 'Exploded_Lines'
        }
        outputs['LoadExploded_linesIntoProject'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(20)
        if feedback.isCanceled():
            return {}

        # Load ULPIN Layer into project
        alg_params = {
            'INPUT': outputs['SaveUlpinLayerToProjectFolder']['OUTPUT'],
            'NAME': 'ULPIN'
        }
        outputs['LoadUlpinLayerIntoProject'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(21)
        if feedback.isCanceled():
            return {}

        # Retain fields In RLR
        alg_params = {
            'FIELDS': ['Field1','Field4','Field6','Field8','Field12','Field13','Field14'],
            'INPUT': outputs['ExtractRlrByExpression']['OUTPUT'],
            'OUTPUT': QgsExpression("@project_folder  ||  '\\\\RLR_excel.xlsx'").evaluate(),
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['RetainFieldsInRlr'] = processing.run('native:retainfields', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(22)
        if feedback.isCanceled():
            return {}

        # Refactor Vertices
        alg_params = {
            'FIELDS_MAPPING': [{'expression': "y( transform( $geometry,@layer_crs,\r\n'EPSG:4326'))",'length': 10,'name': 'LATITUDE','precision': 6,'sub_type': 0,'type': 6,'type_name': 'double precision'},{'expression': "x( transform( $geometry,@layer_crs,\r\n'EPSG:4326'))",'length': 10,'name': 'LONGITUDE','precision': 6,'sub_type': 0,'type': 6,'type_name': 'double precision'},{'expression': '$x','length': 10,'name': 'EASTING_X','precision': 1,'sub_type': 0,'type': 6,'type_name': 'double precision'},{'expression': '$y','length': 10,'name': 'NORTHING_Y','precision': 1,'sub_type': 0,'type': 6,'type_name': 'double precision'},{'expression': '"Ref_Col"','length': 10,'name': 'Ref_Col','precision': 0,'sub_type': 0,'type': 4,'type_name': 'int8'}],
            'INPUT': outputs['ExtractVertices']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['RefactorVertices'] = processing.run('native:refactorfields', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(23)
        if feedback.isCanceled():
            return {}

        # Explode Lines spatial index
        alg_params = {
            'INPUT': outputs['LoadExploded_linesIntoProject']['OUTPUT']
        }
        outputs['ExplodeLinesSpatialIndex'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(24)
        if feedback.isCanceled():
            return {}

        # Load RLR into project
        alg_params = {
            'INPUT': outputs['RetainFieldsInRlr']['OUTPUT'],
            'NAME': 'Resurvey_Land_Register'
        }
        outputs['LoadRlrIntoProject'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(25)
        if feedback.isCanceled():
            return {}

        # Delete duplicates by attribute in Vertices
        alg_params = {
            'FIELDS': QgsExpression(" 'Ref_Col;EASTING_X;NORTHING_Y'").evaluate(),
            'INPUT': outputs['RefactorVertices']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['DeleteDuplicatesByAttributeInVertices'] = processing.run('native:removeduplicatesbyattribute', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(26)
        if feedback.isCanceled():
            return {}

        # Clip
        alg_params = {
            'INPUT': outputs['BoundarySpatialIndex']['OUTPUT'],
            'OUTPUT': QgsExpression("@project_folder  || '\\\\Clip.shp'").evaluate(),
            'OVERLAY': outputs['MultiringSpatialIndex']['OUTPUT'],
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['Clip'] = processing.run('native:clip', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(27)
        if feedback.isCanceled():
            return {}

        # Add Point_ID field
        alg_params = {
            'FIELD_NAME': 'Point_ID',
            'GROUP_FIELDS': ['Ref_Col'],
            'INPUT': outputs['DeleteDuplicatesByAttributeInVertices']['OUTPUT'],
            'MODULUS': 0,
            'OUTPUT': QgsExpression("@project_folder  || '\\\\Final_Vertices.shp'\r\n").evaluate(),
            'SORT_ASCENDING': True,
            'SORT_EXPRESSION': '',
            'SORT_NULLS_FIRST': False,
            'START': 1,
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['AddPoint_idField'] = processing.run('native:addautoincrementalfield', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(28)
        if feedback.isCanceled():
            return {}

        # Prill Lines
        alg_params = {
            'INPUT': QgsExpression("@project_folder  || '\\\\Clip.shp'").evaluate(),
            'OUTPUT': QgsExpression("@project_folder  || '\\\\Prill_Lines.shp'").evaluate(),
            'OUTPUT': QgsProcessing.TEMPORARY_OUTPUT
        }
        outputs['PrillLines'] = processing.run('native:explodelines', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(29)
        if feedback.isCanceled():
            return {}

        # Load Final_Vertices into project
        alg_params = {
            'INPUT': outputs['AddPoint_idField']['OUTPUT'],
            'NAME': 'Final_Vertices'
        }
        outputs['LoadFinal_verticesIntoProject'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(30)
        if feedback.isCanceled():
            return {}

        # Load Prill_Lines into project
        alg_params = {
            'INPUT': QgsExpression("@project_folder  || '\\\\Prill_Lines.shp'").evaluate(),
            'NAME': 'Prill_Lines'
        }
        outputs['LoadPrill_linesIntoProject'] = processing.run('native:loadlayer', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(31)
        if feedback.isCanceled():
            return {}

        # Create Final vertices spatial index
        alg_params = {
            'INPUT': outputs['LoadFinal_verticesIntoProject']['OUTPUT']
        }
        outputs['CreateFinalVerticesSpatialIndex'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(32)
        if feedback.isCanceled():
            return {}

        # Create Prill line spatial index
        alg_params = {
            'INPUT': outputs['LoadPrill_linesIntoProject']['OUTPUT']
        }
        outputs['CreatePrillLineSpatialIndex'] = processing.run('native:createspatialindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(33)
        if feedback.isCanceled():
            return {}

        # Create attribute index Final_Vertices
        alg_params = {
            'FIELD': QgsExpression("'Ref_Col;EASTING_X;NORTHING_Y;LATITUDE;LONGITUDE'").evaluate(),
            'INPUT': outputs['LoadFinal_verticesIntoProject']['OUTPUT']
        }
        outputs['CreateAttributeIndexFinal_vertices'] = processing.run('native:createattributeindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(34)
        if feedback.isCanceled():
            return {}

        # Create explde line attribute index
        alg_params = {
            'FIELD': QgsExpression("'Ref_Col;Length'").evaluate(),
            'INPUT': outputs['LoadExploded_linesIntoProject']['OUTPUT']
        }
        outputs['CreateExpldeLineAttributeIndex'] = processing.run('native:createattributeindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(35)
        if feedback.isCanceled():
            return {}

        # Create polygon attribute index
        alg_params = {
            'FIELD': QgsExpression(" '@lpm_number_column_choose_your_lpm_no_column_according_to_your_shape_file ;  @area_in_acres_column_choose_your_acre_column_according_to_your_shape_file ,  @area_in_hectares_column_choose_your_hectares_column_according_to_your_shape_file '").evaluate(),
            'INPUT': parameters['village_final_shape_file']
        }
        outputs['CreatePolygonAttributeIndex'] = processing.run('native:createattributeindex', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(36)
        if feedback.isCanceled():
            return {}

        # Set Polygon style
        alg_params = {
            'INPUT': parameters['village_final_shape_file'],
            'STYLE': QgsExpression(' @polygon_style_file ').evaluate()
        }
        outputs['SetPolygonStyle'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(37)
        if feedback.isCanceled():
            return {}

        # Set Exploded Lines style
        alg_params = {
            'INPUT': outputs['LoadExploded_linesIntoProject']['OUTPUT'],
            'STYLE': QgsExpression(' @exploded_lines_style_file ').evaluate()
        }
        outputs['SetExplodedLinesStyle'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(38)
        if feedback.isCanceled():
            return {}

        # Set Final Vertices style
        alg_params = {
            'INPUT': outputs['LoadFinal_verticesIntoProject']['OUTPUT'],
            'STYLE': QgsExpression(' @final_vertices_style_file ').evaluate()
        }
        outputs['SetFinalVerticesStyle'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)

        feedback.setCurrentStep(39)
        if feedback.isCanceled():
            return {}

        # Set Prill Line style
        alg_params = {
            'INPUT': outputs['LoadPrill_linesIntoProject']['OUTPUT'],
            'STYLE': QgsExpression(' @prill_line_style_file').evaluate()
        }
        outputs['SetPrillLineStyle'] = processing.run('native:setlayerstyle', alg_params, context=context, feedback=feedback, is_child_algorithm=True)
        return results

    def name(self):
        return 'LPM processing model'

    def displayName(self):
        return 'LPM processing model'

    def group(self):
        return 'abc'

    def groupId(self):
        return 'abc'

    def shortHelpString(self):
        return """<html><body><p><!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Calibri'; font-size:10pt; font-weight:400; font-style:normal;">
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" color:#000000; background-color:#ffffff;">This algorithm helps you to generate LPMS of a village </span>Developed for AP Resurvey 2020 Project you can get latest files from our <a href="https://github.com/surveyorstories"><span style=" text-decoration: underline; color:#0000ff;">GitHub</span></a> page </p></body></html></p>
<h2>Input parameters</h2>
<h3>Village Final Shape File</h3>
<p>Please Select your final shapefile of village with zero topology errors and having the columns of LP NO, ACRES and HECTRES</p>
<h3>LPM Number Column (Choose Your LPM NO column according to your shape File)</h3>
<p>Select Land Parcel Column (Attribute Field name ) in your Shapefile </p>
<h3>Area in Acres Column (Choose Your Acre column according to your shape File)</h3>
<p>Select "Acres" Column (Attribute Field name ) in your Shapefile which is calculated using Calculate Geometry Plugin </p>
<h3>Area in Hectares Column (Choose Your Hectares column according to your shape File)</h3>
<p>Select "Hectares" Column (Attribute Field name ) in your Shapefile which is calculated using Calculate Geometry Plugin </p>
<h3>Prill Line Length (Multi Ring Length)</h3>
<p>Enter your Desired Prill line length by default it was set to 3 </p>
<h3>Choose Your ULPIN Layer</h3>
<p>Choose  your ULPIN file of your village in un edited form </p>
<h3>District Name (Please enter District name in Telugu)</h3>
<p>enter your District name in Telugu</p>
<h3>Mandal Name (Please enter Mandal name in Telugu)</h3>
<p>Enter your Mandal Name in Telugu </p>
<h3>Village Name in Telugu (Please enter your village name in telugu)</h3>
<p>enter your Village name in Telugu</p>
<h3>Please enter 7 Digit village Code </h3>
<p>Enter your 7 Digit village code</p>
<h3>Polygon Style File</h3>
<p>Select the polygon_style file</p>
<h3>Choose Your RLR/DLR (Form-38 Resurvey Land Register)</h3>
<p>Select your RLR/DLR excel file without any changes. you can download it from Webland2 tahsildar login </p>
<br><p align="right">Algorithm author: Surveyor Stories </p><p align="right">Algorithm version: Beta-V.1.0</p></body></html>"""

    def createInstance(self):
        return LpmProcessingModel()
